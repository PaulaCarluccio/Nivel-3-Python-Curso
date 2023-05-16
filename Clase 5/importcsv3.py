import csv
import requests
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
response = requests.get(url)        
for line in response.iter_lines():
     if(line.decode('utf-8').split(',')[1]== 'NORTH AMERICA'):
        print(line.decode('utf-8').split(',')[0])