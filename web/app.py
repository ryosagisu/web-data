from flask import Flask, render_template, request, json
import os
import json
import xmltodict
from xml.etree import ElementTree as ET
from list_functions import validate, validNode, showNode, getJob, getDesc, getCompetencies
import simplejson

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fetchCom', methods=['POST'])
def fetchCom():

	#Get data from post ajax
	# level =  '0' + request.form['level']
	jobs = request.form.getlist('jobs[]')
	# domainList = ['DATA MANAGEMENT SYSTEM',	'PROGRAMMING AND SOFTWARE DEVELOPMENT',	'HARDWARE AND DIGITAL PERIPHERALS',	'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
	selDomList = [x for x in jobs]
	comps = getDesc(json.dumps(jobs))

	return simplejson.dumps({"Kompetensi": comps["Kompetensi"], "hasKnowledge": comps["hasKnowledge"], "hasAspect": comps["hasAspect"], "hasSkill": comps["hasSkill"], })

@app.route('/fetchJob', methods=['POST'])
def fetchJob():
	#Get data from post ajax
	level =  '0' + request.form['level']
	domain = request.form.getlist('domain[]')
	domainList = ['DATA MANAGEMENT SYSTEM',	'PROGRAMMING AND SOFTWARE DEVELOPMENT',	'HARDWARE AND DIGITAL PERIPHERALS',	'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
	selDomList = [str(str(domainList.index(x) + 1).zfill(2) + level) for x in domain]

	print json.dumps(selDomList)[1:-1]

	jobs = getJob(json.dumps(selDomList))

	return json.dumps({"Okupasi": jobs})


def application(env, start_response):
	#start_response('200 OK', [('Content-Type','text/html')])
	app.run(debug=True)
