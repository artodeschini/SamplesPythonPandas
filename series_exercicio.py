import pandas as pd
import numpy as np


def get_statics(notas):
    s1 = pd.Series(notas)
    return pd.Series([s1.min(), s1.max(), s1.mean()], index=['Minima', 'Maxima', 'Media'])
    # return estatisticas


# criar uma serie a partir de outra serie
notas = {'Artur': 10, 'Catia': 9, 'Manu': 8, 'Dani': 7}
print(get_statics(notas))

# criar uma serie a partir de um array do numpy
marcas = np.array(['Audi', 'Fiat', 'BMW', 'Mercedes Bem'])
indices = [1, 2, 3, 4]
s2 = pd.Series(marcas, index=indices)

# criar uma serie a partir de um dicionario
dicionario = {
    'verde': 10,
    'azul': 9,
    'preto': 8,
    'branco': 7,
    'vermelhor': 0
}

s3 = pd.Series(dicionario)
print(s3)

# criar uma serie a partir de uma lista
lista = [1, 2, 3, 4, 5, 6, 7]
s4 = pd.Series(lista, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s4)

# criar uma serie a partir da function linspace do numpy
s5 = pd.Series(np.linspace(2, 14, 6))  # de 2 a 14 com 6 valores
print(s5)

# criar uma serie a partir de numeros entre 0 e 1
s7 = pd.Series(np.random.rand(10))
print(s7)

# mostrar os elementos 1, 3 e 7 da serie s7
print(s7[[1, 3, 7]])

# mostrar os dois ultimos elementos da serie s7
print(s7.tail(2))

# mostrar os dois primeiros elementos da serie s7
print(s7.head(2))

