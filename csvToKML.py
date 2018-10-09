# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:37:15 2017

@author: kunal
"""

import pandas
import simplekml

df = pandas.read_csv("D:\\pythonscripts\\latlong.csv")
kml=simplekml.Kml()
for lat,long in zip(df["latitude"],df["longitude"]):
    kml.newpoint(coords=[(lat,long)])
kml.save("D:\\pythonscripts\\csvtokml.kml")    