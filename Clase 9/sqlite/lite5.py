# Ver documentación
import sqlite3 as lite
con = lite.connect('test.db')

with con:
    cur = con.cursor()
    
    cur.execute("CREATE TABLE tprograma ( idserie INTEGER PRIMARY KEY AUTOINCREMENT, titulo text NOT NULL UNIQUE, idcanal INTEGER NOT NULL)")        
    cur.execute("CREATE TABLE tcanal ( idcanal INTEGER PRIMARY KEY AUTOINCREMENT, canal text NOT NULL UNIQUE, idpais INTEGER NOT NULL)")        
    cur.execute("CREATE TABLE tpais ( idpais INTEGER PRIMARY KEY AUTOINCREMENT, pais text NOT NULL UNIQUE)")
    
    cur.execute("INSERT INTO tpais (pais) VALUES ('USA'),('Argentina'),('Brasil')")
    cur.execute("INSERT INTO tcanal (canal,idpais) VALUES ('CBS',1),('Telefe',2),('O Globo',3)")
    cur.execute("INSERT INTO tprograma (titulo,idcanal) VALUES ('Jimmy Fallon Presenta',1),('Morfi',2),('Avenida Brasil',3)")

    sql = "SELECT tprograma.titulo,tcanal.canal,tpais.pais FROM tprograma INNER JOIN tcanal ON tprograma.idcanal = tcanal.idcanal INNER JOIN tpais ON tcanal.idpais = tpais.idpais"
with con:
    cur = con.cursor()
    cur.execute(sql)
    datos = cur.fetchall()
    print(datos)