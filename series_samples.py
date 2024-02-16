import pandas as pd

s1 = pd.Series([2, 5, 8, 9, 2.3, 12], index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(s1)

# drop elimina o indice selecionado porém nao o altera se quiser alterar preciso
# atribuir o valor a mesma variavel
s2 = s1.drop(['a', 'd'])
print(s2)
print(s1)

# pegar o valor de um determinado indice
print(s2['b'])

# pegar mais de um valor ao mesmo tempo
print(s2[['b', 'c']])

# alterar o valor de algum indice
s2['b'] = 23
print(s2)

# filtros Obtendo valores menores que 4
print(s1[~(s1 > 4)])

# outra forma filtros Obtendo valores menores que 4
print(s1[(s1 < 4)])

# valor entre um intervalo 0 e 10
print(s1[(s1 < 0) & (s1 > 10)])

# add null ao unir as series
s3 = pd.Series([6, 7, 8, -4], index=['a', 'b', 'c', 'd'])

s4 = s1 + s3
print(s4) # colunas e e f serao NaN

# add uma serie em outra colocando valor defult caso seja nulo
s5 = s1.add(s3, fill_value=0)  # no caso aqui substitui os null por 0
print(s5)

# subtrair uma serie em outra colocando valor defult caso seja nulo
s6 = s1.sub(s3, fill_value=0)
print(s6)

# multiplicar uma serie em outra colocando valor defult caso seja nulo
s7 = s1.mul(s3, fill_value=1)
print(s7)

# multiplicar uma serie em outra colocando valor defult caso seja nulo
s8 = s1.div(s3, fill_value=1)
print(s7)
