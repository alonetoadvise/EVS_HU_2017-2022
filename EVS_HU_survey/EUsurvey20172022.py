import pandas as pd

file = (r"EVS_WVS_Joint_csv_v4_0.csv")
data = pd.read_csv(file)

data_hu = data.groupby('cntry_an').get_group('HU')

data_hu.to_csv("EVS_data_hu.csv")
#print(data.isnull().sum())

#print(data["cntry_an"].value_counts())

#print(data_hu.dtypes)