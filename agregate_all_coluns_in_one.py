import pandas as pd
from datetime import datetime


# nome do arquivo
xlsx_file_name_1 = 'Grandao.xlsx'
xlsx_file1 = pd.ExcelFile(xlsx_file_name_1)

# {sheet_name: xlsx_file1.parse(sheet_name) for sheet_name in xlsx_file1.sheet_names}
df1 = xlsx_file1.parse(xlsx_file1.sheet_names[0]) # indice da planilha
# print(df1)

column_names = df1.columns.values.tolist()
# print(column_names)

all_coluns_series = list()
for c in column_names:
    all_coluns_series.append(df1[c])

df2 = pd.concat(all_coluns_series, axis=0)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_unir_todos_{now_as_str}.xlsx'

# saving the excel
df1.to_excel(new_file_name)
