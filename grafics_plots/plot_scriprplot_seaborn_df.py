import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)
x_axis = df.index
y_axis = df['Age']

g = sns.stripplot(x=x_axis, y=y_axis)
plt.show()
