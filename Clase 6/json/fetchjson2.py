import json
from urllib.request import urlopen
def get(url):
    with urlopen(url) as resource:
        return json.load(resource)

usuarios = get('https://jsonplaceholder.typicode.com/users/') 

for u in usuarios:
    print(f"""
        {u['name']} - {u['email']}
        Ciudad: {u['address']['city']}     
     """)