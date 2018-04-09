from flask import Flask, render_template, request, json
import os
import json
import xmltodict
from xml.etree import ElementTree as ET
from list_functions import validate, validNode, showNode, getJob
from eulexistdb import db

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fetchData', methods=['POST'])
def fetchData():

	#Get data from post ajax
	level =  '0' + request.form['level']
	domain = request.form.getlist('domain[]')
	domainList = ['DATA MANAGEMENT SYSTEM',	'PROGRAMMING AND SOFTWARE DEVELOPMENT',	'HARDWARE AND DIGITAL PERIPHERALS',	'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
	selDomList = [str(domainList.index(x) + 1).zfill(2) + level for x in domain]

	print selDomList

	return json.dumps({"job": selDomList})

@app.route('/fetchJob', methods=['POST'])
def fetchJob():
	#Get data from post ajax
	level =  '0' + request.form['level']
	domain = request.form.getlist('domain[]')
	domainList = ['DATA MANAGEMENT SYSTEM',	'PROGRAMMING AND SOFTWARE DEVELOPMENT',	'HARDWARE AND DIGITAL PERIPHERALS',	'NETWORK AND INFRASTRUCTURE', 'OPERATION AND SYSTEM TOOLS', 'INFORMATION SYSTEM AND TECHNOLOGY DEVELOPMENT', 'IT GOVERNANCE AND MANAGEMENT', 'IT PROJECT MANAGEMENT', 'IT ENTERPRISE ARCHITECTURE', 'IT SECURITY AND COMPLIANCE', 'IT SERVICES MANAGEMENT SYSTEM', 'IT AND COMPUTING FACILITIES MANAGEMENT', 'IT MULTEMEDIA', 'IT MOBILITY AND INTERNET OF THINGS', 'INTEGRATION APPLICATION SYSTEM', 'IT CONSULTANCY AND ADVISORY']
	selDomList = [str(str(domainList.index(x) + 1).zfill(2) + level) for x in domain]

	print json.dumps(selDomList)[1:-1]

	getJob(json.dumps(selDomList))

	return json.dumps({})


if __name__ == '__main__':
	app.run(debug = True)
