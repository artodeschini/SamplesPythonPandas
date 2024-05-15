import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)

g = sns.barplot(x=df['Sex'], y=df['Age'])
plt.title('bivarieta analise Sexo e Idade')
plt.show()
