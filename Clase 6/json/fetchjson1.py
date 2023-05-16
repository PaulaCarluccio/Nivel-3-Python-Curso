import json
from urllib.request import urlopen
def get(url):
    with urlopen(url) as resource:
        return json.load(resource)

comentario = get('https://jsonplaceholder.typicode.com/comments/1') 
print(comentario['name'])

comentario = get('https://jsonplaceholder.typicode.com/comments/') 
print(comentario[5]['email'])