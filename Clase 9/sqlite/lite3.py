# Ver documentación
import sqlite3 as lite
con = lite.connect('test.db')
"""
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tpais(idpais INT, pais TEXT)")    
    cur.execute("CREATE TABLE tciudad(idciudad INT, ciudad TEXT, idpais INT)")
    cur.execute("INSERT INTO tpais VALUES (1,'Argentina'),(2,'Uruguay')")
    cur.execute("INSERT INTO tciudad VALUES (1,'Buenos Aires',1),(2,'Montevideo',2),(3,'Rosario',1)")
"""

sql = "SELECT tciudad.ciudad,tpais.pais from tpais INNER JOIN tciudad ON tpais.idpais = tciudad.idpais order by tciudad.ciudad ASC"
with con:
    cur = con.cursor()
    cur.execute(sql)
    datos = cur.fetchall()
    print(datos)