# -*- coding: utf-8 -*-
"""
Created on Sat May  7 19:57:20 2022

@author: Matt Grierson
"""

import pandas as pd
import requests

data = requests.get('https://www.levels.fyi/js/salaryData.json').json()
df = pd.DataFrame(data)

df = df.drop(['cityid', 'rowNumber'], axis = 1)
df = df.drop(['Human Resources', 'Recuriter', 'Sales', 'Marketing', 'Product Manager', 'Management Consultant'], axis = 0)

df.head(5)
df.tail(5)
df.title.value_counts()
