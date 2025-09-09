from sklearn.impute import KNNImputer
import pandas as pd
data = pd.read_csv("C:\shaamilshan\MISSING_DATASET_HANDLING.csv",encoding = 'latin1')
print(data.isnull().sum())
print()

imputer = KNNImputer(n_neighbors=5)
data_imputed = pd.DataFrame(imputer.fit_transform(data.select_dtypes(include=[float,int])),
                            columns = data.select_dtypes(include=[float,int]).columns)
print(data_imputed.isnull().sum())
# data = data.drop(columns = ["ADDRESSLINE2"])
# print(data.isnull().sum())
# print()
# data = data.dropna(subset=["ORDERDATE", "PRODUCTLINE"])
# print(data.isnull().sum())

# data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median())
# data["YEAR_ID"] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
# print(data.isnull().sum())
# print()
# data["STATUS"].fillna(data["STATUS"].mode()[0], inplace=True)
# print(data.isnull().sum())
# print()
# data["PHONE"].fillna("Unknown",inplace=True)
# print(data.isnull().sum())
