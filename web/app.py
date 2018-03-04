from flask import Flask, render_template, request, json
import os
import json
from xml.etree import ElementTree as ET
from list_functions import validate, validNode, showNode

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/fetchData', methods=['POST'])
def fetchData():
	
	#Get data from post ajax
	level =  request.form['level']
	domain = request.form.getlist('domain[]')


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

		#Get data KKNI
		root = ET.parse(full_file_first)
		bidang = root.findall('Bidang')
		for node in bidang:
			if (validNode(node, 'domain', domain)):
				dataKKNI.append(showNode(node, "KKNI", level))
		for data1 in dataKKNI:
			list1 = data1['Jenjang']['UnitKompetensi']
			for data2 in list1:
				if data2['kodeUnitKompetensi'] not in listKompetensi:
					listKompetensi.append(data2['kodeUnitKompetensi'])

		#Get data SKKNI
		root2 = ET.parse(full_file_second)
		tujuanUtama = root2.findall('TujuanUtama')
		for node2 in tujuanUtama:
			# dataSKKNI.append(showNode(node2, "SKKNI", listKompetensi))
			dataSKKNI = showNode(node2, "SKKNI", listKompetensi)
		return json.dumps({'KKNI': dataKKNI, 'SKKNI': dataSKKNI})
	else:
		return json.dumps({'status':'XML not validate'})


if __name__ == '__main__':
	app.run(debug = True)