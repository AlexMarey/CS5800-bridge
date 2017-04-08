# -*- coding: utf-8 -*-
"""
3rd version of the bridge simulation that will try to animate the shapes
on a ttk canvas

Created on Fri Apr  7 11:39:32 2017

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
        self.grid()
        canvas = Canvas(parent, width=600, height=300)
        canvas.grid(column=1, row=1)
        #canvas.pack(expand=YES, fill=BOTH)
        
        self.canvas = canvas
        #sets up the content manager for the window
        #self.grid()
        #sets class variable for the speed that can be used by any method
        self.msecs = msecs
        self.images = []
        self.object = None
        self.moveUp = (0, -2)
        self.moveDown = (0, 2)
        self.moveLeft = (-2, 0)
        self.moveRight = (2, 0)
        self.moveUpLeft = (-2, -.90)
        self.moveUpRight = (2, -.90)
        self.moveDownLeft = (-2, 1.15)
        self.moveDownRight = (2, 1.05)
        #importing images into python
        ball1Image = PhotoImage(file='ball1.gif')
        bridgeImage = PhotoImage(file='bridge.gif')
        ball2Image = PhotoImage(file='ball2.gif')
        
        canvas.background = bridgeImage
        canvas.b = ball1Image
        canvas.bb = ball2Image
        
        #bottom border y = 155
        #top boarder y = 50
        
        #center line x for left side = 140
        #center line y = 108 
        #center line x for right side = 265
        
        #left side x = 35
        #right side x = 357
        
        
        self.bridgeOb = canvas.create_image(200,100, image=bridgeImage)
        self.ball11Ob = canvas.create_image(35,90, image=ball1Image)
        self.ball12Ob = canvas.create_image(357,90, image=ball2Image)
        self.ball21Ob = canvas.create_image(35,115, image=ball1Image)
        self.ball22Ob = canvas.create_image(357,115, image=ball2Image)
        self.testball = canvas.create_image(357, 50, image=ball1Image)
        #puts the widgets on to the canvas
        self.makeWidgets()

        
    def makeWidgets(self):
      
        #first line creates "label" item (basically the picture holder
        #second line sets its location in the grid (col=2, row=2)
        #third line sets the 'image' property to previously imported image
        #self.images.append(self.bridgeImage)
        #print(self.bridgeImage)
        #self.object = self.canvas.create_image(200, 100, image=self.bridgeImage)
        #self.canvas.create_oval(100,100, 200,200)
        #self.canvas.update()
        print(self.object)
        
#        self.bridge = ttk.Label(self)
#        self.bridge.grid(column=2, row=2)
#        self.bridge['image'] = self.bridgeImage
#        
#                   
#        
#        self.canvas.create_image(50,50, image=self.bridgeImage)
#                  
#        set up for each individual block
#        first two are commented to explain. The rest are exactly the same
#        
#            
#        self.channelTop1 = ttk.Label(self)
#        sticky=W means that the picture will go to the "West" (left) side of the label object(aka the square in the grid)
#        self.channelTop1.grid(column=2, row=1, sticky=(W))
#        self.channelTop1['image'] = self.ball1Image
#        
#        self.channelTop2 = ttk.Label(self)
#        self.channelTop2.grid(column=2, row=1, sticky=(E))
#        self.channelTop2['image'] = self.ball1Image
#        
#        self.channelBottom2 = ttk.Label(self)
#        self.channelBottom2.grid(column=2, row=3, sticky=(E))
#        self.channelBottom2['image'] = self.ball2Image           
#                   
#        self.channelBottom1 = ttk.Label(self)
#        self.channelBottom1.grid(column=2, row=3, sticky=(W))
#        self.channelBottom1['image'] = self.ball2Image              
#                      
#        self.sideB1 = ttk.Label(self)
#        self.sideB1.grid(column=3, row=2, sticky=(N))
#        self.sideB1['image'] = self.ball1Image
#             
#        self.sideA1 = ttk.Label(self)
#        self.sideA1.grid(column=1, row=2, sticky=(N))
#        self.sideA1['image'] = self.ball2Image
#              
#        self.sideB2 = ttk.Label(self)
#        self.sideB2.grid(column=3, row=2, sticky=(S))
#        self.sideB2['image'] = self.ball1Image
#             
#        self.sideA2 = ttk.Label(self)
#        self.sideA2.grid(column=1, row=2, sticky=(S))
#        self.sideA2['image'] = self.ball2Image   
#        
        #creates button to stop and start the simulation
        self.onoff = Button(self, text='Start', command=self.onStart)   
        self.onoff.grid(column=1, row=3)   
        
        #creates the slider that is not used yet
        #note that the .grid at the end places it onto the GUI
        self.s = ttk.Scale(self, command=self.onScale,orient=HORIZONTAL, length=200, from_=0, to=3000).grid(column=1,row=2)
        
#        self.order = [self.channelTop1, self.channelTop2, self.sideB1, self.sideB2, self.channelBottom2, self.channelBottom1, self.sideA2, self.sideA1]
             
#        #makes padding between each element. Can be ignored
#        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)
    
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
        
        self.canvas.move(self.ball11Ob, self.moveDown[0], self.moveDown[1])
        self.canvas.move(self.ball12Ob, 1, 1)
        self.canvas.move(self.ball21Ob, 1, 0)
        self.canvas.move(self.ball22Ob, -1,-1)
        self.canvas.move(self.testball, self.moveDownLeft[0], self.moveDownLeft[1])
        
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