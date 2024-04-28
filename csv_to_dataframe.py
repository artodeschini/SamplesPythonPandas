import pandas as pd


df1 = pd.read_csv('in/my.csv')
print(df1)

df2 = pd.read_csv('in/my.csv') #, index_col='id')
df2 = df2.set_index('id')

# caso eu queria alterar a referencia sem reatribuir uso o atributo implace com o valor True
# df2.set_index('id', inplace=True)  # df2 = df2.set_index('id')

print(df2)


df3 = pd.read_csv('in/my.csv', index_col=0) #, index_col='id')

print(df3)

df4 = pd.read_csv('in/my.csv', index_col='id') #, index_col='id')

print(df4)

df5 = pd.read_csv('in/my.csv') #, index_col='id')
# nao remove na referencia
df5.set_index('id')

print(df5)
# caso eu queria alterar a referencia sem reatribuir uso o atributo implace com o valor True
df5.set_index('id', inplace=True)  # df5 = df5.set_index('id')
print(df5)

print(df5.describe())
