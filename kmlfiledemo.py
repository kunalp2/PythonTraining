# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:39:24 2017

@author: kunal
"""

import simplekml

def userInputLatAndLong(lat,long):
    kml=simplekml.Kml()
    kml.newpoint(name="Sample",coords=[(lat,long)])
    kml.save("D:\\pythonscripts\\point.kml")
    
userLat=input("Please enter the desired value of latitude :")
userLong=input("Please enter the desired value of longitude : ")
userInputLatAndLong(userLat,userLong)