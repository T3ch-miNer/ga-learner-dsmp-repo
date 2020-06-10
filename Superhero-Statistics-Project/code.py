# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data =pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')


# --------------
#Code starts here
alignment= data['Alignment'].value_counts()
alignment.plot(kind='bar')
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = data.Strength.cov(data.Combat).round(2)
print(sc_covariance)
sc_strength = data['Strength'].std().round(2)
sc_combat = data['Combat'].std().round(2)
sc_pearson = sc_covariance /(sc_strength*sc_combat)
ic_df = data[['Intelligence','Combat']]
ic_combat = data['Combat'].std().round(2)
ic_covariance = data.Intelligence.cov(data.Combat).round(2)
ic_intelligence = data['Intelligence'].std().round(2)
ic_pearson = ic_covariance / (ic_intelligence*sc_combat)


# --------------
#Code starts here
total_high = np.quantile(data.Total,.99)
super_best= data[data['Total'] > total_high]
super_best_names =list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3)
ax_1.boxplot(data['Intelligence'])
ax_2.boxplot(data['Speed'])
ax_3.boxplot(data['Power'])


