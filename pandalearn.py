import pandas as pd
s = pd.Series([10,20,30,40])
print(s)

data = {'Name' : ['Shan','Siuu Annan','shanumon','shaamilshan','shottappan','Obama',None], 'Age' : [21,40,22,33,21,None,26]}
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
print(df.iloc[:,0:2])
print(df.isnull())
# print(df.dropna())
df['Age'].fillna(df['Age'].median(), inplace=True)
print(df)