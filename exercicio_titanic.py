import pandas as pd


# https://github.com/josecodetech/pandas

"""  
 1. generar un dataframe con los datos del fichero indicado.
 2. mostrar sus dimensiones, el numero de datos que contiene, 
  nombres de las columnas y filas, tipos de datos de las columnas y mostrar las 5 primeras filas y las 5 ultimas.
 3. mostrar los datos del pasajero con identificador 121.
 4. mostrar las filas impares del dataframe.
 5. cuantas personas sobrevivieron y murieron, indicar porcentaje.
 6. personas que estaban en segunda clase por orden alfabetico.
 7. eliminar los pasajeros que no tengan registrada su edad o sea nula.
 8. porcentaje de personas que murieron por cada clase.
 9. edad media de hombres y mujeres que viajaban en cada clase.
 10. añadir nueva columna que indique si el pasajero era menor de edad o no.
 11 mostrar el porcentaje de menores y mayores de edad que sobrevivieron.
 
"""

# 1. generar un dataframe con los datos del fichero indicado.
# abre o arquivo utilizando o id como a coluna 0
df = pd.read_csv('titanic.csv', index_col=0)
print(df)

# dimensoes linhas x colunas
print(df.shape)

# quantidade de registros
# linhax x colunas
print(df.size)

# pelo o dado pelo id
# 3. mostrar los datos del pasajero con identificador 121.
print("passagerio 121")
print(df.loc[121])

# conta a quantidade de linhas
print(df.count()[0])

# 4. mostrar las filas impares del dataframe.
# listar as colunas impares
print(df.iloc[range(0, df.shape[0], 2)])

# 5. cuantas personas sobrevivieron y murieron, indicar porcentaje.
# mostrar a quantidade de sobreviventes e obtios em percentual
survived = df['Survived'].value_counts() / df['Survived'].count() * 100


def legend(v):
    if v == 0:
        return 'Obitos'
    else:
        return 'Sobreviventes'


# print(type(survived)) vivou uma serie
sobreviventes = survived.to_frame('contagem') # transforma novamente em dataFrame
# df['salary_stats'] = df['salary'].map(salary_stats)
# adiciona uma nova coluna baseado no valor do index
sobreviventes['legenda'] = sobreviventes.index.map(legend)
# print(type(sobre))
print(sobreviventes)

# 6. personas que estaban en segunda clase por orden alfabetico.
print("Passagerios da segunda class")
segunda_classe = df[df['Pclass'] == 2]['Name'].sort_values()
print(segunda_classe)

# 7. eliminar los pasajeros que no tengan registrada su edad o sea nula.
df = df.dropna(subset=['Age'])
print(df)

# 8. porcentaje de personas que murieron por cada clase.
obitos_por_classe_serie = df.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100
print(obitos_por_classe_serie)

# obitos_por_classe = obitos_por_classe_serie.to_frame()
# obitos_por_classe['legenda'] = obitos_por_classe['Survived'].map(legend)
# print(obitos_por_classe)


# 9. edad media de hombres y mujeres que viajaban en cada clase.
idade_por_class = df.groupby(['Pclass', 'Sex'])['Age'].mean()
print(idade_por_class)

# 10. añadir nueva columna que indique si el pasajero era menor de edad o no.
df['Menor'] = df['Age'] < 18
print(df)

# pega um dado que será menos
print(df.loc[8])

# 11 mostrar el porcentaje de menores y mayores de edad que sobrevivieron.
menores_por_classe_sobrevivem = df.groupby(['Pclass', 'Menor'])['Survived'].value_counts(normalize=True) * 100
print(menores_por_classe_sobrevivem)
