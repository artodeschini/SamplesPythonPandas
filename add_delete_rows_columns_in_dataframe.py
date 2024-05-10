import pandas as pd


df = pd.read_csv('in/my.csv', index_col='id')
print(df)

# add new row com loc
df.loc[5] = ['Novo', '01/01/2024', 'novo@loc.add']
print(df)

# remover row com drop
df.drop(4, axis=0, inplace=True)  # axis 0 para row
print(df)

# add new column
df['new_col'] = [1, 2, 3, 4]
print(df)

# deletar uma coluna pelo seu nome
df.drop('data', axis=1, inplace=True) # axis 1 para col
print(df)
