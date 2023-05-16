#By Lean y Dami
import csv,re
with open('oscar_age_female.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=',')  
    for row in d:        
        peli = row[4].replace('"', '').strip()
        if peli[0] == 'G':
            print(peli)
        else:
            continue