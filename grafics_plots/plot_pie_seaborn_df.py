import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
print(df['Survived'].value_counts())
#print(df)

legend = ['Mortos', 'Sobreviventes']
plt.pie(df["Survived"].value_counts(), labels=legend)
plt.show()

# print(df['Survived'].value_counts())
