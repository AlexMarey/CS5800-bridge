# -*- coding: utf-8 -*-
"""
CS5800 Project

Created on Sat Mar 25 12:33:11 2017

@author: tpwin10
"""

from tkinter import *
from tkinter import ttk

'''
Set up for the gui. can be ignored
'''
root = Tk()
root.title("Bridge Simulation")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)                      
mainframe.rowconfigure(0, weight=1)

#importing images into python
ball1Image = PhotoImage(file='ball1.png')
bridgeImage = PhotoImage(file='bridge.png')
ball2Image = PhotoImage(file='ball2.png')

#set up for each individual block
#first two are commented to explain. The rest are exactly the same

#first line creates "label" item (basically the picture holder
bridge = ttk.Label(mainframe)
#second line sets its location in the grid (col=2, row=2)
bridge.grid(column=2, row=2)
#third line sets the 'image' property to previously imported image
bridge['image'] = bridgeImage
      
channelTop1 = ttk.Label(mainframe)
#sticky=W means that the picture will go to the "West" (left) side of the label object(aka the square in the grid)
channelTop1.grid(column=2, row=1, sticky=(W))
channelTop1['image'] = ball1Image

channelTop2 = ttk.Label(mainframe)
channelTop2.grid(column=2, row=1, sticky=(E))
channelTop2['image'] = ball1Image

channelBottom2 = ttk.Label(mainframe)
channelBottom2.grid(column=2, row=3, sticky=(E))
channelBottom2['image'] = ball2Image           
           
channelBottom1 = ttk.Label(mainframe)
channelBottom1.grid(column=2, row=3, sticky=(W))
channelBottom1['image'] = ball2Image              
              
sideB1 = ttk.Label(mainframe)
sideB1.grid(column=3, row=2, sticky=(N))
sideB1['image'] = ball1Image
     
sideA1 = ttk.Label(mainframe)
sideA1.grid(column=1, row=2, sticky=(N))
sideA1['image'] = ball2Image
      
sideB2 = ttk.Label(mainframe)
sideB2.grid(column=3, row=2, sticky=(S))
sideB2['image'] = ball1Image
     
sideA2 = ttk.Label(mainframe)
sideA2.grid(column=1, row=2, sticky=(S))
sideA2['image'] = ball2Image   
     
      

#creates the slider that is not used yet
#note that the .grid at the end places it onto the GUI
s = ttk.Scale(mainframe, orient=HORIZONTAL, length=200, from_=1.0, to=100.0).grid(column=2,row=4)



#makes padding between each element. Can be ignored
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#repeats the program waiting for user input. can be ignored. put new code BEFORE this
root.mainloop()
