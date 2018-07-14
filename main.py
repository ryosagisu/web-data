from bs4 import BeautifulSoup

with open('data.html', 'r') as myfile:
	data=myfile.read().replace('\n', '')



soup = BeautifulSoup(data)
# print soup.body.prettify()

f1=open('./testfile', 'w+')

for x in soup.body.find_all('div'):
	for y in x.find_all('div'):
		f1.write(y.get_text().encode('utf8') + '\n')

f1.close()