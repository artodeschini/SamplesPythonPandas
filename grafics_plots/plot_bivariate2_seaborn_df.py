import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)
survived_ratio = df[['Pclass', 'Survived']].groupby('Pclass').sum()
print(survived_ratio)

g = sns.barplot(x=survived_ratio.index, y=survived_ratio['Survived'])
plt.title('bivarieta analise')
plt.show()
