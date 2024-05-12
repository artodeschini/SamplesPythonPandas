from numpy import NaN
import numpy as np
import pandas as pd


data = {'Age': [47, 43, 9], 'Salary': [10000, 4500, 0]}
df = pd.DataFrame.from_dict(data)

print(df)

# normalization
df = (df - df.min()) / (df.max() - df.min())

print(df)

# standerdization
df = (df - df.mean()/ df.std()) # pd.DataFrame.from_dict(data)
print(df.std())
