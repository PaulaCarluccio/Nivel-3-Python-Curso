import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")
per = [["Hulk","Bruce Baner",45,2],["Wonder Woman","Diana Prince",95,1]]
try:
    with conn.cursor() as cursor:
        cursor.executemany("insert into tpersonajes (nombre,atler,edad,ideditorial) values (%s,%s,%s,%s)", per)
        #Envia los queries
        conn.commit()
finally:
    conn.close()