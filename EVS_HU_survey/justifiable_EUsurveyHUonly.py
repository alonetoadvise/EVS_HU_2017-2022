import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"/Users/mbencsik/Documents/python/EVS_data_hu.csv")
data = pd.read_csv(file)

data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(5, 3, figsize=(20, 20))

fig.suptitle('Is this justifiable (Hungary by Regions)?')

sns.countplot(ax = axes[0, 0], data = data, x = 'f114a', hue = 'regions', stat = 'percent')
axes[0, 0].set_xlabel('Benefits')
sns.countplot(ax = axes[0, 1], data = data, x = 'f115', hue = 'regions', stat = 'percent')
axes[0, 1].set_xlabel('Fare dodging')
sns.countplot(ax = axes[0, 2], data = data, x = 'f116', hue = 'regions', stat = 'percent')
axes[0, 2].set_xlabel('Tax cheating')
sns.countplot(ax = axes[1, 0], data = data, x = 'f117', hue = 'regions', stat = 'percent')
axes[1, 0].set_xlabel('Bribe')
sns.countplot(ax = axes[1, 1], data = data, x = 'f118', hue = 'regions', stat = 'percent')
axes[1, 1].set_xlabel('LGBTQ')
sns.countplot(ax = axes[1, 2], data = data, x = 'f119', hue = 'regions', stat = 'percent')
axes[1, 2].set_xlabel('Prost')
sns.countplot(ax = axes[2, 0], data = data, x = 'f120', hue = 'regions', stat = 'percent')
axes[2, 0].set_xlabel('Abortion')
sns.countplot(ax = axes[2, 1], data = data, x = 'f121', hue = 'regions', stat = 'percent')
axes[2, 1].set_xlabel('Divorce')
sns.countplot(ax = axes[2, 2], data = data, x = 'f122', hue = 'regions', stat = 'percent')
axes[2, 2].set_xlabel('Euthanasia')
sns.countplot(ax = axes[3, 0], data = data, x = 'f123', hue = 'regions', stat = 'percent')
axes[3, 0].set_xlabel('Suicide')
sns.countplot(ax = axes[3, 1], data = data, x = 'f132', hue = 'regions', stat = 'percent')
axes[3, 1].set_xlabel('Casual sex')
sns.countplot(ax = axes[3, 2], data = data, x = 'e290', hue = 'regions', stat = 'percent')
axes[3, 2].set_xlabel('political violence')
sns.countplot(ax = axes[4, 0], data = data, x = 'f144_02', hue = 'regions', stat = 'percent')
axes[4, 0].set_xlabel('Death penalty')
sns.countplot(ax = axes[4, 1], data = data, x = 'g005', hue = 'regions', stat = 'percent')
axes[4, 1].set_xlabel('citizen')
sns.countplot(ax = axes[4, 2], data = data, x = 'g006', hue = 'regions', stat = 'percent')
axes[4, 2].set_xlabel('proud')

plt.show()


