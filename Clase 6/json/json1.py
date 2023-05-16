import json
nombre =  '{"name":"Damián", "edad":21, "ciudad":"Buenos Aires"}'
print(type(nombre))
y = json.loads(nombre)
print(type(y))
print(y["edad"])
print(type(y["edad"]))