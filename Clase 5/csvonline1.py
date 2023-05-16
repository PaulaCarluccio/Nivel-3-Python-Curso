import csv, urllib.request

url = 'http://winterolympicsmedals.com/medals.csv'
r = urllib.request.urlopen(url)
lineas = [l.decode('utf-8') for l in r.readlines()]
cr = csv.reader(lineas)
#print(type(lineas))
for row in cr:
    print(row)