import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)
print(df[['Fare', 'Age']].corr())

g = sns.heatmap(df[['Fare', 'Age']].corr())
plt.title('bivarieta analise heatmap')
plt.show()
