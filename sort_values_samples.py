import pandas as pd


df = pd.read_csv('in/my.csv', index_col='id')
print(df)

df['in_order'] = [9, 4, 2, 7]
print(df)

crescente = df.sort_values(by='in_order')
print(crescente)

decresente = df.sort_values(by='in_order', ascending=False)
print(decresente)
