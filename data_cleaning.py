# -*- coding: utf-8 -*-
"""
Final: Independent Study

Author: Amber Shannon Barbosa
"""

import pandas as pd
import numpy as np

# get and convert Levels FYI json data to csv
with open('levelsfyi.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('levelsfyi.csv', encoding='utf-8', index=False)

# drop variables
# otherdetails seems to have been corrupted
# cityid, rowNumber, dmaid will not be used in this analysis
df = df.drop(['cityid', 'rowNumber', 'otherdetails', 'dmaid'], axis = 1)
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
