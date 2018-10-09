# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:40:04 2017

@author: kunal
"""
listToWrite = ["b3","b4","b5","b6"]
with open("C:\\Users\\kunal\\Documents\\Python Scripts\\exercise2.txt",'w') as file:
    for item in listToWrite:
        file.write(item)
        file.write("\n")
        
    
with open("C:\\Users\\kunal\\Documents\\Python Scripts\\exercise2.txt",'r') as samefile:
    content = samefile.read()
    print(content)