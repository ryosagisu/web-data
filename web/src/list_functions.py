from lxml import etree
from xml.etree import ElementTree as ET
import xmltodict
import json
import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
import pprint
from collections import Counter
import itertools

def get_occupation(codes):
	print ""

def getJob(codes):
	sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
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
	sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	query = """
	PREFIX ok: <http://localhost:5000/okupasi/>
	PREFIX kom: <http://localhost:5000/kompetensi/>

	select distinct ?reqs
	where
	{{
		?kompetensi kom:hasComReq ?reqs .
		filter(?kompetensi in({c}))
	}}
	""".format(c=json.dumps(codes).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1].replace('"', ''))
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
	sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	query = """
	PREFIX ok: <http://localhost:5000/okupasi/>
	PREFIX kom: <http://localhost:5000/kompetensi/>

	select ?competencies ?reqs
	where
	{{
		?okupasi ok:id ?id ;
			ok:name ?name ;
			ok:hasCompetencies ?competencies .
		filter(?name in({c}))
		optional{{
    		?kompetensi kom:hasComReq ?reqs .
    		filter(?kompetensi in(?competencies))
  		}}
	}}
	""".format(c=codes[1:-1])
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

	query = """
	PREFIX ok: <http://localhost:5000/okupasi/>
	PREFIX kom: <http://localhost:5000/kompetensi/>
	select ?ID ?key ?content
	where {{
	  ?ID ?key ?content ;
	    (kom:title|kom:description|kom:hasAspect|kom:hasContextEval|kom:hasContextVar|kom:hasKnowledge|kom:hasNS|kom:hasPRP|kom:hasSkill|kom:hasAttitude) ?content .
	    filter(?ID in({c}))
	}}""".format(c=json.dumps(comps).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1]).replace('"', '')

	print query
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	bind = results['results']['bindings']
	com = {}
	for x in bind:
		ID = x['ID']['value'].rsplit('/', 1)[-1]
		if ID not in com:
			com[ID] = {}

		key = x['key']['value'].rsplit('/', 1)[-1]

		if key not in com[ID]:
			com[ID][key] = []

		com[ID][key].append(x["content"]["value"])

	# for key in com:
	# 	new_key = key.rsplit('/', 1)[-1]
	# 	com[new_key] = list(set(com.pop(key)))
	# com["Kompetensi"] = comps
	pprint.pprint(com)

	return com

def getAcm(codes):
	sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	query = """
	PREFIX acm: <http://localhost:5000/acm/>
	select ?code ?title ?entity
	where {{
		acm:{c} acm:hasDomains _:blankNode .
		_:blankNode acm:code ?code ;
			acm:title ?title;
			acm:hasEntities ?entity;   
	}}
	""".format(c=codes)

	print query
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	acm = {}
	for x in results['results']['bindings']:
		ID = x['code']['value']
		if ID not in acm:
			acm[ID] = {}
			acm[ID]["title"] = x['title']['value']
			acm[ID]["entity"] = []
		acm[ID]["entity"].append(x['entity']['value'])
	return acm

