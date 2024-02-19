import pandas as pd
from datetime import datetime


xlsx_file_name_1 = 'LeadsAnteriores.xlsx'
xlsx_file1 = pd.ExcelFile(xlsx_file_name_1)

# {sheet_name: xlsx_file1.parse(sheet_name) for sheet_name in xlsx_file1.sheet_names}
df1 = xlsx_file1.parse(xlsx_file1.sheet_names[0])
# print(df1)

xlsx_file_name_2 = 'ClientesNumeros.xlsx'
# df = pd.read_excel(xlsx_file, sheetname="Sheet1")
xlsx_file2 = pd.ExcelFile(xlsx_file_name_2)

# df2 = {sheet_name: xlsx_file2.parse(sheet_name) for sheet_name in xlsx_file2.sheet_names}
df2 = xlsx_file2.parse(xlsx_file2.sheet_names[0])
# print(df2)

cond = df1['col1'].isin(df2['col1'])
df1.drop(df1[cond].index, inplace=True)
# print(df1)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_catia_{now_as_str}.xlsx'

# saving the excel
df1.to_excel(new_file_name)
