import pandas as pd


a = pd.read_csv('in/a.csv', index_col='id')
# print(a)

b = pd.read_csv('in/b.csv', index_col='id')
# print(b)

print("(a ⋃ b)")
# union = pd.merge(a, b, how='outer', on='desc')

union = pd.concat([a, b], ignore_index=True, sort=False)
print(union)
