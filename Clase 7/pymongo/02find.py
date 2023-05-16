import pymongo
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]
#r1 = coleccion.find_one()
#print(r1)
#print("********")
#for r in coleccion.find():
#for r in coleccion.find().sort("nombre"):
  #print(r)  
  #print(r['nombre'])

#Filtra solo los nombre que comienzan con J
#for r in coleccion.find({ "nombre": { "$regex": "^J" }}):
  #print(r)  

#devolver solo algunos campos
#for n in coleccion.find({},{ "_id": 0}):
for n in coleccion.find({ "nombre": { "$regex": "^J" }},{ "_id": 0}):
  print(n)  