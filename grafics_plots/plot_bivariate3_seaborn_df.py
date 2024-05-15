import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)

g = sns.boxplot(x=df['Survived'], y=df['Age'])
plt.title('bivarieta analise idade e sobreviventes')
plt.show()
