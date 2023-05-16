#version by Martin
import csv, urllib.request
anio = 1992
pais = "USA"

def ver_medallas_pais(pais, anio):
    pais_medalla = []
    url = 'http://winterolympicsmedals.com/medals.csv'
    r = urllib.request.urlopen(url)
    lineas = [l.decode('utf-8') for l in r.readlines()]
    cr = csv.reader(lineas, delimiter=',', quotechar='"')
    for row in cr:
        try:
            rowaInt = row[0]
            if int(rowaInt) == anio:
                if row[4].lower() == pais.lower():
                    pais_medalla.append("|| Año: "+row[0]+'|| País: '+row[4]+'|| Disc: '+row[2]+'|| Espec.: '+row[3]+'|| Medalla: '+row[7])
                else:
                    continue
        except:
            continue
    return pais_medalla

print("Medallas ganadas por el País: "+pais)
for x in ver_medallas_pais(pais, anio):
    print(x)