import pandas as pd
import requests


response = requests.get("https://viacep.com.br/ws/RS/Porto%20Alegre/Domingos+Jos%C3%A9/json/")
# print(response.text)

# df = pd.json_normalize(response.text)
df = pd.read_json(response.text)
print(df)
