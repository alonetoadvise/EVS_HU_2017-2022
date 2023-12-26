import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"/Users/mbencsik/Documents/python/EVS_data_hu.csv")
data = pd.read_csv(file)

data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(2, 3, figsize=(15, 8))

fig.suptitle('Who do you trust(Hungary by Regions)?')

sns.countplot(ax = axes[0, 0], data = data, x = 'd001_b', hue = 'regions', stat = 'percent')
axes[0, 0].set_xlabel('Family')
sns.countplot(ax = axes[0, 1], data = data, x = 'g007_18_b', hue = 'regions', stat = 'percent')
axes[0, 1].set_xlabel('Neighbour')
sns.countplot(ax = axes[0, 2], data = data, x = 'g007_33_b', hue = 'regions', stat = 'percent')
axes[0, 2].set_xlabel('Acquaintance')
sns.countplot(ax = axes[1, 0], data = data, x = 'g007_34_b', hue = 'regions', stat = 'percent')
axes[1, 0].set_xlabel('Meet first time')
sns.countplot(ax = axes[1, 1], data = data, x = 'g007_35_b', hue = 'regions', stat = 'percent')
axes[1, 1].set_xlabel('Religion')
sns.countplot(ax = axes[1, 2], data = data, x = 'g007_36_b', hue = 'regions', stat = 'percent')
axes[1, 2].set_xlabel('Nationallity')


plt.show()


