import urllib.request,re
url= "https://raw.githubusercontent.com/testdami555/python/master/README.md"
file = urllib.request.urlopen(url)
total = 0
word = "test"
lineascount = []
for line in file:
	linea = line.decode('utf-8')
	count = len(re.findall(word,linea, re.IGNORECASE))	
	print(linea)
	print(count)
	lineascount.append(count)

print(lineascount)
print("Total: "+ str(sum(lineascount)))