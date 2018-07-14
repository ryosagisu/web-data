# from flask import Flask, Response, render_template, request, json
# import json
# from list_functions import getJob, getDesc, getAcm, getCompetencies
from sparql_connector import SparqlConnector

# # app = Flask(__name__)
# config = {}

# # @app.route('/')
# def index():
# 	return render_template('index.html')

# # @app.route('/fetchCom', methods=['POST'])
# # def fetchCom():
# # 	jobs = request.form.getlist('jobs[]')
# # 	selDomList = [x for x in jobs]
# # 	comps = getDesc(json.dumps(jobs))

# # 	return json.dumps(comps)

# # @app.route('/fetchJob', methods=['POST'])
# # def fetchJob():
# # 	level =  '0' + request.form['level']
# # 	domain = request.form.getlist('domain[]')
# # 	domainList = ['DATA MANAGEMENT SYSTEM',	'PROGRAMMING AND SOFTWARE DEVELOPMENT',	'HARDWARE AND DIGITAL PERIPHERALS',	'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
# # 	selDomList = [str(str(domainList.index(x) + 1).zfill(2) + level) for x in domain]

# # 	print json.dumps(selDomList)[1:-1]

# # 	jobs = getJob(json.dumps(selDomList))

# # 	return json.dumps({"Okupasi": jobs})

# # @app.route('/fetchAcm', methods=['POST'])
# # def fetchAcm():
# # 	acmId = request.form['acmId']
	
# # 	return json.dumps(getAcm(acmId))

# def app(env, start_response):
# 	web = FlaskAppWrapper('wrap')
# 	config =  get_config()
# 	sparql = SparqlConnector(config['sparql'])
# 	#start_response('200 OK', [('Content-Type','text/html')])
# 	web.add_endpoint(endpoint='/', endpoint_name='home', handler=index)
# 	web.run(debug=True)
# 	return 



# # def action():
#     # Execute anything

# # a = FlaskAppWrapper('wrap')
# # a.add_endpoint(endpoint='/ad', endpoint_name='ad', handler=fetchAcm)
# # a.run()


import tornado.web
import os
import json

from sparql_connector import SparqlConnector
from tornado import httpclient
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler
from tornado import gen
# from list_functions import get_occupation

class MainHandler(RequestHandler):
	def initialize(self):
		# TODO: move this variable to database
		self.grade_list = ["SMP", "SMA", "Diploma I", "Diploma II", "Diploma III", "Strata-1", "Strata-2", "Strata-3", "Profesor"]
		self.domain_list = ['DATA MANAGEMENT SYSTEM', 'PROGRAMMING AND SOFTWARE DEVELOPMENT', 'HARDWARE AND DIGITAL PERIPHERALS', 'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
		self.acm_list = {"ITE-CSP": "Cybersecurity Principles", "ITE-GPP": "Global Professional Practice", "ITE-IMA": "Information Management", "ITE-IST": "Integrated Systems Technology", "ITE-NET": "Networking", "ITE-PFT": "Platform Technologies", "ITE-SPA": "System Paradigms", "ITE-SWF": "Software Fundamentals", "ITE-UXD": "User Experience Design", "ITE-WMS": "Web and Mobile Systems", "ITS-ANE": "Applied Networks", "ITS-CCO": "Cloud Computing", "ITS-CEC": "Cybersecurity Emerging Challenges", "ITS-DSA": "Data Scalability and Analytics", "ITS-IOT": "Internet of Things", "ITS-MAP": "Mobile Application", "ITS-SDM": "Software Development and Management", "ITS-SRE": "Social Responsibility", "ITS-VSS": "Virtual Systems and Services"}

	def get(self):
		print self.acm_list
		self.render("index.html", grade=self.grade_list, domain=self.domain_list, acm=self.acm_list)

class AjaxHandler(RequestHandler):
	def initialize(self):
		global sparql_connector
		self.sparql_connector = sparql_connector
		self.ok = "http://localhost:5000/okupasi/"
		self.kom = "http://localhost:5000/kompetensi/"
		self.acm = "http://localhost:5000/acm/"
		self.query_head = """
		PREFIX ok: <{ok}>
		PREFIX kom: <{kom}>
		PREFIX acm: <{acm}>""".format(ok=self.ok, kom=self.kom, acm=self.acm)

	"""Simple, ajax handler"""
	def get(self, *args, **kwargs):
		"""get unlikely to be used for ajax"""
		self.write("Not allowed")
		self.finish()

	@gen.coroutine
	def post(self, *args):
		"""Example handle ajax post"""

		msg = tornado.escape.json_decode(self.request.body)
		res = {}

		if msg['req'] == "occupation":
			res = self.fetch_occupation(msg)
		elif msg['req'] == "competency":
			res = self.fetch_competency(msg)
		elif msg['req'] == "compare":
			res = self.fetch_acm(msg)


		self.write({'data': res})
		self.finish()


	def __add_competencies(self, com_id, com):
		self.active_competencies = {}
		for i in range(len(com_id)):
			self.active_competencies[com_id[i].rsplit('/')[-1]] = com[i]
		# print json.dumps(self.active_competencies, indent=2)

	def fetch_occupation(self, msg):
		codes = []
		for dom in msg['domain']:
			codes.append(dom + msg['level'])

		query = """
			{head}
			construct {{
			  ?s ?p ?o .
			}}
			FROM ok:
			WHERE
			{{
			  ?s ok:id ?id .
			  FILTER(SUBSTR(?id, 1, 4) IN ({c})) .

			  ?s ?p ?o .
			}}""".format(head=self.query_head, c=json.dumps(codes)[1:-1])

		msg = {}
		for item in self.sparql_connector.execute_query(query):
			msg = item
		return msg

	def fetch_competency(self, msg):
		codes = []
		for c in msg['occupation']:
			codes.append("ok:" + c)

		query = """
			{head}
			SELECT DISTINCT ?com 
			WHERE {{
			  ?s ok:hasCompetencies ?com .
			  FILTER(?s in({c})) .
			}}""".format(head=self.query_head, c=json.dumps(codes)[1:-1].replace('"', ''))

		temp = {}
		for item in self.sparql_connector.execute_query(query):
			temp = item

		comps = set()
		for x in temp['results']['bindings']:
			comps.add("kom:" + x['com']['value'].rsplit('/')[-1])

		loop = True
		res = []
		while True:
			# TODO: get kom:hasElement values
			query = """
				{head}
				CONSTRUCT {{
				  ?com ?x ?y .
				}}
				FROM kom:
				WHERE
				{{
				  ?com ?x ?y .
				  FILTER(?com IN({c}) && ?x != kom:hasElement)
				}}""".format(head=self.query_head, c=json.dumps(list(comps))[1:-1].replace('"', ''))

			temp = {}
			for item in self.sparql_connector.execute_query(query):
				temp = item

			comps = set()
			for x in temp:
				if self.kom + 'hasComReq' in x:
					for y in x[self.kom + 'hasComReq']:
						comps.add("kom:" + y['@id'].rsplit('/')[-1])
			res.extend(temp)

			if len(comps) == 0:
				break

		query = """
			{head}
			select ?code ?title ?entity
			where {{
				acm:{c} acm:hasDomains _:blankNode .
				_:blankNode acm:code ?code ;
					acm:title ?title;
					acm:hasEntities ?entity;   
			}}
			""".format(c=msg['acm'])

		for item in self.sparql_connector.execute_query(query):
			temp = item
		print query
		print 'here', item
		return res

	def fetch_acm(self, msg):
		codes = []
		for c in msg['occupation']:
			codes.append("ok:" + c)

		query = """
			{head}
			SELECT DISTINCT ?com 
			WHERE {{
			  ?s ok:hasCompetencies ?com .
			  FILTER(?s in({c})) .
			}}""".format(head=self.query_head, c=json.dumps(codes)[1:-1].replace('"', ''))

		temp = {}
		for item in self.sparql_connector.execute_query(query):
			temp = item

		comps = set()
		for x in temp['results']['bindings']:
			comps.add("kom:" + x['com']['value'].rsplit('/')[-1])

		loop = True
		res = []
		while True:
			query = """
				{head}
				CONSTRUCT {{
				  ?s ?p ?o .
				}}
				FROM kom:
				WHERE {{
				  {{
					SELECT ?s ?p ?o 
					WHERE {{
					  VALUES ?p {{ kom:hasKnowledge kom:hasSkill kom:hasComReq }}
					  ?s ?p ?o .
					  FILTER(?s IN({c}))
					}}
				  }}
				  UNION 
				  {{
					SELECT ?s ?p ?o 
					WHERE {{
					  ?s kom:hasElement ?bn .
					  FILTER(?s IN({c}))
					  VALUES ?p {{ kom:element }}
					  ?bn ?p ?o .
					}}
				  }}
				}}""".format(head=self.query_head, c=json.dumps(list(comps))[1:-1].replace('"', ''))

			temp = {}
			for item in self.sparql_connector.execute_query(query):
				temp = item

			comps = set()
			for x in temp:
				if self.kom + 'hasComReq' in x:
					for y in x[self.kom + 'hasComReq']:
						comps.add("kom:" + y['@id'].rsplit('/')[-1])
			res.extend(temp)

			if len(comps) == 0:
				break

		skill = set()
		knowledge = set()
		element = {}
		for k in res:
			if self.kom + 'hasSkill' in k:
				skill.update(set(self.get_value(k[self.kom + 'hasSkill'], "@value")))

			if self.kom + 'hasKnowledge' in k:
				knowledge.update(set(self.get_value(k[self.kom + 'hasKnowledge'], "@value")))
			element[k['@id']] = self.get_value(k[self.kom + 'element'], "@value")

		codes = []
		for c in msg['acm']:
			codes.append("acm:" + c)

		query = """
			{head}
			CONSTRUCT {{
			  ?s ?p ?o .
			}}
			FROM acm:
			WHERE {{
			  {{
				SELECT ?s ?p ?o 
				WHERE {{
				  ?s ?p ?o .
				  FILTER(?s IN ({c}))
				}}
			  }}
			  UNION
			  {{
				SELECT ?s ?p ?o 
				WHERE {{
				  ?x acm:hasDomains ?s .
				  FILTER(?x IN ({c}))
				  VALUES ?p {{ acm:hasEntities }}
				  ?s ?p ?o.
				}}
			  }}
			}}""".format(head=self.query_head, c=json.dumps(codes)[1:-1].replace('"', ''))

		print query
		for item in self.sparql_connector.execute_query(query):
			temp = item

		dom = {}
		ent = {}
		for k in temp:
			if self.acm + 'hasDomains' in k:
				dom[k['@id'].rsplit('/')[-1]] = {
					'name': self.get_value(k[self.acm + 'name'], "@value")[0], 
					'hasDomains': {key.rsplit('/')[-1]: [] for key in self.get_value(k[self.acm + 'hasDomains'], "@id")}  
				}

			if self.acm + 'hasEntities' in k:
				ent[k['@id'].rsplit('/')[-1]] = self.get_value(k[self.acm + 'hasEntities'], "@value")

		for k in dom.keys():
			for bn in dom[k]['hasDomains'].keys():
				dom[k]['hasDomains'][bn].extend(ent[bn])
		# 	print k, v
			# temp[k['@id'].rsplit('/')[-1]] = k
		
		# acm = {msg['acm']: temp[msg['acm']]}
		# print acm
		# for k, v in enumerate(acm[msg['acm']]['http://localhost:5000/acm/hasDomains']):
		# 	acm[msg['acm']]['http://localhost:5000/acm/hasDomains'][k] = temp[v['@id']]

		# print json.dumps({'dom': dom, 'ent': 'ent'}, indent=2)
		return {'competency': {'skill': list(skill), 'knowledge': list(knowledge), 'element': element}, 'acm': dom}

	def get_value(self, l, key):
		return [d[key] for d in l]

def application():
	settings = {
		'debug':True,
		"static_path": os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static')),
		"template_path": os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'templates')),
	}
	return tornado.web.Application([
		(r"/", MainHandler),
		(r"/(ajax)$", AjaxHandler),
	], **settings)

def init(config):
	global sparql_connector
	sparql_connector = SparqlConnector(config['sparql'])
	app = application()
	app.listen(8888)
	tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
	tornado.ioloop.IOLoop.current().start()
