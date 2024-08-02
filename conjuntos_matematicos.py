import pandas as pd


a = pd.read_csv('in/a.csv', index_col='id')
# print(a)

b = pd.read_csv('in/b.csv', index_col='id')
# print(b)

print("(a ⋂ b)")
inner = pd.merge(a, b, how='inner', on='desc')
print(inner)

print("(a ⋃ b)")
union = pd.merge(a, b, how='outer', on='desc')
print(union)

# how = ‘left’ ou how= ‘right’
print("a + (a ⋂ b)")
left = pd.merge(a, b, 'left', on='desc')
print(left)

print("b + (a ⋂ b)")
right = pd.merge(a, b, 'right', on='desc')
print(right)

print("a - (a ⋂ b)")
copy_of_a = pd.read_csv('in/a.csv')
cond = copy_of_a['desc'].isin(inner['desc'])
copy_of_a.drop(copy_of_a[cond].index, inplace=True)
print(copy_of_a)


print("a - (a ⋂ b)")
copy_of_b = pd.read_csv('in/b.csv')
cond = copy_of_b['desc'].isin(inner['desc'])
copy_of_b.drop(copy_of_b[cond].index, inplace=True)
print(copy_of_b)

