import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"EVS_data_hu.csv")
data = pd.read_csv(file)

data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    
fig, axes = plt.subplots(1, 2, figsize=(15, 8))

fig.suptitle('Who has more right to a job (Hungary by Regions)?')

sns.countplot(ax = axes[0], data = data, x = 'c001_01', hue = 'regions', stat = 'percent')
axes[0].set_xlabel('MenvsWomen')
sns.countplot(ax = axes[1], data = data, x = 'c002_01', hue = 'regions', stat = 'percent')
axes[1].set_xlabel('LocalvsImmigrant')



plt.show()


