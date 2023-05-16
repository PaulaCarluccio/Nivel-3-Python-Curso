import sqlite3 as lite
con = lite.connect('test.db')
sql = "SELECT * from tproducto"
with con:
    cur = con.cursor()
    cur.execute(sql)
    datos = cur.fetchall()
    print(datos)