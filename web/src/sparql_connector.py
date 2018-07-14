import requests
import yaml
import json

from concurrent import futures
from tornado import httpclient
from tornado.httputil import url_concat

def handle_response(response):
    if response.error:
    	print "ss"
        print("Error: %s" % response.error)
    else:
    	self.write(response.body)
    	self.write('heh')
        print response.body
        print 'heh'

class SparqlConnector:
	def __init__(self, config):
		self.endpoint = config['endpoint']
		self.port = config['port']
		self.route = config['route']
		self.repo = config['repo']
		self.executor = futures.ThreadPoolExecutor(max_workers=1)

	def execute_query(self, query):
		# refer to this http://docs.rdf4j.org/rest-api/
		headers = {'Accept': 'application/sparql-results+json,application/ld+json'}
		payload = {'query': query}
		http = httpclient.AsyncHTTPClient()
		url = "http://%s:%s/%s/repositories/%s" % (self.endpoint, self.port, self.route, self.repo)
		

		url = url_concat(url, payload)

		# print url
		req = httpclient.HTTPRequest(url, headers=headers)

		# # I have used synchronous one (you can use async one with callback)
		client = httpclient.HTTPClient()
		response = client.fetch(req)
		
		body = response.body
		# if response.headers['Content-Type'] == "application/ld+json;charset=UTF-8":
		# 	body = self.__clean_result(body)
		yield json.loads(body)
		# try:
		# 	foo = yield http.fetch(httpclient.HTTPRequest(url, headers=headers, body=payload))
		# # 	foo = yield http.fetch("{}/foo/{}".format(endpoint, id))
		# # 	bar = yield http.fetch("{}/bar/{}".format("http://www.doh.com", id))
		# except e:
		# 	raise e
		# self._response(foo)
		# r = requests.get("http://%s:%s/%s/repositories/%s" % (self.endpoint, self.port, self.route, self.repo), params=payload, headers=headers)
		# yield "haha"
		return

	def _response(self, foodict):
		self.write(json.dumps({'foo':'bar'}))
		self.finish()

	def __clean_result(self, res):
		shortened_uri = {}
		for content in res:
			for key in content:
				# get last 2 useful element from uri
				uri = key.rsplit('/')[-2:]
				prefix = ""
				if uri[0] == "kompetensi":
					prefix = "kom:" + uri[1]
				elif uri[0] == "okupasi":
					prefix = "ok:" + uri[1]
				elif uri[0] == "acm":
					prefix = "acm:" + uri[1]
				else:
					prefix = uri[0]

				if prefix not in shortened_uri:
					shortened_uri[prefix] = []

				# if isinstance(content[key], (list,)):
				# 	shortened_uri[prefix].extend(content[key])
				# else:
				# print res
				shortened_uri[prefix].append(content[key])
		return shortened_uri

# ch = SparqlExecutor()
# # ret = ch.execute_query(query)
# query = """
# PREFIX kom: <http://localhost:5000/kompetensi/>
# PREFIX ok: <http://localhost:5000/okupasi/>
# CONSTRUCT {
#    ?ID ?key ?content .
# }
# FROM kom:
# FROM ok:
# WHERE {
# ?ID ?key ?content ;
# 	    (kom:title|kom:description|kom:hasAspect|kom:hasContextEval|kom:hasContextVar|kom:hasKnowledge|kom:hasNS|kom:hasPRP|kom:hasSkill|kom:hasAttitude) ?content .
# }"""

# query = """PREFIX kom: <http://localhost:5000/kompetensi/>
# PREFIX ok: <http://localhost:5000/okupasi/>
# CONSTRUCT { 
#    ?ID ?key ?content .
# }
# FROM kom:
# FROM ok:
# WHERE {
# ?ID ?key ?content ;
# 	    (kom:title|kom:description|kom:hasAspect|kom:hasContextEval|kom:hasContextVar|kom:hasKnowledge|kom:hasNS|kom:hasPRP|kom:hasSkill|kom:hasAttitude) ?content .
# }"""

# # r = requests.get("http://%s:%s/%s/repositories/%s" % ("localhost", "8080", "rdf4j-server-2.3.0", "sample"))

# # payload = {'some': 'data'}

# # print type(json_data)
# ret = ch.execute_query(query)
# # print ret

# 	# for k in cont:

# 		# print k
# # print len(ret) 
# # ret.print_results(2)
# # ret.convert(JSONLD)
# # ret.print_results()
# # for binding in ret.contexts() :
# # 	# each binding is a dictionary. Let us just print the results
# # 	print binding
# # 	break
# 	# print "%s: %s (of type %s)" % ("p",binding[u"prop"].value,binding[u"prop"].type)
