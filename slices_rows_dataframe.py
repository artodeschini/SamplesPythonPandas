import pandas as pd


df = pd.read_csv('in/my.csv', index_col=0)

print(df.head(2)) ## mostrar as duas primeiras linhas se passar
# um numero o padrao é 5

print(df.tail(2)) ## mostrar as duas ultimas linhas se passar
# um numero o padrao é 5


print(df[1:3])  # mostrara a 2 e 3 linhas
# obs o primeiro parametro no splice nao esta incluso e o segundo sim

print(df[['nome', 'data']])

## formas de pegar uma row por index

# com loc
print(df.loc[[3]])

row3 = [False, False, True, False]
print(df[row3])

row3_and_4 = [False, False, True, True]
print(df[row3_and_4])

print(df.loc[[3, 4]])
print(df.loc[[1, 4]])
