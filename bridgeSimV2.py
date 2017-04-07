# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 00:30:10 2017

@author: tpwin10
"""

from tkinter import *
#from tkinter import PhotoImage
from tkinter import ttk

'''
Set up for the gui. can be ignored
'''

class BridgeSim(ttk.Frame):
   
    def __init__(self, parent=None, msecs=2000, **args):
        #creates the frame which actually holds all of the widgets
        ttk.Frame.__init__(self, parent)
        #sets up the content manager for the window
        self.grid()
        #sets class variable for the speed that can be used by any method
        self.msecs = msecs
        #importing images into python
        self.ball1Image = PhotoImage(file='ball1.png')
        self.bridgeImage = PhotoImage(file='bridge.png')
        self.ball2Image = PhotoImage(file='ball2.png')
        #puts the 
        self.makeWidgets()

        
    def makeWidgets(self):
      
        #first line creates "label" item (basically the picture holder
        #second line sets its location in the grid (col=2, row=2)
        #third line sets the 'image' property to previously imported image
  
        self.bridge = ttk.Label(self)
        self.bridge.grid(column=2, row=2)
        self.bridge['image'] = self.bridgeImage
                  
        #set up for each individual block
        #first two are commented to explain. The rest are exactly the same
        
            
        self.channelTop1 = ttk.Label(self)
        #sticky=W means that the picture will go to the "West" (left) side of the label object(aka the square in the grid)
        self.channelTop1.grid(column=2, row=1, sticky=(W))
        self.channelTop1['image'] = self.ball1Image
        
        self.channelTop2 = ttk.Label(self)
        self.channelTop2.grid(column=2, row=1, sticky=(E))
        self.channelTop2['image'] = self.ball1Image
        
        self.channelBottom2 = ttk.Label(self)
        self.channelBottom2.grid(column=2, row=3, sticky=(E))
        self.channelBottom2['image'] = self.ball2Image           
                   
        self.channelBottom1 = ttk.Label(self)
        self.channelBottom1.grid(column=2, row=3, sticky=(W))
        self.channelBottom1['image'] = self.ball2Image              
                      
        self.sideB1 = ttk.Label(self)
        self.sideB1.grid(column=3, row=2, sticky=(N))
        self.sideB1['image'] = self.ball1Image
             
        self.sideA1 = ttk.Label(self)
        self.sideA1.grid(column=1, row=2, sticky=(N))
        self.sideA1['image'] = self.ball2Image
              
        self.sideB2 = ttk.Label(self)
        self.sideB2.grid(column=3, row=2, sticky=(S))
        self.sideB2['image'] = self.ball1Image
             
        self.sideA2 = ttk.Label(self)
        self.sideA2.grid(column=1, row=2, sticky=(S))
        self.sideA2['image'] = self.ball2Image   
             
        self.onoff = Button(self, text='Start', command=self.onStart)   
        self.onoff.grid(column=2, row=5)   
        #creates the slider that is not used yet
        #note that the .grid at the end places it onto the GUI
        self.s = ttk.Scale(self, command=self.onScale,orient=HORIZONTAL, length=200, from_=0, to=3000).grid(column=2,row=4)
        
        self.order = [self.channelTop1, self.channelTop2, self.sideB1, self.sideB2, self.channelBottom2, self.channelBottom1, self.sideA2, self.sideA1]
        
        
        #makes padding between each element. Can be ignored
        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    def onStart(self):
        self.loop = 1
        self.onoff.config(text='Stop', command=self.onStop)
        self.onTimer()
    
    def onStop(self):
        self.loop = 0
        self.onoff.config(text='Start', command=self.onStart)
        
    def onTimer(self):
        if self.loop:
            self.drawNext()
            self.after(self.msecs, self.onTimer)
            
    def drawNext(self):
        lastx = self.order[-1]['image']
        for x in self.order:
            templastx = x['image']
            x['image'] = lastx
            lastx = templastx
        
    def onScale(self, value):
        self.msecs = int(float(value))

if __name__ == '__main__':
    #creates the top window of the application
    root = Toplevel()
    #gives the window a title
    root.title("Bridge Simulation")
    #creates the program class and passes the top window to be used
    BridgeSim(root)
  
    #repeats the program waiting for user input. can be ignored. put new code BEFORE this
    root.mainloop()