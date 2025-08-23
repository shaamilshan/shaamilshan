import pandas as pd
s = pd.Series([10,20,30,40])
print(s)

data = {'Name' : ['Shan','Siuu Annan','shanumon','shaamilshan','shottappan','Obama','Kudu'], 'Age' : [21,40,22,33,21,34,26]}
df = pd.DataFrame(data)
print(df)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
print(df.info())
print(df.describe())
print(df.columns)
print(df.shape)

print(df.iloc[0])
print(df.iloc[:,0:1])