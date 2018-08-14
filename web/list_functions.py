import json
from SPARQLWrapper import SPARQLWrapper, JSON
from collections import Counter
import itertools

def getBoK():
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = """PREFIX acm: <http://localhost:5000/acm/> SELECT ?name WHERE {{ ?acm acm:id ?id . ?acm acm:name ?name . }}"""
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	keys = results['head']['vars']
	r = results['results']['bindings']
	bok = [x['name']['value'] for x in r]
	return bok

def getSubBoK(name):
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = "PREFIX acm: <http://localhost:5000/acm/> SELECT ?code WHERE {{ ?acm acm:name '"+name+"' . ?acm acm:hasChild ?hasChild . ?hasChild acm:code ?code . }}"
	#PREFIX acm: <http://localhost:5000/acm/> SELECT ?hasComp WHERE {{ ?acm acm:name 'Software Engineering' . ?acm acm:hasChild ?hasChild . ?hasChild acm:code 'SE/Software Project Management' . ?hasChild acm:hasComp ?hasComp }}
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	keys = results['head']['vars']
	r = results['results']['bindings']
	subbok = [x['code']['value'] for x in r]
	return subbok

def getComp1(bok, subbok):
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = "PREFIX acm: <http://localhost:5000/acm/> SELECT ?hasComp WHERE {{ ?acm acm:name '" + bok + "' . ?acm acm:hasChild ?hasChild . ?hasChild acm:code '" + subbok + "' . ?hasChild acm:hasComp ?hasComp }}"
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	keys = results['head']['vars']
	r = results['results']['bindings']
	comp = [x['hasComp']['value'] for x in r]
	return comp

def getJob(codes):
	# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
	sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
	query = """PREFIX ok: <http://localhost:5000/okupasi/> SELECT ?name WHERE {{ ?okupasi ok:id ?id ; ok:name ?name . FILTER(SUBSTR(?id, 1, 4) IN({c})) . }}""".format(c=codes[1:-1])
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
	intersection = Counter(codes) & Counter(reqs)
	reqs = list(Counter(reqs) - intersection)
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
	query = """PREFIX ok: <http://localhost:5000/okupasi/> PREFIX kom: <http://localhost:5000/kompetensi/> select ?key ?content where {{ ?s ?key ?content ; (kom:hasAspect|kom:hasContextEval|kom:hasContextVar|kom:hasKnowledge|kom:hasNS|kom:hasPRP|kom:hasSkill|kom:hasAttitude) ?content . filter(?s in({c})) }}""".format(c=json.dumps(comps).replace("http://localhost:5000/kompetensi/", "kom:")[1:-1]).replace('"', '').replace("file://C:/fakepath/", "kom:")
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

	return com
