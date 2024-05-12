import pandas as pd
import numpy as np
from numpy import NaN


dados = {'Name': ['Artur', 'Manu', 'Catia', 'Bug'], 'Age': [47, 9, 43, NaN]}
df1 = pd.DataFrame.from_dict(dados)

print(df1)

print(df1.isnull().sum())

# deleting null values
df1.dropna(inplace=True)

print(df1)

df2 = pd.DataFrame.from_dict(dados)
# alterando dados em branco pela media
df2.fillna(df2.mean(numeric_only=True), inplace=True) # agora meam deve ser usado so em numericos
# or
df2.fillna(df2['Age'].mean(), inplace=True)

print(df2)

df3 = pd.DataFrame.from_dict(dados)
print(df3)
mode = df3['Age'].mode()
print(mode)

df3['Age'].fillna(df3['Age'].mode()[0], inplace=True)
print(df3)

