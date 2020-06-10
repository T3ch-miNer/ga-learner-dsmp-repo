# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
#print(loan_status)
loan_status.plot.bar()



#Code starts here


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
#print(property_and_loan.size)
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
#plt.bar(x=property_and_loan['Loan_Status'],y=property_and_loan['Property_Area'],stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()
#print(property_and_loan)




# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Education Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# --------------
#Code starts here

graduate = data[data['Education'] == 'Graduate']
not_graduate = data[data['Education'] == 'Not Graduate']
graduate['LoanAmount'].plot(kind='density',label ='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label ='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
x1 =data['ApplicantIncome']
y1 =data['LoanAmount']
x2=data['CoapplicantIncome']
data['TotalIncome'] = x1 + x2
x3 = data['TotalIncome']
fig ,(ax_1,ax_2,ax_3)= plt.subplots(nrows = 3 , ncols = 1)
ax_1.scatter(x1,y1)
ax_2.scatter(x2,y1)



