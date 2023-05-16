import pymongo
import pandas as pd
from pymongo import MongoClient
conn = pymongo.MongoClient("mongodb://localhost:27017/")
db = conn["testdb"]
coleccion = db["testcol"]
data = pd.DataFrame(list(coleccion.find()))
print(data)
#print(data.loc[0]["nombre"])