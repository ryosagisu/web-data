import json
import itertools
import math
#Lib exclude (Mus be installed)
from SPARQLWrapper import SPARQLWrapper, JSON
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pprint

stop_words = set(stopwords.words('english'))
ps = PorterStemmer()
separators = [".", ",", ":", ";", "-", "#", "(", ")"]
subBok = ["AL/Basic Analysis", "AL/Algorithmic Strategies", "AL/Fundamental Data Structures and Algorithms", "AL/Basic Automata, Computability and Complexity", "AL/Advanced Computational Complexity", "AL/Advanced Automata Theory and Computability", "AL/Advanced Data Structures, Algorithms, and Analysis", "AR/Digital Logic and Digital Systems", "AR/Machine Level Representation of Data", "AR/Assembly Level Machine Organization", "AR/Memory System Organization and Architecture", "AR/Interfacing and Communication", "AR/Functional Organization", "AR/Multiprocessing and Alternative Architectures", "AR/Performance Enhancements", "CN/Introduction to Modeling and Simulation", "CN/Modeling and Simulation", "CN/Processing", "CN/Interactive Visualization", "CN/Data, Information, and Knowledge", "CN/Numerical Analysis", "DS/Sets, Relations, and Functions", "DS/Basic Logic", "DS/Proof Techniques", "DS/Basics of Counting", "DS/Graphs and Trees", "DS/Discrete Probability", "GV/Fundamental Concepts", "GV/Basic Rendering", "GV/Geometric Modeling", "GV/Advanced Rendering", "GV/Computer Animation", "GV/Visualization", "HCI/Foundations", "HCI/Designing Interaction", "HCI/Programming Interactive Systems", "HCI/User-Centered Design & Testing", "HCI/New Interactive Technologies", "HCI/Collaboration & Communication", "HCI/Statistical Methods for HCI", "HCI/Human Factors & Security", "HCI/Design-Oriented HCI", "HCI/Mixed, Augmented and Virtual Reality", "IAS/Foundational Concepts in Security", "IAS/Principles of Secure Design", "IAS/Defensive Programming", "IAS/Threats and Attacks", "IAS/Network Security", "IAS/Cryptography", "IAS/Web Security", "IAS/Platform Security", "IAS/Security Policy and Governance", "IAS/Digital Forensics", "IAS/Secure Software Engineering", "IM/Information Management Concepts", "IM/Database Systems", "IM/Data Modeling", "IM/Indexing", "IM/Relational Databases", "IM/Query Languages", "IM/Transaction Processing", "IM/Distributed Databases", "IM/Physical Database Design", "IM/Data Mining", "IM/Information Storage And Retrieval", "IM/MultiMedia Systems", "IS/Fundamental Issues", "IS/Basic Search Strategies", "IS/Basic Knowledge Representation and Reasoning", "IS/Basic Machine Learning", "IS/Advanced Search", "IS/Advanced Representation and Reasoning", "IS/Reasoning Under Uncertainty", "IS/Agents", "IS/Natural Language Processing", "IS/Advanced Machine Learning", "IS/Robotics", "IS/Perception and Computer Vision", "NC/Introduction", "NC/Networked Applications", "NC/Reliable Data Delivery", "NC/Routing And Forwarding", "NC/Local Area Networks", "NC/Resource Allocation", "NC/Mobility", "NC/Social Networking", "OS/Overview of Operating Systems", "OS/Operating System Principles", "OS/Concurrency", "OS/Scheduling and Dispatch", "OS/Memory Management", "OS/Security and Protection", "OS/Virtual Machines", "OS/Device Management", "OS/File Systems", "OS/Real Time and Embedded Systems", "OS/Fault Tolerance", "OS/System Performance Evaluation", "PBD/Introduction", "PBD/Web Platforms", "PBD/Mobile Platforms", "PBD/Industrial Platforms", "PBD/Game Platforms", "PD/Parallelism Fundamentals", "PD/Parallel Decomposition", "PD/Communication and Coordination", "PD/Parallel Algorithms, Analysis, and Programming", "PD/Parallel Architecture", "PD/Parallel Performance", "PD/Distributed Systems", "PD/Cloud Computing", "PD/Formal Models and Semantics", "PL/Object-Oriented Programming", "PL/Functional Programming", "PL/Event-Driven and Reactive Programming", "PL/Basic Type Systems", "PL/Program Representation", "PL/Language Translation and Execution", "PL/Syntax Analysis", "PL/Compiler Semantic Analysis", "PL/Code Generation", "PL/Runtime Systems", "PL/Static Analysis", "PL/Advanced Programming Constructs", "PL/Concurrency and Parallelism", "PL/Type Systems", "PL/Formal Semantics", "PL/Language Pragmatics", "PL/Logic Programming", "SDF/Algorithms and Design", "SDF/Fundamental Programming Concepts", "SDF/Fundamental Data Structures", "SDF/Development Methods", "SE/Software Processes", "SE/Software Project Management", "SE/Tools and Environments", "SE/Requirements Engineering", "SE/Software Design", "SE/Software Construction", "SE/Software Verification and Validation", "SE/Software Evolution", "SE/Software Reliability", "SE/Formal Methods", "SF/Computational Paradigms", "SF/Cross-Layer Communications", "SF/State and State Machines", "SF/Parallelism", "SF/Evaluation", "SF/Resource Allocation and Scheduling", "SF/Proximity", "SF/Virtualization and Isolation", "SF/Reliability through Redundancy", "SF/Quantitative Evaluation", "SP/Social Context", "SP/Analytical Tools", "SP/Professional Ethics", "SP/Intellectual Property", "SP/Privacy and Civil Liberties", "SP/Professional Communication", "SP/Sustainability", "SP/History", "SP/Economies of Computing", "SP/Security Policies, Laws and Computer Crimes"]
openAcmFile  = open("../raw_topic_acm.txt")
acmFile = openAcmFile.read()

def getsubBokandComp(description):
	#Preparation
	resSub = []
	resComp = []

	#Process
	doc_parsed = acmFile.split("|")
	D = len(doc_parsed)
	arrDesc = json.loads(description)
	for desc in arrDesc:
		tf = {}
		df  = {}
		idf = {}
		weigth = {}
		highest = 0
		res = ""
		words = []
		words = [str(ps.stem(x.lower())) for x in word_tokenize(desc) if is_ascii(desc)]
		for word in words:
			i = 0
			df[word] = 0
			for d in doc_parsed:
				all_words  = [str(ps.stem(w.lower())) for w in word_tokenize(d) if w not in stop_words and w not in separators]
				if word in all_words:
					tf[word+"-"+str(i)] = all_words.count(word)
					df[word] += 1
				else:
					tf[word+"-"+str(i)] = 0
				i+=1
			Dperdf = D/float(df[word]) if df[word] > 0 else float(0)
			idf[word] = 1 + math.log10(Dperdf) if Dperdf > 0 else float(0)
		j = 0
		for d in doc_parsed:
			weigth[j] = 0
			for word in words:
				weigth[j] += tf.get(word+"-"+str(j), float(0)) * idf[word]
			j+=1
		#Result
		highest = max(weigth, key=weigth.get)
		res = subBok[highest]
		#7|8|6|6|6|10|11|12|12|8|12|5|9|17|4|10|10|10
		if highest > 152:
			bok = "Social Issues and Professional Practice"
		elif highest > 142:
			bok = "Systems Fundamentals"
		elif highest > 132:
			bok = "Software Engineering"
		elif highest > 128:
			bok = "Software Development Fundamentals"
		elif highest > 111:
			bok = "Programming Languages"
		elif highest > 102:
			bok = "Parallel and Distributed Computing"
		elif highest > 97:
			bok = "Platform-Based Development"
		elif highest > 85:
			bok = "Operating Systems"
		elif highest > 77:
			bok = "Networking and Communication"
		elif highest > 65:
			bok = "Intelligent Systems"
		elif highest > 53:
			bok = "Information Management"
		elif highest > 42:
			bok = "Information Assurance and Security"
		elif highest > 32:
			bok = "Human-Computer Interaction"
		elif highest > 26:
			bok = "Graphics and Visualization"
		elif highest > 20:
			bok = "Discrete Structures"
		elif highest > 14:
			bok = "Computational Science"
		elif highest > 6:
			bok = "Architecture and Organization"
		else:
			bok = "Algorithms and Complexity"
		# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
		sparql = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
		query = "PREFIX acm: <http://localhost:5000/acm/> SELECT ?hasComp WHERE {{ ?acm acm:name '" + bok + "' . ?acm acm:hasChild ?hasChild . ?hasChild acm:code '" + res + "' . ?hasChild acm:hasComp ?hasComp }}"
		sparql.setQuery(query)
		sparql.setReturnFormat(JSON)
		results = sparql.query().convert()
		r = results['results']['bindings']
		comp = []
		for x in r:
			item = {}
			# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
			sparql2 = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
			query2 = "PREFIX compname: <http://localhost:5000/compname/> SELECT ?detail WHERE {{ ?compname compname:code '" + x['hasComp']['value'] + "' . ?compname compname:detail ?detail }}"
			sparql2.setQuery(query2)
			sparql2.setReturnFormat(JSON)
			results2 = sparql2.query().convert()
			r2 = results2['results']['bindings']
			item['code'] = str(x['hasComp']['value'])
			try:
				item['name'] = str(r2[0]['detail']['value'][1:])
			except IndexError:
				item['name'] = "-"
			comp.append(item)
		if res not in resSub:
			resSub.append(res)
			resComp += comp
	resRet = dict()
	resRet['subbok'] = resSub
	resRet['comp'] = resComp
	return resRet

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

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
	
	compFull = []
	for x in comps:
		item = {}
		# sparql = SPARQLWrapper("http://localhost:8080/rdf4j-server-2.3.0/repositories/sample")
		sparql2 = SPARQLWrapper("http://localhost:4000/rdf4j-http-server-2.3.0/repositories/skripsi")
		query2 = "PREFIX compname: <http://localhost:5000/compname/> SELECT ?detail WHERE {{ ?compname compname:code '" + x.replace('http://localhost:5000/kompetensi/','').replace('file://C:/fakepath/','') + "' . ?compname compname:detail ?detail }}"
		sparql2.setQuery(query2)
		sparql2.setReturnFormat(JSON)
		results2 = sparql2.query().convert()
		r2 = results2['results']['bindings']
		item['code'] = str(x.replace('http://localhost:5000/kompetensi/','').replace('file://C:/fakepath/',''))
		item['name'] = str(r2[0]['detail']['value'][1:])
		compFull.append(item)
	com["Kompetensi"] = compFull

	return com
