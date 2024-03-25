import pandas as pd
import json


def row_to_json(row):
    d = {
        'id': row['id'],
        'nome': row['nome'],
        'data': row['data'],
        'email': row['email']
    }
    return json.dumps(d)


def send(j):
    print(j)


df = pd.read_csv('in/my.csv')
# df['price'] = df.apply(lambda row: valuation_formula(row['x'], row['y']), axis=1)
df.apply(lambda row: send(row_to_json(row)), axis=1)

# # make sure indexes pair with number of rows
# df = df.reset_index()
# for index, row in df.iterrows():
#     print(type(row))
