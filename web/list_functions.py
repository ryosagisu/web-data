from lxml import etree
from xml.etree import ElementTree as ET
import xmltodict
import json
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON

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
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server/repositories/skripsi")
	query = """
		PREFIX ok: <http://localhost:5000/okupasi/>
		SELECT ?name
		WHERE
		{{
			?okupasi ok:id ?id ;
				ok:name ?name .

			FILTER(SUBSTR(?id, 1, 4) IN({c})) .
		}}""".format(c=codes[1:-1])

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	keys = results['head']['vars']
	r = results['results']['bindings']

	jobs = []
	for x in r:
		for key in keys:
			jobs.append(x[key]['value'])

	return jobs

# def getJob(codes):
# 	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server/repositories/skripsi")
# 	query = """
# 		PREFIX ok: <http://localhost:5000/okupasi/>
# 		SELECT ?name
# 		WHERE
# 		{{
# 			?okupasi ok:id ?id ;
# 				ok:name ?name .

# 			FILTER(SUBSTR(?id, 1, 4) IN({c})) .
# 		}}""".format(c=codes[1:-1])

# 	sparql.setQuery(query)
# 	sparql.setReturnFormat(JSON)
# 	results = sparql.query().convert()
# 	keys = results['head']['vars']
# 	r = results['results']['bindings']

# 	jobs = []
# 	for x in r:
# 		for key in keys:
# 			jobs.append(x[key]['value'])

# 	return jobs

def getCompetencies(codes):
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server/repositories/skripsi")
	query = """
	PREFIX ok: <http://localhost:5000/okupasi/>
	PREFIX kom: <http://localhost:5000/kompetensi/>
	select distinct ?competency
	where
	{{
	  ?okupasi ok:id ?id ;
	           ok:name ?name ;
	           ok:hasCompetencies ?competencies .
	  filter(?name in({c}))

	 {{
	    select ?competency where{{
	      ?competencies kom:hasComReq+ ?x
	      bind(?competencies as ?competency)
	    }}
	  }} union {{
	    select ?competency where {{
	      ?competencies kom:hasComReq+ ?y
	      bind(?y as ?competency)
	    }}
	  }}
	}}""".format(c=codes[1:-1])
	print query

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	keys = results['head']['vars']
	bind = results['results']['bindings']
	comps = []
	print results
	for x in bind:
		for key in keys:
			comps.append(x[key]['value'])

	query = """
	PREFIX ok: <http://localhost:5000/okupasi/>
	PREFIX kom: <http://localhost:5000/kompetensi/>
	select ?key ?content
	where {{
	  ?s ?key ?content ;
	    (kom:hasKnowledge|kom:hasSkill|kom:hasAspect) ?content .
	    filter(?s in({c}))
	}}""".format(c=json.dumps(comps).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1]).replace('"', '')
	print query
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
		com[new_key] = com.pop(key)
	com["Kompetensi"] = comps

	return com
