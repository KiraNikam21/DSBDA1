import pandas as pd
import numpy as np
df=pd.read_csv("iris.csv")
df.head()
df.species.unique()
df.groupby(df.species).count()
df.groupby(df.species).min()
df.groupby(df.species).max()
df.groupby(df.species).std()
df.groupby(df.species).median()
df.info()
df.isnull().sum()
df.value_counts("species")


import seaborn as sns
import matplotlib.pyplot as plt
 
 
sns.countplot(x='species', data=df, )
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt


sns.scatterplot(x='sepal.length', y='sepal.width',
				hue='species', data=df, )

# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()


import seaborn as sns
import matplotlib.pyplot as plt


sns.scatterplot(x='petal.length', y='petal.width',
				hue='species', data=df, )

# Placing Legend outside the Figure
plt.legend(bbox_to_anchor=(1, 1), loc=2)

plt.show()


df.corr(method='pearson')

