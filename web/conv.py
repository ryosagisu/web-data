import os
import sys
import csv
import lxml.etree
import lxml.builder   

pathName = os.getcwd()

file = open("dump.csv", "rU")
reader = csv.reader(file, delimiter=',')
prev = ""

E = lxml.builder.ElementMaker()
ROOT = E.PetaOkupasi
FIELD1 = E.namaOkupasi
FIELD2 = E.Kompetensi
FIELD3 = E.kodeUnitKompetensi
FIELD4 = E.namaUnitKompetensi

the_doc = ROOT()

for row in reader:
	if prev != row[1]:
		ok = E.Okupasi(E.kodeOkupasi(row[4]), E.namaOkupasi(row[1]))
		# the_doc.append(ok)
	elif prev != "":
		the_doc.append(ok)
	uk = E.Kompetensi(E.kodeUnitKompetensi(row[2]), E.namaUnitKompetensi(row[3]))
	ok.append(uk)
	prev = row[1]
	# print prev

# k = ROOT(E.Okupasi("Page Title"), E.link(""),E.description(""))
# print lxml.etree.tostring(k, pretty_print=True)
x = lxml.etree.tostring(the_doc, pretty_print=True)

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f

print x

sys.stdout = orig_stdout
f.close()