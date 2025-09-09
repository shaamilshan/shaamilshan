import pandas as pd
data = pd.read_csv("C:\shaamilshan\MISSING_DATASET_HANDLING.csv",encoding = 'latin1')
print(data.isnull().sum())