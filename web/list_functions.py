from lxml import etree
from xml.etree import ElementTree as ET
import xmltodict
import json
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
import pprint
from collections import Counter
import itertools

def validate(xml_path, xsd_path):

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


def validNode(domNode, tagName, value):
	nodeVal = domNode.find(tagName).text
	if isinstance(value, list):
		if nodeVal in value or nodeVal[:4] in value:
			return True
	else:
		if nodeVal == value:
			return True
	return False


def showNode(x, root, param):
	if root == 'KKNI':
		jenjang = x.findall('Jenjang')
		for jen in jenjang:
			if jen.find('level').text == param:
				return xmltodict.parse(ET.tostring(jen, 'us-ascii', 'xml'))
	elif root == 'SKKNI':
		listUK = x.find('FungsiKunci').find('FungsiUtama').findall('UnitKompetensi')
		listKomp = []
		for uk in listUK:
			if uk.find('kodeUnit').text in param:
				listKomp.append(xmltodict.parse(ET.tostring(uk, 'us-ascii', 'xml')))
		return listKomp
	elif root == 'PetaOkupasi':
		listK = x.findall('Kompetensi')
		listKomp = []
		for k in listK:
			listKomp.append(xmltodict.parse(ET.tostring(k, 'us-ascii', 'xml')))
		return listKomp

def getJob(codes):
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = """
		PREFIX ok: <http://localhost:5000/okupasi/>
		SELECT ?name
		WHERE
		{{
			?okupasi ok:id ?id ;
				ok:name ?name .

			FILTER(SUBSTR(?id, 1, 4) IN({c})) .
		}}""".format(c=codes[1:-1])

	pprint.pprint(query)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	# pprint.pprint(results)
	keys = results['head']['vars']
	r = results['results']['bindings']
	jobs = []
	for x in r:
		for key in keys:
			jobs.append(x[key]['value'])

	return jobs

def getCompetencies(codes, index=1, comps=[]):
	comps.append(codes)
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = """PREFIX ok: <http://localhost:5000/okupasi/> PREFIX kom: <http://localhost:5000/kompetensi/> select distinct ?reqs where {{ ?kompetensi kom:hasComReq ?reqs . filter(?kompetensi in({c})) }} """.format(c=json.dumps(codes).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1].replace('"', '').replace("file://C:/fakepath/", "kom:"))
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	reqs = []

	for x in results['results']['bindings']:
		if "reqs" in x:
			reqs.append(x['reqs']['value'])
	print query
	intersection = Counter(codes) & Counter(reqs)
	reqs = list(Counter(reqs) - intersection)
	print reqs
	if len(reqs) == 0:
		return comps
	return getCompetencies(reqs, index+1, comps)

def getDesc(codes):
	comps = []
	comps.append([])
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = """PREFIX ok: <http://localhost:5000/okupasi/> PREFIX kom: <http://localhost:5000/kompetensi/> select ?competencies ?reqs where {{ ?okupasi ok:id ?id ; ok:name ?name ; ok:hasCompetencies ?competencies . filter(?name in({c})) optional{{ ?kompetensi kom:hasComReq ?reqs . filter(?kompetensi in(?competencies)) }} }} """.format(c=codes[1:-1])
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	reqs = []

	for x in results['results']['bindings']:
		comps[0].append(x['competencies']['value'])
		if "reqs" in x:
			reqs.append(x['reqs']['value'])
	comps[0] = list(set(comps[0]))
	intersection = Counter(comps[0]) & Counter(reqs)
	reqs = list(Counter(reqs) - intersection)

	if len(reqs) > 0:
		comps.extend(getCompetencies(reqs))
	comps = list(set(itertools.chain.from_iterable(comps)))
	# query = """
	# PREFIX ok: <http://localhost:5000/okupasi/>
	# PREFIX kom: <http://localhost:5000/kompetensi/>
	# select ?key ?content
	# where {{
	#   ?s ?key ?content ;
	#     (kom:hasKnowledge|kom:hasSkill|kom:hasAspect) ?content .
	#     filter(?s in({c}))
	# }}""".format(c=json.dumps(comps).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1]).replace('"', '')

	query = """PREFIX ok: <http://localhost:5000/okupasi/> PREFIX kom: <http://localhost:5000/kompetensi/> select ?key ?content where {{ ?s ?key ?content ; (kom:hasAspect|kom:hasContextEval|kom:hasContextVar|kom:hasKnowledge|kom:hasNS|kom:hasPRP|kom:hasSkill|kom:hasAttitude) ?content . filter(?s in({c})) }}""".format(c=json.dumps(comps).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1]).replace('"', '').replace("file://C:/fakepath/", "kom:")
	pprint.pprint(query)
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	bind = results['results']['bindings']
	com = {}
	for x in bind:
		currKey = x["key"]["value"]
		if currKey not in com:
			com[currKey] = []

		com[currKey].append(x["content"]["value"])

	for key in com:
		new_key = key.rsplit('/', 1)[-1]
		com[new_key] = list(set(com.pop(key)))
	com["Kompetensi"] = comps
	# pprint.pprint(com)

	return com
