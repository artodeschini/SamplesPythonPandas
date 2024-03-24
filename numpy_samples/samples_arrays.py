import numpy as np


# posso criar numpy array de python list, dictionary, set e tuple
oneDArray = np.array([1, 2, 3, 4])
print(oneDArray)

# para ver q qde de dimenssoes do array
print(oneDArray.ndim)

# array de duas dimenssoes
twoDArray = np.array([[1, 2, 3], [4, 5, 6]])
print(twoDArray)
print(twoDArray.ndim)

# array from a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
dictArray = np.array(d)
print(dictArray)
print(dictArray.ndim)

# array index
print(twoDArray[0])  # ira mostrar [1,2,3]
print(twoDArray[0, 1])  # ira mosrear 1

# array shapy
print(twoDArray.shape)  # ira mosrar (2,3) linha x colunas

# interate for numpyArray
for row in twoDArray:
    print(row)
    for col in row:
        print(col)

# zeros
zeros = np.zeros(10)
print(zeros)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(type(zeros[0]))  # <class 'numpy.float64'>

zeros_as_int = np.zeros(10).astype(int)
print(zeros_as_int) # [0 0 0 0 0 0 0 0 0 0]
print(type(zeros_as_int[0]))  # <class 'numpy.int64'>

ones = np.ones(10)
print(ones)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(type(ones[0]))  # <class 'numpy.float64'>

ones_as_int = np.ones(10).astype(int)
print(ones_as_int)  # [1 1 1 1 1 1 1 1 1 1]
print(type(ones_as_int[0]))  # <class 'numpy.ndarray'>

# full
cincos = np.full(10, 5)
print(cincos)
print(type(cincos[0]))

# add scalar
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)  # mostra a matrix com os seus valores
print(matrix + 2)  # mostra a matrix com o seus valores adicionado 2
print(matrix)  # mas nao alera o array

a_list = [[1, 2, 3], [4, 5, 6]]
# print(a_list + 2) isso vai gerar um erro ao executar

# substract scalar
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)  # mostra a matrix com os seus valores
print(matrix - 2)  # mostra a matrix com o seus valores subtraindo 2
print(matrix)  # mas nao alera o array

a_list = [[1, 2, 3], [4, 5, 6]]
# print(a_list - 2) isso vai gerar um erro ao executar

# multiply scalar
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)  # mostra a matrix com os seus valores
print(matrix * 2)  # mostra a matrix com o seus valores multiplicado 2
print(matrix)  # mas nao alera o array

a_list = [[1, 2, 3], [4, 5, 6]]
print(a_list * 2)

# divide scalar
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)  # mostra a matrix com os seus valores
print(matrix / 2)  # mostra a matrix com o seus valores dividido por 2
print(matrix)  # mas nao alera o array

a_list = [[1, 2, 3], [4, 5, 6]]
# print(a_list / 2)

# numpy array to list
a_np_array = np.uint32([1, 2, 3])
print(a_np_array)  # mostra a matrix com os seus valores

nao_converte_os_elementos = list(a_np_array)
print(type(nao_converte_os_elementos))
print(type(nao_converte_os_elementos[0]))

converte_os_elementos = a_np_array.tolist()
print(type(converte_os_elementos))
print(type(converte_os_elementos[0]))

# power scalar
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)  # mostra a matrix com os seus valores
print(matrix ** 2)  # mostra a matrix com o seus valores dividido por 2
print(matrix)  # mas nao alera o array

a_list = [[1, 2, 3], [4, 5, 6]]
# print(a_list ** 2) isso dará erro ao executar

# trasporta da matrix
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz.shape)
print(matriz)

trasposta = matriz.T
print(trasposta.shape)
print(trasposta)
