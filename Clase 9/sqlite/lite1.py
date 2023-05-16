#Version basada en http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tproducto(id INT, nombre TEXT, precio INT)")
    cur.execute("INSERT INTO tproducto VALUES(1,'Teclado',2612)")
    cur.execute("INSERT INTO tproducto VALUES(2,'Mouse',577)")
    cur.execute("INSERT INTO tproducto VALUES(3,'Webcam',9500)")
    cur.execute("INSERT INTO tproducto VALUES(4,'Parlantes',2910)")    
