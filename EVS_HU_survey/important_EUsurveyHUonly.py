import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"EVS_data_hu.csv")
data = pd.read_csv(file)

data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

for column in columns:
    data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

fig.suptitle('What is important to Hungarians by Regions')

sns.countplot(ax = axes[0, 0], data = data, x = 'a001', hue = 'regions', stat = 'percent')
axes[0, 0].set_xlabel('Family')
sns.countplot(ax = axes[0, 1], data = data, x = 'a002', hue = 'regions', stat = 'percent')
axes[0, 1].set_xlabel('Friends')
sns.countplot(ax = axes[0, 2], data = data, x = 'a003', hue = 'regions', stat = 'percent')
axes[0, 2].set_xlabel('Leisure')
sns.countplot(ax = axes[1, 0], data = data, x = 'a004', hue = 'regions', stat = 'percent')
axes[1, 0].set_xlabel('Politics')
sns.countplot(ax = axes[1, 1], data = data, x = 'a005', hue = 'regions', stat = 'percent')
axes[1, 1].set_xlabel('Work')
sns.countplot(ax = axes[1, 2], data = data, x = 'a006', hue = 'regions', stat = 'percent')
axes[1, 2].set_xlabel('Religion')

plt.show()


