import pandas as pd


xlsx_file_name = 'generate.xlsx'
# df = pd.read_excel(xlsx_file, sheetname="Sheet1")
xlsx_file = pd.ExcelFile(xlsx_file_name)

# todas as sheets
df = {sheet_name: xlsx_file.parse(sheet_name) for sheet_name in xlsx_file.sheet_names}
# print(df)

# pega especificamente um sheet

df1 = xlsx_file.parse(xlsx_file.sheet_names[0])
print(df1)
