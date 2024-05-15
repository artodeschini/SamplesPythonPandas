import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')

# g = sns.distplot(df['Age']) # está depreciado
g = sns.histplot(df["Age"], kde=True)
plt.show()
