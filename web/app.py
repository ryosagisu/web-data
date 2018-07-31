from flask import Flask, render_template, request, json
import os
import json
from list_functions import getJob, getDesc, getCompetencies, getBoK, getSubBoK
import simplejson

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index2.html')

@app.route('/fetchCom', methods=['POST'])
def fetchCom():

	#Get data from post ajax
	jobs = request.form.getlist('jobs[]')
	selDomList = [x for x in jobs]
	comps = getDesc(json.dumps(jobs))

	return simplejson.dumps({"Kompetensi": comps["Kompetensi"], "hasKnowledge": comps["hasKnowledge"], "hasAspect": comps["hasAspect"], "hasSkill": comps["hasSkill"], })

@app.route('/fetchJob', methods=['POST'])
def fetchJob():
	#Get data from post ajax
	level =  request.form['level']
	domain = request.form.getlist('domain[]')
	domainlevel = [ x+level for x in domain]
	jobs = getJob(json.dumps(domainlevel))

	return json.dumps({"Okupasi": jobs})

@app.route('/fetchBoK', methods=['GET'])
def fetchBoK():
	#Get data from post ajax
	BoK = getBoK()

	return json.dumps({"BoK": BoK})

@app.route('/fetchsubBoK', methods=['POST'])
def fetchsubBoK():
	#Get data from post ajax 2
	name =  request.form['name']
	subBoK = getSubBoK(name)

	return json.dumps({"subBoK": subBoK})


def application(env, start_response):
	#start_response('200 OK', [('Content-Type','text/html')])
	app.run(debug=True)
