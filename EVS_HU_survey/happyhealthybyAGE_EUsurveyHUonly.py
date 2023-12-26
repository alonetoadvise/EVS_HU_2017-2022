import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"EVS_data_hu.csv")
data = pd.read_csv(file)

data['age'] = data['x003r'].replace({1:"15-24", 2:"25-34", 3:"35-44", 4:"45-54", 5:"55-64", 6:">65", -2:"NA", -1:"Not sure"})

#data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(2, 2, figsize=(15, 8))

fig.suptitle('Do you feel happy, healthy (Hungary by Age)')

sns.countplot(ax = axes[0, 0], data = data, x = 'a008', hue = 'age', stat = 'percent')
axes[0, 0].set_xlabel('Happiness')
sns.countplot(ax = axes[0, 1], data = data, x = 'a009', hue = 'age', stat = 'percent')
axes[0, 1].set_xlabel('Health')
sns.countplot(ax = axes[1, 0], data = data, x = 'a170', hue = 'age', stat = 'percent')
axes[1, 0].set_xlabel('Satisfaction')
sns.countplot(ax = axes[1, 1], data = data, x = 'a173', hue = 'age', stat = 'percent')
axes[1, 1].set_xlabel('Freedom')

#plt.show()
fig.savefig('happyhealthybyage_eusurveyhuonly.png')

