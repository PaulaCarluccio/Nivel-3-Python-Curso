#By Lean
import csv,re
with open('oscar_age_female.csv', newline='') as csvfile:
    d = csv.reader(csvfile, delimiter=',', quotechar='"')
    print("Ganadoras Siglo XXI")
    for row in d:
        try:
            if int(row[1]) >= 2000:
                print(row)
        except:
            continue