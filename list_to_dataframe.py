import pandas as pd
import numpy as np


my_list = [['Apple', 'Red'], ['Banana', 'Yellow'], ['Orange', 'Orange']]
df = pd.DataFrame(my_list)
print(df)  # mostra o df com 0, 1 coluns e 0, 1, 2 rows

print()

df = pd.DataFrame(my_list, columns=['Fruit', 'Color'])
print(df)  # mostra o df com as colunas Fruit e Color e 0, 1, 2 rows

print()

numpy_2d = np.array([[0, 1], [2, 3], [4, 5]])
df = pd.DataFrame(numpy_2d, columns=['Odd', 'Even'])
print(df)
