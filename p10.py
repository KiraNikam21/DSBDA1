import numpy as np
import pandas as pd
df=pd.read_csv("iris.csv")
df.head()

column=len(list(df))
print(column)

df.info()

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline

fig, axes=plt.subplots(2,2, figsize=(16,8))

axes[0,0].set_title("Distribution of first column")
axes[0,0].hist(df["col1"]);

axes[0,1].set_title("Distribution of second column")
axes[0,1].hist(df["col2"]);

axes[1,0].set_title("Distribution of third column")
axes[1,0].hist(df["col1"]);

axes[1,1].set_title("Distribution of fourth column")
axes[1,1].hist(df["col4"]);


data_to_plot=[df["col1"],df["col2"],df["col3"],df["col4"]]

sns.set_style("whitegrid")

fig=plt.figure(1,figsize=(12,8))

ax=fig.add_subplot(111)

bp=ax.boxplot(data_to_plot);
