import pandas as pd
import matplotlib.pyplot as plt


def get_data_hora_str(s: str) -> str:
    return s[:19]


df = pd.read_csv('../in/4063-T-1d-bad-stock-split-fixed.csv')

# print(get_data_hora_str('2023-04-14 00:00:00+09:00'))

print(df)
print(type(df['Date'][0])) # é uma str

# df1['new'] = pd.to_numeric(df1[df1.columns[0]].astype(str).apply(only_numbers)
#                           .apply(remove_nono_digito_e_ciquenta_cinco_internacional).fillna(0).astype(int))

# converte a coluna Date em <class 'pandas._libs.tslibs.timestamps.Timestamp'>
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f', errors='coerce', utc=True)\
    .fillna(pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce', utc=True))
# df['Date'] = pd.to_datetime(df[df.columns[1]].astype(str).apply(get_data_hora_str),
                           # format='%Y-%m-%d %H:%M:%S', errors='coerce')
                           # format='%Y-%m-%d %H:%M:%S', errors='coerce')
# df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce', utc=True)

print(type(df['Date'][0]))  # é uma str
print(df)

plt.figure(figsize=(15, 5))
plt.title("exemplo de plote de uma series")
plt.xlabel("Ano")
plt.xlabel("Preço")

plt.plot(df['Adj Close'])
plt.show()
