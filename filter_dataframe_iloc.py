import pandas as pd


df = pd.read_csv('in/my.csv', index_col='id')
print(df)

# para filtrar com iloc defino quase as linhas quever no primeiro agumento
# no segundo quase colunas quero ver
iloc_f_1 = df.iloc[0:3, 0:3] # como um interval
print(iloc_f_1)

iloc_f_2 = df.iloc[[1, 3], 0: 3]  # defino uma a uma quase linhas quero obter
print(iloc_f_2)
