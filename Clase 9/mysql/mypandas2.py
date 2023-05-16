import pandas as pd
import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")

try:
    with conn.cursor() as cursor:
        query = "SELECT tpersonajes.nombre,tpersonajes.edad,teditorial.editorial FROM tpersonajes INNER JOIN teditorial ON tpersonajes.ideditorial = teditorial.ideditorial"
        cursor.execute(query) 
        df = pd.read_sql(query, conn)
finally:
    conn.close()

print(df)