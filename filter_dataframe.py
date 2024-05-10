import pandas as pd


df = pd.read_csv('in/titanic.csv', index_col='PassengerId')

# filtrar uma condicao
print(df)
condicao = df['Age'] < 18
print(df[condicao])

# filtrar duas ou mais condicoes use & para operador logico and
menores_sobreviventes = df[(df['Survived'] == 1) & (df['Age'] < 18)]
print(menores_sobreviventes)

# filtrar duas ou mais condicoes use | para operador logico or
sobrevive = df[(df['Survived'] == 1) | (df['Embarked'] == 'S')]
print(sobrevive)

