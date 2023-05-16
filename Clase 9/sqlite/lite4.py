# Ver documentación
import sqlite3 as lite
con = lite.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE tpersonas ( idpersona INTEGER PRIMARY KEY AUTOINCREMENT, username text NOT NULL UNIQUE, habilitado BOOLEAN DEFAULT 1);")        
    cur.execute("INSERT INTO tpersonas (username) VALUES ('dami'),('coco'),('pato')")
    

sql = "SELECT * FROM tpersonas"
with con:
    cur = con.cursor()
    cur.execute(sql)
    datos = cur.fetchall()
    print(datos)