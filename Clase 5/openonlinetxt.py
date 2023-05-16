import urllib.request
url= "https://raw.githubusercontent.com/testdami555/python/master/README.md"
file = urllib.request.urlopen(url)
print(type(file))
for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)