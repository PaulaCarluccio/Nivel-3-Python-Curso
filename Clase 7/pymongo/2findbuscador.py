import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]

def buscar(b):
    regex = f"{b}"    
    for r in coleccion.find({ "nombre": { "$regex": regex }}):
        print(r["nombre"])

b = input("Buscar: ")
buscar(b)