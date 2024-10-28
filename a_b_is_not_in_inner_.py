import pandas as pd


a = pd.read_csv('in/a.csv', index_col='id')
# print(a)

b = pd.read_csv('in/b.csv', index_col='id')
# print(b)

# print("(a ⋂ b)")
inner = pd.merge(a, b, how='inner', on='desc')
# print(inner)

# print("(a ⋃ b)")
union = pd.merge(a, b, how='outer', on='desc')
# print(union)


print("(a ⋃ b) - (a ⋂ b)")
cond = union['desc'].isin(inner['desc'])
union.drop(union[cond].index, inplace=True)
print(union)
