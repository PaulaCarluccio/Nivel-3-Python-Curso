import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]

#insertar un dato
def insertar(n,e): 
    datos = { "nombre": n, "edad": e }
    ins = coleccion.insert_one(datos)    

n = input("Nombre: ")
e = int(input("Edad: "))
insertar(n,e)