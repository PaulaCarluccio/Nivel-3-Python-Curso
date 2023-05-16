import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")
a = conn.cursor()
sql = "SELECT * FROM tpersonajes order by nombre asc"
a.execute(sql)
datos = a.fetchall()
print(type(datos))
for x in datos:
  for y in x:
    print(y, end=' ')
  print(f"\n--------")