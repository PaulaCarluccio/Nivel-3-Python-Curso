import csv
import requests
# pip install requests si no estaba instalado
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
response = requests.get(url)        

with open('out.csv', 'w') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))