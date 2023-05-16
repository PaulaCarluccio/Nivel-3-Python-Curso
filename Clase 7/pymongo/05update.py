import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]
buscar = { "nombre": "Ulrich"}
upd = { "$set": { "edad": 52 } }
coleccion.update_one(buscar, upd)