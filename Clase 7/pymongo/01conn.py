import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
print(conn.list_database_names())

dblist = conn.list_database_names()
if "testdb" in dblist:
  print("La DB existe.")
  db = conn["testdb"]
  colecciones = db.list_collection_names()
  print(colecciones)
else:
    print("La DB No existe")
