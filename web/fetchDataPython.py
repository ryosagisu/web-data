import os
from xml.etree import ElementTree as ET

first_data = 'kkni.xml'
second_data = 'skkni.xml'
third_data = 'peta_okupasi.xml'
full_file = os.path.abspath(second_data)


root = ET.parse(full_file)
domain = root.findall('TujuanUtama')
level = '1'
value = ['J.63OPR00.001.2', 'J.63OPR00.002.2']
hasil = []

for x in domain:
	listUK = x.find('FungsiKunci').find('FungsiUtama').findall('UnitKompetensi')
	for uk in listUK:
		if uk.find('kodeUnit').text in value:
			hasil.append(uk)
	# if dom.find('domain').text in value:
	# 	jenjang = dom.findall('Jenjang')
	# 	for jen in jenjang:
	# 		if jen.find('level').text == level:
	# 			hasil.append(jen)

for a in hasil:
	print(a)
