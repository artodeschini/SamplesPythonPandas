import pandas as pd
import numpy as np


# uma forma de encontrar valores animalos
s = pd.Series([2.1, 2.3, 4.5, 2.2, 2.4])

mediana = np.median(s)
devem_ser = 2
elementos = []
for item in s:
    if abs(item - mediana) > devem_ser:
        elementos.append(item)

print(elementos)

media = np.mean(s)
desvio_padrao = np.std(s)
anomalos = []
for item in s:
    if (item < media - desvio_padrao) or (item > media + desvio_padrao):
        anomalos.append(item)

print(anomalos)
