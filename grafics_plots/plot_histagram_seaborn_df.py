import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)

# g = sns.distplot(df['Age']) # depreciado
sns.histplot(df["Age"], kde=True, kde_kws=dict(cut=3)) # semelhante sem warning
plt.show()
