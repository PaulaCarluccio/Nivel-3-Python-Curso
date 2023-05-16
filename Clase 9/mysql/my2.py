import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")
cursor = conn.cursor()
insertar = "INSERT INTO tpersonajes (nombre,atler,edad,ideditorial) VALUES ('Flash','Barry Allen',28,1);"
cursor.execute(insertar)
sql = "SELECT * FROM tpersonajes order by nombre asc"
cursor.execute(sql)
datos = cursor.fetchall()
for x in datos:
  for y in x:
    print(y, end=' ')
  print(f"\n--------")