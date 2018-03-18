from flask import Flask, render_template, request, json
import os
import json
import xmltodict
from xml.etree import ElementTree as ET
from list_functions import validate, validNode, showNode

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
	
	#Get dataset
	first_data = 'kkni.xml'
	second_data = 'skkni.xml'
	third_data = 'peta_okupasi.xml'
	full_file_first = os.path.abspath(first_data)
	full_file_second = os.path.abspath(second_data)
	full_file_third = os.path.abspath(third_data)

	#Get validator
	first_validator = 'kkni.xsd'
	second_validator = 'skkni.xsd'
	third_validator = 'peta_okupasi.xsd'
	full_validator_first = os.path.abspath(first_validator)
	full_validator_second = os.path.abspath(second_validator)
	full_validator_third = os.path.abspath(third_validator)

	if (validate(full_file_first, full_validator_first)
		and validate(full_file_second, full_validator_second)
		and validate(full_file_third, full_validator_third)):
		listKompetensi = []
		dataKKNI = []
		dataSKKNI = []
		dataPO = []
		dataJab = []

		po = ET.parse(full_file_third)
		okupasi = po.findall('Okupasi')
		for node in okupasi:
			if (validNode(node, 'kodeOkupasi', selDomList)):
				dataJab.append(xmltodict.parse(ET.tostring(node.find('namaOkupasi'), 'us-ascii', 'xml')))
				dataPO.append(showNode(node, "PetaOkupasi", ""))
		flatPO = [item for sub in dataPO for item in sub]
		print dataJab
		print flatPO
		for data1 in flatPO:
			if data1['Kompetensi']['kodeUnitKompetensi'] not in listKompetensi:
				listKompetensi.append(data1['Kompetensi']['kodeUnitKompetensi'])		
		#Get data SKKNI
		root2 = ET.parse(full_file_second)
		tujuanUtama = root2.findall('TujuanUtama')
		for node2 in tujuanUtama:
			# dataSKKNI.append(showNode(node2, "SKKNI", listKompetensi))
			dataSKKNI = showNode(node2, "SKKNI", listKompetensi)
		return json.dumps({'KKNI': dataKKNI, 'SKKNI': dataSKKNI, 'KodeUnitKompetensi': listKompetensi, 'Jabatan': dataJab})
	else:
		return json.dumps({'status':'XML not validate'})


if __name__ == '__main__':
	app.run(debug = True)
