import pandas as pd
from datetime import datetime


df1 = pd.read_csv('my.csv')
# print(df1)

column_names = df1.columns.values.tolist()
# print(column_names)

all_coluns_series = list();
for c in column_names:
    all_coluns_series.append(df1[c])

df2 = pd.concat(all_coluns_series, axis=0)

print(df2)
