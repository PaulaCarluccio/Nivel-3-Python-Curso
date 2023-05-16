import json
import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/users/")
data = json.loads(response.content.decode(response.encoding))
df = pd.DataFrame([data])
#print(df)
print(df.loc[0])
print(df.loc[0][0]["name"])
print(df.loc[0][0])