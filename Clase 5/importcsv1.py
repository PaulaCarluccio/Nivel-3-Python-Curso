import csv
with open('oscar_age_female.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=',', quotechar='"')    
    for row in d:
        #print(type(row))
        #print(row) 
        print("Año: " + row[1])