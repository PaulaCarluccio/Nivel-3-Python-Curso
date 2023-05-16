import pandas as pd
import pymysql
conn = pymysql.connect(host="localhost",user="root",password="",db="test1")

try:
    with conn.cursor() as cursor:
        query = "SELECT * FROM tpersonajes"
        cursor.execute(query) 
        df = pd.read_sql(query, conn)
finally:
    conn.close()

print(df)