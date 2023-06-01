import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Students.csv') 
print(df.head())
print("  ")
print("  ")
print("  ")
print(df.tail())
print("  ")
print("  ")
print("  ")

df['Gender'].replace(['Male','Female'],[0,1],inplace=True)
print(df)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Students.csv') 
print(df.head())
bool_series=pd.isnull(df['Gender'])
df['Gender'].fillna('No Gender', inplace=True)
col=['Roll No','Insem Marks','Total Marks','Endesm Marks']
df[3:10]
df.boxplot(col)
df[bool_series]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Students.csv') 
print(df.head())
bool_series=pd.isnull(df['Gender'])
df['Gender'].fillna('No Gender', inplace=True)
df['Insem Marks'].fillna(df['Insem Marks'].median())
col=['Roll No','Insem Marks','Total Marks','Endesm Marks']
df[3:10]
outlier=np.where(df['Total Marks']>600)
#df['Total Marks'].fillna(df['Total Marks'].me
print(outlier)
df[bool_series]
print(df['Insem Marks'].median())
#df.boxplot(col)

