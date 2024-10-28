import pandas as pd


a = pd.read_csv('in/a.csv', index_col='id')
# print(a)

b = pd.read_csv('in/b.csv', index_col='id')
# print(b)

print("(a ⋂ b)")
inner = pd.merge(a, b, how='inner', on='desc')
print(inner)
