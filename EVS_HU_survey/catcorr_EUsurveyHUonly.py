import pandas as pd 
from scipy.stats import chi2_contingency 
import matplotlib.pyplot as plt
import seaborn as sns

file = (r"/Users/mbencsik/Documents/python/EVS_data_hu.csv")
data = pd.read_csv(file)

#data['age'] = data['x003r'].replace({1:"15-24", 2:"25-34", 3:"35-44", 4:"45-54", 5:"55-64", 6:">65", -2:"NA", -1:"Not sure"})

data_num = data.select_dtypes(exclude = ["object"])

#print(data_num['x003r'].corr(data_num['x025a_01']))
graph = sns.displot(data = data_num, x = 'x003r', y = 'x025a_01')

plt.show()

#data['regions'] = data['reg_nuts2'].replace({"HU11":"BP", "HU12":"Pest", "HU21":"EDunantul", "HU22":"WDunantul", "HU23":"SDunantul", "HU31":"NHU", "HU32":"NAlfold", "HU33":"SAlfold"})
#columns = data[['a001', 'a002', 'a003', 'a004', 'a005', 'a006']]

#for column in columns:
    #data[column]=data[column].replace({1:"Very", 2:"Rather", 3:"Not very", 4:"Not", -2:"NA", -1:"Not sure"})
    


