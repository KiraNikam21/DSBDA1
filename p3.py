import pandas as pd
df=pd.read_csv("p3.csv")
print(df)
print(df.groupby(df.group).min())
print(df.groupby(df.group).max())
print(df.groupby(df.group).mean())
print(df.groupby(df.group).median())
print(df.groupby(df.group).std())






