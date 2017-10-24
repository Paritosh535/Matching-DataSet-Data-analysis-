# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:45:25 2017

@author: paritosh.yadav
"""

import difflib as df
from difflib import SequenceMatcher as sm
import numpy as np
import pandas as pd

source=pd.DataFrame({
    "Orgnization":["John Doe Inc","Saint Rogers","Sally Harper Center"]
    }).set_index("Orgnization")
target=pd.DataFrame({
    "Orgnization":["St. Rogers","Sally Harper Cntr","John Doe Incorporated"]
    }).set_index("Orgnization")


mostMatchitemIndex=[]
for x in range(0,len(source)):
        pre=0
        ind=0
        for y in range(0,len(target)):
            cur=sm(None,source.iloc[x].name,target.iloc[y].name).ratio()
            if pre<cur:
                pre=cur
                ind=y
        mostMatchitemIndex.append(ind)

for x in range(len(source)):
    print('{0} MATCH WITH {1}'.format(source.iloc[x].name,target.iloc[mostMatchitemIndex[x]].name))
    