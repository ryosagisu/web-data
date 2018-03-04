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
	if isinstance(value, list):
		if domNode.find(tagName).text in value:
			return True
	else:
		if domNode.find(tagName).text == value:
			return True


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