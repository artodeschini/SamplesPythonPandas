import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('../in/titanic.csv', index_col='PassengerId')
#print(df)

sns.countplot(x=df["Survived"])
plt.show()
