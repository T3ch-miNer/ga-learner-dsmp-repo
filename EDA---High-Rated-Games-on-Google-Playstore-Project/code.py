# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data =pd.read_csv(path)


#Code starts here
data = data[data['Rating']<=5]
plt.hist(x=data['Rating'])
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null, percent_null],axis=1 , keys=['Total','Percent'])
print(missing_data)
data = data.dropna()
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1/data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1],axis=1 , keys=['Total','Percent'])
print(missing_data_1)
print(total_null_1)
# code ends here



# --------------

#Code starts here
lol =sns.catplot(x='Category',y='Rating',data=data,kind='box',height=10)
plt.subplots_adjust(top=0.9)
lol.fig.suptitle('Rating vs Category [BoxPlot]')
lol.set_xticklabels(rotation=90)

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
#print(data['Installs'].value_counts())
'''
bad_chars = ['+', ',']   
for i in bad_chars : 
    data['Installs'] = data['Installs'].replace(i, '') '''
data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].str.replace(',','').astype(int)
le = LabelEncoder() 
data['Installs']= le.fit_transform(data['Installs']) 
lol1 =sns.regplot(x='Installs',y='Rating',data=data)
lol1.set_title('Rating vs Installs [RegPlot]')


# --------------
#Code startas here
data['Price']=data['Price'].str.replace('$','').astype(float)
lol2 =sns.regplot(x='Price',y='Rating',data=data)
lol1.set_title('Rating vs Price [RegPlot]')


#Code ends here


# --------------

#Code starts here
data1= data["Genres"].str.split(";", n = 1, expand = True)
data['Genres'] =data1.iloc[:,0]
gr_mean =data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
#print(gr_mean.describe())
gr_mean =gr_mean.sort_values(by=['Rating'])
print(gr_mean)
#Code ends here



# --------------

#Code starts here
data["Last Updated"]= pd.to_datetime(data["Last Updated"])
max_date= data['Last Updated'].max()

data['Last Updated Days']= max_date - data['Last Updated']
data['Last Updated Days']=data['Last Updated Days'].dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data).set_title("Rating vs Last Updated [RegPlot]")
#Code ends here




