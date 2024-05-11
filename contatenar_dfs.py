import pandas as pd


df1 = pd.read_csv('in/my.csv')
df2 = pd.read_csv('in/copy.csv')

print(df1)
print(df2)

print(pd.concat([df1, df2], axis=1)) # como mais colunas

print(pd.concat([df1, df2], axis=0)) # como mais linhas
