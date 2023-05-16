import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["personajesdark"]
datos = [{ "nombre": "Martha", "edad": 51 },{ "nombre": "Mikel", "edad": 11 },{ "nombre": "Ulrich", "edad": 55 }]
ins = coleccion.insert_many(datos)
print(ins.inserted_ids)