import pandas as pd


df = pd.read_csv('in/my.csv', index_col='id')
print(df)

loc_f_1 = df.loc[1:3, 'nome': 'email'] # linhas entre 1 e 3
print(loc_f_1)

loc_f_2 = df.loc[[1, 3], 'nome': 'email']  # só a linha 1 e 3
print(loc_f_2)
