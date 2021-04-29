# Imports data from .csv file 
''' The objective of this project is to identify one driver of user
    churn using the IBM telco database. I decided to look at what influence
    enrollment in bill auto-pay. I statistically verified significance using 
    Fishers exact test since data was binomial and the two groups were unpaired.
    '''
# import libraries for data management and analysis
from pydataset import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# load telco .csv. file must be in the same directory as this script
telco_df = pd.read_csv('telco_churn.csv')

# Clean avg charges column, will still be a string
telco_df['avg_charges'] = telco_df['avg_charges'].str.replace('$','')

# Convert data type to numeric. must use errors = 'coerce' to not return 
# an error when it encounters a null field
telco_df['avg_charges'] = pd.to_numeric(telco_df['avg_charges'], errors = 'coerce')

# Project specs ask to focus on users that pay month to month, use pandas to 
# filter for month-to-month users
month_df = telco_df[telco_df['contract_type'] == 0]

#create a boolean mask for users who are enrolled in autopay
truem_df = month_df[month_df['auto_pay']==True]
falsm_df = month_df[month_df['auto_pay']== False]

# Use masks to then select who churned in people who were and were not enrolled
fish_1 = truem_df[truem_df['has_churned']== True]
fish_2 = falsm_df[falsm_df['has_churned'] == True]
fish_3 = truem_df[truem_df['has_churned']== False]
fish_4 = falsm_df[falsm_df['has_churned'] == False]

# Conduct a fischers test on the values to determine if autopay drives churn
oddsratio, pvalue = stats.fisher_exact([[380, 753], [1276, 1467]])
    # oddsratio : .58, meaning that negative results (People not enrolled in autopay who churn, and people who are enrolled who dont churn)
    #             the likelihood of people who are enrolled in auto pay churning is 42% lower. 
    # p value is 7.748e-14, which means that there is a difference between the two sets of data

# Next step is to create figures to communicate results



