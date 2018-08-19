from flask import Flask, render_template, request, json
import os
import json
from list_functions import getJob, getDesc, getCompetencies, getsubBokandComp
import simplejson
import pprint

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index2.html')

@app.route('/fetchCom', methods=['POST'])
def fetchCom():

	#Get data from post ajax
	jobs = request.form.getlist('jobs[]')
	comps = getDesc(json.dumps(jobs))
	arrComp = comps["Kompetensi"] if "Kompetensi" in comps else []
	arrKnowledge = comps["hasKnowledge"] if "hasKnowledge" in comps else []
	arrAspect = comps["hasAspect"] if "hasAspect" in comps else []
	arrSkill = comps["hasSkill"] if "hasSkill" in comps else []

	return simplejson.dumps({"Kompetensi": arrComp, "hasKnowledge": arrKnowledge, "hasAspect": arrAspect, "hasSkill": arrSkill })

@app.route('/fetchJob', methods=['POST'])
def fetchJob():
	#Get data from post ajax
	level =  request.form['level']
	domain = request.form.getlist('domain[]')
	domainlevel = [ x+level for x in domain]
	jobs = getJob(json.dumps(domainlevel))

	return json.dumps({"Okupasi": jobs})

@app.route('/fetchCompetencies1', methods=['POST'])
def fetchCompetencies2():
	#Get data from post ajax 3
	description =  request.form['description']
	index =  request.form['index']
	subBokandComp = getsubBokandComp(description, index)

	return json.dumps({"subbok": subBokandComp.get("subbok", ""), "comp": subBokandComp.get("comp", []), "index": subBokandComp.get("index", 0)})

def application(env, start_response):
	#start_response('200 OK', [('Content-Type','text/html')])
	app.run(debug=True)
