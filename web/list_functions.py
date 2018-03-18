from lxml import etree
from xml.etree import ElementTree as ET
import xmltodict
import json

def validate(xml_path, xsd_path):

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result
    

def validNode(domNode, tagName, value):
	nodeVal = domNode.find(tagName).text
	if isinstance(value, list):
		if nodeVal in value or nodeVal[:4] in value:
			print nodeVal, value
			return True
	else:
		if nodeVal == value:
			return True
	return False


def showNode(x, root, param):
	if root == 'KKNI':
		jenjang = x.findall('Jenjang')
		for jen in jenjang:
			if jen.find('level').text == param:
				return xmltodict.parse(ET.tostring(jen, 'us-ascii', 'xml'))
	elif root == 'SKKNI':
		listUK = x.find('FungsiKunci').find('FungsiUtama').findall('UnitKompetensi')
		listKomp = []
		for uk in listUK:
			if uk.find('kodeUnit').text in param:
				listKomp.append(xmltodict.parse(ET.tostring(uk, 'us-ascii', 'xml')))
		return listKomp
	elif root == 'PetaOkupasi':
		listK = x.findall('Kompetensi')
		listKomp = []
		for k in listK:
			listKomp.append(xmltodict.parse(ET.tostring(k, 'us-ascii', 'xml')))
		return listKomp