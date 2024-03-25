import pandas as pd
from datetime import datetime


# df = pd.read_excel('c:/apps/courses_schedule.xlsx')
df1 = pd.read_csv('in/my.csv')
# print(df1)

df2 = pd.read_csv('in/copy.csv')
# print(df2)

# df = pd.concat([df1, df2])
# print(df)
# print (pd.merge(a,b, indicator=True, how='outer')
#          .query('_merge=="left_only"')
#          .drop('_merge', axis=1))

# df = pd.merge(df1, df2, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
# print(df)

cond = df1['email'].isin(df2['email'])
df1.drop(df1[cond].index, inplace=True)

print(df1)

now = datetime.now()
now_as_str = now.strftime("%Y%m%d%H%M%S")

new_file_name = f'output/generate_novo_excel_{now_as_str}.csv'


# saving the excel
# df1.to_csv(new_file_name)
