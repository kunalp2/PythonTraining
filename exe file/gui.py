# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 22:37:15 2017

@author: kunal
"""

import pandas
import simplekml
import tkinter

from tkinter.filedialog import askopenfilename

def getUserFile():
    global filepath
    filepath=askopenfilename()

def KMLGenerator(outputFile="D:\\pythonscripts\\csvtokml.kml"):
    df = pandas.read_csv(filepath)
    kml=simplekml.Kml()
    for lat,long in zip(df["latitude"],df["longitude"]):
        kml.newpoint(coords=[(lat,long)])
    kml.save(outputFile)    

root=tkinter.Tk()
root.title("this is a test title")
label=tkinter.Label(root,text="first label")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=getUserFile)
browseButton.pack()
kmlButton=tkinter.Button(root,text="Generate KML",command=KMLGenerator)
kmlButton.pack()
root.mainloop()