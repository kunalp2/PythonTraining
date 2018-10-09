# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:35:15 2017

@author: kunal
"""

import pandas
import glob

df = pandas.read_csv("C:\\Users\\kunal\\Documents\\Python Scripts\\file1.txt")
print(df)
print(df.mean())
filelist = glob.glob("C:\\Users\\kunal\\Documents\\Python Scripts\\*.txt")
print(filelist)
for file in filelist:
        df1=pandas.read_csv(file)
        m=df1.mean()
        m=float(m)
        print(m)