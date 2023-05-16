import json
persona = '{"nombre":"Dami","datos":{"ciudad":"Buenos Aires","pais":"Argentina"}}'
p = json.loads(persona)
print(p['nombre'])
print(p["datos"]["pais"])