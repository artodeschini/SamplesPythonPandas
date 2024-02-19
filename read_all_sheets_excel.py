import pandas as pd
from datetime import datetime


xlsx_file_name = 'Book3.xlsx'
# le o arquivo excel
xlsx_file1 = pd.ExcelFile(xlsx_file_name)

list_of_data_frames = list()

# le uma a uma todas as sheet do arquivo excel
for i, s in enumerate(xlsx_file1.sheet_names):

    # armazena o a sheet da posicao n em df1
    df1 = xlsx_file1.parse(xlsx_file1.sheet_names[i])

    # le todos as colunas da sheet n
    column_names = df1.columns.values.tolist()
    # print(column_names)

    all_coluns_series = list()

    # agrega todas as colunas da sheet em uma so
    for c in column_names:
        all_coluns_series.append(df1[c])

    # adiciona a lista de colunas em uma so e a diciona na lista
    list_of_data_frames.append(pd.concat(all_coluns_series, axis=0))

# toda a lista gera so una agregando todos na coluna
df2 = pd.concat(list_of_data_frames)
# print(df2)
# col = "'" + df2.columns.values.tolist()[0] + "'"
# df.drop_duplicates(subset=['brand'])
df2.drop_duplicates()

# df1 = xlsx_file1.parse(xlsx_file1.sheet_names[0])
# print(xlsx_file1.sheet_names)
# print(df2)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_todas_as_planilhas_{now_as_str}.xlsx'

# saving the excel
df2.to_excel(new_file_name)
