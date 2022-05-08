# -*- coding: utf-8 -*-
"""
Final: Independent Study

author: Amber Shannon Barbosa
"""

import scraper_levelsfyi as lf
import pandas as pd
import numpy as np

path = "C:/Users/aleig/Desktop/STA4913/"

df = df.drop(['cityid', 'rowNumber'], axis = 1)
df = df.drop(['Human Resources', 'Recuriter', 'Sales', 'Marketing', 'Product Manager', 'Management Consultant'], axis = 0)
df = df.replace("", np.nan)
df['otherdetails'] = df['otherdetails'].astype(str)

# Separate variable for state
df['state'] = df['location'].apply(lambda x: x.split(', ')[1])

# prior experience = Years of experience - years at company
df['priorXP'] = df['yearsofexperience']-df['yearsatcompany']

# parsing out otherdetails variable
# bonus
df['bonus'] = df['otherdetails'].apply(lambda x: 1 if 'bonus' in x.lower() else 0)
df['bonus'].value_counts()
# sign on, signon, sign-on, signing
df['sign on'] = df['otherdetails'].apply(lambda x: 1 if 'sign on' in x.lower() or 'signon' in x.lower() or 'sign-on' in x.lower() or 'signing' in x.lower() else 0)
df['sign on'].value_counts()

