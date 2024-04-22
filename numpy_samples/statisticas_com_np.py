import numpy as np

# funcao min obtem menor valor do array
matrix = np.array([[1, 2, 3], [4, 5, 6], [-2, 7, 10]])
minimo = np.min(matrix)
print(minimo)  # print -2

# funcao max obtem maior valor do array
maximo = np.max(matrix)
print(maximo)  # print 10

# function sum todos os elementos do array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
soma = np.sum(matrix)
print(soma)  # print 21

# function mean obtem a media do array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
media = np.mean(matrix)
print(media)  # print 21

# function std obtem o desvio padrao
matrix = np.array([[1, 2, 3], [4, 5, 6]])
desvio = np.std(matrix)
print(desvio)  # 1.707825127659933

# function median obtem a mediana
matrix = np.array([[1, 2, 3], [4, 5, 6]])
mediana = np.median(matrix)
print(mediana)  # 3.5

