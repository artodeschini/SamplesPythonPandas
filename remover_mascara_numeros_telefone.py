import pandas as pd
from datetime import datetime
import re


# remove todos os caracteres diferentes de numeros dos telefones
def only_numbers(s):
    return re.sub('[^0-9]+', '', s)


def remove_nono_digito_e_ciquenta_cinco_internacional(s: str):
    if s.startswith('55') and len(s) >= 13:
        return s[2:4] + s[-8::]  # pula o 55 e pega o ddd concatena com os ultimos 8 digitos
    else:
        return s


# xlsx_file_name_1 = 'LeadsAnteriores.xlsx'
# xlsx_file1 = pd.ExcelFile(xlsx_file_name_1)

# {sheet_name: xlsx_file1.parse(sheet_name) for sheet_name in xlsx_file1.sheet_names}
df1 = pd.read_csv('in/Contatos7aTodos.csv') # xlsx_file1.parse(xlsx_file1.sheet_names[0])
# print(df1)

# Converting first column i.e 'TELEFONE' to Series
# s1 = df1[df1.columns[0]]
# print(type(s1))
# print(s1.str[-8:])  # os ultimos 8 numeros

# If need replace non numeric values use to_numeric with parameter errors='coerce':
# https://stackoverflow.com/questions/42929997/how-to-replace-non-integer-values-in-a-pandas-dataframe
# df1['new'] = pd.to_numeric(df1[df1.columns[0]].astype(str)
# .apply(only_numbers).str.replace(',', ''), errors='coerce').fillna(0).astype(int)

df1['new'] = pd.to_numeric(df1[df1.columns[0]].astype(str).apply(only_numbers)
                           .apply(remove_nono_digito_e_ciquenta_cinco_internacional).fillna(0).astype(int))
print(df1)
# xlsx_file_name_2 = 'ClientesNumeros.xlsx'
# df = pd.read_excel(xlsx_file, sheetname="Sheet1")
# xlsx_file2 = pd.ExcelFile(xlsx_file_name_2)

# df2 = {sheet_name: xlsx_file2.parse(sheet_name) for sheet_name in xlsx_file2.sheet_names}
# df2 = pd.read_csv('GrupoWorkshop7a.csv') # xlsx_file2.parse(xlsx_file2.sheet_names[0])
# print(df2)

# cond = df1['TELEFONES'].isin(df2['TELEFONES'])
# df1.drop(df1[cond].index, inplace=True)
# print(df1)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_catia_{now_as_str}.csv'

# saving the excel
# df1.to_excel(new_file_name)
# df1.to_csv(new_file_name)
