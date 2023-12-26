import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"EVS_data_hu.csv")
data = pd.read_csv(file)

data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(5, 3, figsize=(15, 8))

fig.suptitle('Do you have confidence in (Hungary by Regions)?')

sns.countplot(ax = axes[0, 0], data = data, x = 'e069_01', hue = 'regions', stat = 'percent')
axes[0, 0].set_xlabel('Church')
sns.countplot(ax = axes[0, 1], data = data, x = 'e069_02', hue = 'regions', stat = 'percent')
axes[0, 1].set_xlabel('Army')
sns.countplot(ax = axes[0, 2], data = data, x = 'e069_04', hue = 'regions', stat = 'percent')
axes[0, 2].set_xlabel('Press')
sns.countplot(ax = axes[1, 0], data = data, x = 'e069_05', hue = 'regions', stat = 'percent')
axes[1, 0].set_xlabel('Unions')
sns.countplot(ax = axes[1, 1], data = data, x = 'e069_06', hue = 'regions', stat = 'percent')
axes[1, 1].set_xlabel('Police')
sns.countplot(ax = axes[1, 2], data = data, x = 'e069_07', hue = 'regions', stat = 'percent')
axes[1, 2].set_xlabel('Parliament')
sns.countplot(ax = axes[2, 0], data = data, x = 'e069_08', hue = 'regions', stat = 'percent')
axes[2, 0].set_xlabel('Services')
sns.countplot(ax = axes[2, 1], data = data, x = 'e069_18a', hue = 'regions', stat = 'percent')
axes[2, 1].set_xlabel('Organisations')
sns.countplot(ax = axes[2, 2], data = data, x = 'e069_18', hue = 'regions', stat = 'percent')
axes[2, 2].set_xlabel('EU')
sns.countplot(ax = axes[3, 0], data = data, x = 'e069_11', hue = 'regions', stat = 'percent')
axes[3, 0].set_xlabel('Government')
sns.countplot(ax = axes[3, 1], data = data, x = 'e069_12', hue = 'regions', stat = 'percent')
axes[3, 1].set_xlabel('Parties')
sns.countplot(ax = axes[3, 2], data = data, x = 'e069_13', hue = 'regions', stat = 'percent')
axes[3, 2].set_xlabel('Companies')
sns.countplot(ax = axes[4, 0], data = data, x = 'e069_14', hue = 'regions', stat = 'percent')
axes[4, 0].set_xlabel('Environmental')
sns.countplot(ax = axes[4, 1], data = data, x = 'e069_17', hue = 'regions', stat = 'percent')
axes[4, 1].set_xlabel('Justice system')
sns.countplot(ax = axes[4, 2], data = data, x = 'e069_20', hue = 'regions', stat = 'percent')
axes[4, 2].set_xlabel('UN')

plt.show()


