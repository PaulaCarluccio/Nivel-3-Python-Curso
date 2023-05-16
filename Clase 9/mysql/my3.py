import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")
editoriales = [["Planeta"],["Estrada"]]
try:
    with conn.cursor() as cursor:
        cursor.executemany("insert into teditorial (editorial) values (%s)", editoriales)
        #Envia los queries
        conn.commit()
finally:
    conn.close()