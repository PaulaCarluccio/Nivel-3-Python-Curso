import json
persona = '{"nombre":"Dami","dev":["Python","JavaScript","PHP"]}'
p = json.loads(persona)
print(p['nombre'])
print(p['dev'][1])