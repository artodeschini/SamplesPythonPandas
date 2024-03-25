import pandas as pd

dados = {
    'alunos': ['Artur', 'Catia', 'Manu', 'Liria', 'Diego', 'Vitoria', 'Bianca'],
    'notas': [10, 9.5, 10, 9, 8, 8, 8]
}

# df1 = pd.DataFrame(dados, columns=['alunos', 'notas'])
df1 = pd.DataFrame(dados, columns=dados.keys())
print(df1)

# selecao por indice
print(df1[2:])  # mostra os dados do indice 2 em diante

# selecao por indice
print(df1[0:3])  # mostra os dados do indice 0 até 2

# por posicao linha coluna
print(df1.iloc[[1]])  # mostra toda a linha 1

# por posicao linha coluna
print(df1.iloc[[1], [0]])  # mostra toda a linha 1 coluna 0 pegano o nome da catia
print(df1.iloc[[0], [0]])  # mostra o meu nome que esta na linha 0 coluna 0 pegano o nome da catia

# por nome da coluna ou indice
print(df1.loc[[2]], ['alunos'])  # vai petar a Manu

# filtro
print(df1[df1['notas'] > 8])

# obter informacoes sobre o dataset
print(df1.shape)  # numero de linhas e colunas

# obter as colunas
print(df1.columns)

# nos da informacoes do dataframe
print(df1.info)

# nos idica se temos valores nulos
print(df1.count())

# soma de todos os valores
print(df1.sum())

# obtem o menor valor
print(df1.min())

# obtem o maior valor
print(df1.max(skipna=True))

# dessa forma posso pega max min avg etc de uma coluna especifica
print(df1['notas'].max())

# obtem a media
# print(df1.mean(skipna=True))

# obtem a media
# print(df1.median())

# resume com estatisticas basicas
print(df1.describe())

# aplicando funcoes
multiplica_por_dois = lambda x: x * 2

print(df1['notas'].apply(multiplica_por_dois))

print(df1['notas'] + 8)

dados = {'mes': ['janeiro', 'fevereiro', 'Março', 'Abril'],
         'ingressos': [21500, 17500, 25000, 34800],
         'gastos': [1700, 14800, 19200, 21500]}

df2 = pd.DataFrame(dados)
print(df2)


# exercicios com funcao
def add_beneficios(df):
    df['beneficios'] = df['ingressos'] - df['gastos']
    return df


print(add_beneficios(df2))
