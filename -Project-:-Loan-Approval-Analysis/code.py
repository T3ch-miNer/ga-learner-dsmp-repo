# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
# code starts here
bank = pd.read_csv(path)
categorical_var  =bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks = bank.drop(columns = 'Loan_ID' ) 
banks.isnull().sum()
bank_mode= banks.mode().iloc[0]
banks.fillna(bank_mode, inplace = True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here





avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)

print(avg_loan_amount)
# code ends here



# --------------
# code starts here





loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100
# code ends here


# --------------
# code starts here
def con(num):
    return num/12 

loan_term = abs(banks['Loan_Amount_Term'].apply(lambda x : con(x)))

big_loan_term = (loan_term[loan_term >= 25]).count()
#banks['loan_term']

# code ends herevf


# --------------
# code starts here
import numpy as np
loan_groupby = banks.groupby('Loan_Status')
#loan_groupby = banks[['ApplicantIncome', 'Credit_History']]
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.agg([np.mean])
#loan_groupby.head()
print(mean_values)

# code ends here
#loan_groupby.mean()


