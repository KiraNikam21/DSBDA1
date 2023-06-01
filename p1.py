import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris.csv') 
print(df.head())
print(" \n")
print("\n")
print(df.tail())
print(" \n")
print("\n")
print(df.index)
print(df.columns)
print(df.shape)
print(df.dtypes)
print(" \n")
print("\n")
print(df.columns.value())

data={

'sepal.length':[5.1,6.3],
'sepal.width':[5.4,4.5],
'petal.length':[3.3,4.5],
'petal.width':[1.0,4.5],
'variety':['sertosa','kjnswkaefrs']

}

mf=pd.DataFrame(data)
print(" \n")
print("\n")
mf.to_csv('iris.csv', mode='a', index=False, header=False)
print(df)
print(" \n")
print("\n")
print(df.isnull().sum())
print(" \n")
print("\n")
print(df[["sepal.length"]].describe(include="all"))
print(" \n")
print("\n")




