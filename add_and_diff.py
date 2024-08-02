import pandas as pd
from datetime import datetime


xlsx_file_name_1 = 'in/AlunosT04.xlsx'
xlsx_file1 = pd.ExcelFile(xlsx_file_name_1)

# {sheet_name: xlsx_file1.parse(sheet_name) for sheet_name in xlsx_file1.sheet_names}
df1 = xlsx_file1.parse(xlsx_file1.sheet_names[0])
# print(df1)

xlsx_file_name_2 = 'in/Vips_l04.xlsx'
# df = pd.read_excel(xlsx_file, sheetname="Sheet1")
xlsx_file2 = pd.ExcelFile(xlsx_file_name_2)

# df2 = {sheet_name: xlsx_file2.parse(sheet_name) for sheet_name in xlsx_file2.sheet_names}
df2 = xlsx_file2.parse(xlsx_file2.sheet_names[0])

xlsx_file_name_3 = 'in/PequisaTemCartao.xlsx'
xlsx_file3 = pd.ExcelFile(xlsx_file_name_3)

# {sheet_name: xlsx_file1.parse(sheet_name) for sheet_name in xlsx_file1.sheet_names}
df3 = xlsx_file3.parse(xlsx_file3.sheet_names[0])

# how = ‘inner’ intersecao (A ⋂ B)
# how = ‘outer’ uniaon all (A ⋃ B)
# how = ‘left’ ou how= ‘right’ tudo do lado A + (A ⋂ B)
merge = pd.merge(df1, df2, how='outer')

# print(merge)

# cond = df3['Telefone'].isin(merge['Telefone'])
# df3.drop(df3[cond].index, inplace=True)
# print(df1)
cond = merge['Telefone'].isin(df3['Telefone'])
merge.drop(merge[cond].index, inplace=True)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_catia_{now_as_str}.xlsx'

# saving the excel
# df3.to_excel(new_file_name)
merge.to_excel(new_file_name)
