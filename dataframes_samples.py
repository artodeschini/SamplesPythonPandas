import pandas as pd
import numpy as np
from datetime import datetime

dados = {
    'alunos': ['Artur', 'Catia', 'Manu', 'Liria', 'Diego', 'Vitoria', 'Bianca'],
    'notas': [10, 9.5, 10, 9, 8, 8, 8]
}

# df1 = pd.DataFrame(dados, columns=['alunos', 'notas'])
df1 = pd.DataFrame(dados, columns=dados.keys())
print(df1)

# remover uma coluna
drop = df1.drop('notas', axis=1)  # axis 0 para linha 3 1 para coluna
# repare que na linha acima nao altero o df1 se quiser altera-lo devo atribuir df1 = df1.drop('notas', axis=1)
print(drop)

# mostrar parte do dataframe do inicio
print(df1.head(2))  # mostra os 2 primeiro registros

# mostrar parte do dataframe do fim
print(df1.tail(2))  # mostra os 2 ultimo registros

# gerar exemplos
desordenado = df1.sample(2)  # quantidade de exemplos
print(desordenado)

# ordenar dataframe pelo index
print(desordenado.sort_index())

# ordenar dataframe pela coluna de A ao Z
print(df1.sort_values(by='alunos'))

# ordenar de maneira inversa o dataframe pela coluna do Z ao A
print(df1.sort_values(['alunos'], ascending=False))

# gerar valores
print(df1.rank())

# entrada e saida ou IO

# saida escrita
now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'generate_csv_sem_index_{now_as_str}.csv'
df1.to_csv(
    new_file_name,  # nome do arquivo
    index=False,  # sem o index como coluna
    columns=['alunos', 'notas'])  # quais colunas

new_file_name = f'generate_csv_sem_excolher_colunas_{now_as_str}.csv'
# df1.to_csv(new_file_name)

# ler dados de um arquivo csv
df2 = pd.read_csv('in/my.csv')

## continua em sam

# selecao por indice
print(df1[2:])  # mostra os dados do indice 2 em diante

