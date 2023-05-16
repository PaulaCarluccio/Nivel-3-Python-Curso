import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]
d = { "nombre": "Barthos"}
coleccion.delete_one(d)