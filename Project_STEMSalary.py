# -*- coding: utf-8 -*-
"""
Final: Independent Study

author: Amber Shannon Barbosa
"""

import pandas as pd

path = "C:/Users/aleig/Desktop/STA4913/"

df = pd.read_csv('DataSciSTEMSalary.csv')



# Separate variable for state
df['state'] = df['location'].apply(lambda x: x.split(','[1]))

# parsing out otherdetails variable