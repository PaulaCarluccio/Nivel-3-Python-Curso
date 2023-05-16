import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]
datos = { "nombre": "Eva", "edad": 90 }
ins = coleccion.insert_one(datos)
print(ins.inserted_id)