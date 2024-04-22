import pandas as pd


df = pd.read_csv('in/duplicados.csv')
print(df)

df = df.drop_duplicates(subset=['email'], keep='first')  # ou last
print(df)
