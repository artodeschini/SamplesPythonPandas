import pandas as pd


def carga():
    return pd.read_csv('in/titanic.csv', index_col=0)


df1 = carga()
print(df1)

# mostra valores null valores null
print(df1.isin)

# elimita os valores null
df2 = df1.dropna(axis=0, how='all')  # para linhas axis 0 para colunas axis 1
print(df2)

# eliminar todos que tenha ao menos dois faltantes
df3 = carga()
df3.dropna(axis=0, thresh=2)
print(df3)

# eliminar por coluna especifica
df4 = carga();
df4 = df4.dropna(subset=['Cabin'])
print(df4)

# substituir null por valor indicado
df5 = carga();
df5.fillna(0, inplace=True)  # altera a referencia do dataFrame
print(df5)
