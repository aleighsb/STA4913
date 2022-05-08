# -*- coding: utf-8 -*-
"""
Final: Independent Study

Author: Amber Shannon Barbosa
"""

import pandas as pd
import numpy as np

with open('levelsfyi.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('levelsfyi.csv', encoding='utf-8', index=False)

df = df.drop(['cityid', 'rowNumber'], axis = 1)

df.head(5)
df.tail(5)
df.title.value_counts()

df = df.replace("", np.nan)

# delete rows based on condition in column
# remove non-STEM job titles from Title variable
print(df)
indexNonStem = df[(df['title'] == 'Human Resources') | (df['title'] == 'Recruiter') | (df['title'] == 'Sales') | (df['title'] == 'Marketing') | (df['title'] == 'Product Manager') | (df['title'] == 'Management Consultant')].index
df.drop(indexNonStem, inplace=True)
df.title.value_counts()

# Separate variable for state
df['state'] = df['location'].apply(lambda x: x.split(', ')[1])

# prior experience = Years of experience - years at company
df['priorXP'] = df['yearsofexperience']-df['yearsatcompany']

# parsing out otherdetails variable
# change otherdetails variable to string
df['otherdetails'] = df['otherdetails'].astype(str)
# bonus
df['bonus'] = df['otherdetails'].apply(lambda x: 1 if 'bonus' in x.lower() else 0)
df['bonus'].value_counts()
# sign on, signon, sign-on, signing
df['sign on'] = df['otherdetails'].apply(lambda x: 1 if 'sign on' in x.lower() or 'signon' in x.lower() or 'sign-on' in x.lower() or 'signing' in x.lower() else 0)
df['sign on'].value_counts()
