# -*- coding: utf-8 -*-
"""
3rd version of the bridge simulation that will try to animate the shapes
on a ttk canvas

Created on Fri Apr  7 11:39:32 2017

@author: tpwin10

possible improvements:
    -create object that contains image, with order index and movement as
        properties
    -set constant variables for movement switches instead of being hard coded
    -make triangles even so mevments can be the same for each direction
    -fix where the buttons are
"""

from tkinter import *
#from tkinter import PhotoImage
from tkinter import ttk


'''
Set up for the gui. can be ignored
'''

class BridgeSim(ttk.Frame):
   
    def __init__(self, parent=None, msecs=20, **args):
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

        self.speed1 = 7
        self.speed2 = 5
        self.speed3 = 3
        self.speed4 = 1
        self.drawCounter = 1
        self.msecs = msecs
        self.objects = []
        self.moveUp = (0, -2)
        self.moveDown = (0, 2)
        self.moveLeft = (-2, 0)
        self.moveRight = (2, 0)
        self.moveUpLeft = (-2, -.90)
        self.moveUpRight = (2, -1.15)
        self.moveDownLeft = (-2, .90)
        self.moveDownRight = (2, 1.05)
        #importing images into python
        ball1Image = PhotoImage(file='ball1.gif')
        bridgeImage = PhotoImage(file='bridge.gif')
        ball2Image = PhotoImage(file='ball2.gif')
        
        #needed so that images arent garbage collected 
        canvas.background = bridgeImage
        canvas.b = ball1Image
        canvas.bb = ball2Image
        
        ####Pixel boundary estimates
        #bottom border y = 155
        #top boarder y = 50
        
        #center line x for left side = 140
        #center line y = 108 
        #center line x for right side = 265
        
        #left side x = 35
        #right side x = 357
        
        #places images on canvas
        self.bridgeOb = canvas.create_image(200,100, image=bridgeImage)
        self.ball11Ob = canvas.create_image(35,89, image=ball1Image)
        self.ball12Ob = canvas.create_image(35,115, image=ball1Image)
        self.ball21Ob = canvas.create_image(357,89, image=ball2Image)
        self.ball22Ob = canvas.create_image(357,115, image=ball2Image)
        #put objects on canvas into a list
        self.objects = [self.ball11Ob, self.ball12Ob, self.ball21Ob, self.ball22Ob]
        #keeps track of direction and images crossing bridge
        self.leftOnBridge = []
        self.rightOnBridge = []
        #keeps track of waiting order
        self.waiting = []
        
        #list to keep  track of movement order on the chart
        self.order = [self.moveUp, self.moveDownRight, self.moveRight, self.moveUpRight, self.moveDown, self.moveUpLeft, self.moveLeft, self.moveDownLeft]
        
        #sets starting movement indecies
        self.ball11ObIND = 0
        self.ball12ObIND = 0
        self.ball21ObIND = 4
        self.ball22ObIND = 4
        
        
        #sets actually movements using indecies
        self.ball11ObcurrentMove = self.order[self.ball11ObIND]
        self.ball12ObcurrentMove = self.order[self.ball12ObIND]
        self.ball21ObcurrentMove = self.order[self.ball21ObIND]
        self.ball22ObcurrentMove = self.order[self.ball22ObIND]
        
        #puts the widgets on to the canvas
        self.makeWidgets()

        
    def makeWidgets(self):
        #creates button to stop and start the simulation
        self.onoff = Button(self, text='Start', command=self.onStart)   
        self.onoff.grid(column=1, row=3)   
        
        #creates the slider that is not used yet
        #note that the .grid at the end places it onto the GUI
        self.s = ttk.Scale(self, command=self.onScale,orient=HORIZONTAL, length=200, from_=1, to=300).grid(column=1,row=2)
        
        self.sp1 = ttk.Scale(self, command=self.onSpeedScale1,orient=HORIZONTAL, length=100, from_=0, to=10).grid(column=1,row=7)
        self.sp2 = ttk.Scale(self, command=self.onSpeedScale2,orient=HORIZONTAL, length=100, from_=0, to=10).grid(column=1,row=8)
        self.sp3 = ttk.Scale(self, command=self.onSpeedScale3,orient=HORIZONTAL, length=100, from_=0, to=10).grid(column=1,row=9)
        self.sp4 = ttk.Scale(self, command=self.onSpeedScale4,orient=HORIZONTAL, length=100, from_=0, to=10).grid(column=1,row=10)
        

    
        
        self.progTypeFlag = IntVar()
        
        self.progTypeFlag.set(1)
        
        #radio button to control type of protocol used by program
        self.r1 = Radiobutton(self, text="One Person on Bridge", variable=self.progTypeFlag, value=1)
        self.r1.grid(column=1, row=5)
        self.r2 = Radiobutton(self, text="More than One if Same Way", variable=self.progTypeFlag, value=0)
        self.r2.grid(column=1, row=6)
        
        
    #Starts simulation
    def onStart(self):
        self.loop = 1
        self.onoff.config(text='Stop', command=self.onStop)
        self.onTimer()
    #stops simulation
    def onStop(self):
        self.loop = 0
        self.onoff.config(text='Start', command=self.onStart)
    
    #if simulation is running, animates 
    def onTimer(self):
        if self.loop:
            self.drawNext()
            self.after(self.msecs, self.onTimer)
    
    #checks the location of objects and changes directions accordingly
    #also makes sure that images are going the same way on the bridge            

    def checkMoves2Bridge(self, currentObj):
        #print('left', self.leftOnBridge)
        #print('right', self.rightOnBridge)
        
        #each section checks if the image is at a turning point then updates the direction index and movement var
        if self.canvas.coords(currentObj)[0] == 35 and self.canvas.coords(currentObj)[1] == 55:
            self.canvas.move(currentObj, 0, -3)
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
        
        if self.canvas.coords(currentObj)[1] - 107 < .7 and self.canvas.coords(currentObj)[1] - 107 > 0 and self.canvas.coords(currentObj)[0] == 141:
            
            #checks if bridge is clear and object about to cross is first in line
            #moves ball or sets it still
            if len(self.leftOnBridge) < 1 and (len(self.waiting) == 0 or currentObj == self.waiting[0]):
                self.rightOnBridge.append(currentObj)
                if currentObj in self.waiting:
                    self.waiting.remove(currentObj)
                
                if currentObj == self.ball11Ob:
                    self.ball11ObIND += 1
                    self.ball11ObcurrentMove = self.order[self.ball11ObIND]
                elif currentObj == self.ball12Ob:
                    self.ball12ObIND += 1
                    self.ball12ObcurrentMove = self.order[self.ball12ObIND]
                elif currentObj == self.ball21Ob:
                    self.ball21ObIND += 1
                    self.ball21ObcurrentMove = self.order[self.ball21ObIND]
                elif currentObj == self.ball22Ob:
                    self.ball22ObIND += 1
                    self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            else:
                if currentObj == self.ball11Ob:
                    self.ball11ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball12Ob:
                    self.ball12ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball21Ob:
                    self.ball21ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball22Ob:
                    self.ball22ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
            
        if self.canvas.coords(currentObj)[1] - 107 < .7 and self.canvas.coords(currentObj)[1] - 107 > 0 and self.canvas.coords(currentObj)[0] == 257:
            self.rightOnBridge.remove(currentObj)
            
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
            
        if self.canvas.coords(currentObj)[1] - 50 < .2 and self.canvas.coords(currentObj)[1] - 50 > 0 and self.canvas.coords(currentObj)[0] == 357:
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
                
        if self.canvas.coords(currentObj)[1] == 155 and self.canvas.coords(currentObj)[0] == 357:
            self.canvas.move(currentObj, 0, 1.14999999999966)
            
        if self.canvas.coords(currentObj)[1] - 156 < .2 and self.canvas.coords(currentObj)[1] - 156 > 0 and self.canvas.coords(currentObj)[0] == 357:
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 111 < .2 and self.canvas.coords(currentObj)[1] - 111 > 0 and self.canvas.coords(currentObj)[0] == 257:

            if len(self.rightOnBridge) < 1 and (len(self.waiting) == 0 or currentObj == self.waiting[0]):
                self.leftOnBridge.append(currentObj)
                if currentObj in self.waiting:
                    self.waiting.remove(currentObj)
                
                if currentObj == self.ball11Ob:
                    self.ball11ObIND += 1
                    self.ball11ObcurrentMove = self.order[self.ball11ObIND]
                elif currentObj == self.ball12Ob:
                    self.ball12ObIND += 1
                    self.ball12ObcurrentMove = self.order[self.ball12ObIND]
                elif currentObj == self.ball21Ob:
                    self.ball21ObIND += 1
                    self.ball21ObcurrentMove = self.order[self.ball21ObIND]
                elif currentObj == self.ball22Ob:
                    self.ball22ObIND += 1
                    self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            else:
                if currentObj == self.ball11Ob:
                    self.ball11ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball12Ob:
                    self.ball12ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball21Ob:
                    self.ball21ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball22Ob:
                    self.ball22ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                    
        if self.canvas.coords(currentObj)[1] - 111 < .2 and self.canvas.coords(currentObj)[1] - 111 > 0 and self.canvas.coords(currentObj)[0] == 141:
            self.leftOnBridge.remove(currentObj)
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 159 > -.2 and self.canvas.coords(currentObj)[1] - 159 < 0 and self.canvas.coords(currentObj)[0] == 35:
            if currentObj == self.ball11Ob:
                self.ball11ObIND = 0
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND = 0
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND = 0
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND = 0
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 61 > -.2 and self.canvas.coords(currentObj)[1] - 61 < 0 and self.canvas.coords(currentObj)[0] == 35:
            self.canvas.move(currentObj, 0, -1.84999999999968)

    def checkMoves(self, currentObj):
        
        if self.canvas.coords(currentObj)[0] == 35 and self.canvas.coords(currentObj)[1] == 55:
            self.canvas.move(currentObj, 0, -3)
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
        
        if self.canvas.coords(currentObj)[1] - 107 < .7 and self.canvas.coords(currentObj)[1] - 107 > 0 and self.canvas.coords(currentObj)[0] == 141:

                
            if (len(self.rightOnBridge) + len(self.leftOnBridge) < 1) and (len(self.waiting) == 0 or currentObj == self.waiting[0]):
                #if statement not needed, always goes else
                if self.rightOnBridge.__contains__(currentObj):
                    print("wait")
                else:
                    self.rightOnBridge.append(currentObj)
                    if currentObj in self.waiting:
                        self.waiting.remove(currentObj)
                    #print("added")
                
                if currentObj == self.ball11Ob:
                    self.ball11ObIND += 1
                    self.ball11ObcurrentMove = self.order[self.ball11ObIND]
                elif currentObj == self.ball12Ob:
                    self.ball12ObIND += 1
                    self.ball12ObcurrentMove = self.order[self.ball12ObIND]
                elif currentObj == self.ball21Ob:
                    self.ball21ObIND += 1
                    self.ball21ObcurrentMove = self.order[self.ball21ObIND]
                elif currentObj == self.ball22Ob:
                    self.ball22ObIND += 1
                    self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            else:
                if currentObj == self.ball11Ob:
                    self.ball11ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball12Ob:
                    self.ball12ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball21Ob:
                    self.ball21ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball22Ob:
                    self.ball22ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
            
        if self.canvas.coords(currentObj)[1] - 107 < .7 and self.canvas.coords(currentObj)[1] - 107 > 0 and self.canvas.coords(currentObj)[0] == 257:
            self.rightOnBridge.remove(currentObj)
            
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
            
        if self.canvas.coords(currentObj)[1] - 50 < .2 and self.canvas.coords(currentObj)[1] - 50 > 0 and self.canvas.coords(currentObj)[0] == 357:
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
                
        if self.canvas.coords(currentObj)[1] == 155 and self.canvas.coords(currentObj)[0] == 357:
            self.canvas.move(currentObj, 0, 1.14999999999966)
            
        if self.canvas.coords(currentObj)[1] - 156 < .2 and self.canvas.coords(currentObj)[1] - 156 > 0 and self.canvas.coords(currentObj)[0] == 357:
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 111 < .2 and self.canvas.coords(currentObj)[1] - 111 > 0 and self.canvas.coords(currentObj)[0] == 257:
            
            if (len(self.leftOnBridge) + len(self.rightOnBridge) < 1) and (len(self.waiting) == 0 or currentObj == self.waiting[0]):
                if self.leftOnBridge.__contains__(currentObj):
                    print("wait")
                else:
                    self.leftOnBridge.append(currentObj)
                    if currentObj in self.waiting:
                        self.waiting.remove(currentObj)
                    #print("addedL")
                
                if currentObj == self.ball11Ob:
                    self.ball11ObIND += 1
                    self.ball11ObcurrentMove = self.order[self.ball11ObIND]
                elif currentObj == self.ball12Ob:
                    self.ball12ObIND += 1
                    self.ball12ObcurrentMove = self.order[self.ball12ObIND]
                elif currentObj == self.ball21Ob:
                    self.ball21ObIND += 1
                    self.ball21ObcurrentMove = self.order[self.ball21ObIND]
                elif currentObj == self.ball22Ob:
                    self.ball22ObIND += 1
                    self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            else:
                if currentObj == self.ball11Ob:
                    self.ball11ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball12Ob:
                    self.ball12ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball21Ob:
                    self.ball21ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                elif currentObj == self.ball22Ob:
                    self.ball22ObcurrentMove = (0,0)
                    if currentObj not in self.waiting:
                        self.waiting.append(currentObj)
                    
        if self.canvas.coords(currentObj)[1] - 111 < .2 and self.canvas.coords(currentObj)[1] - 111 > 0 and self.canvas.coords(currentObj)[0] == 141:
            self.leftOnBridge.remove(currentObj)
            if currentObj == self.ball11Ob:
                self.ball11ObIND += 1
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND += 1
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND += 1
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND += 1
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 159 > -.2 and self.canvas.coords(currentObj)[1] - 159 < 0 and self.canvas.coords(currentObj)[0] == 35:
            if currentObj == self.ball11Ob:
                self.ball11ObIND = 0
                self.ball11ObcurrentMove = self.order[self.ball11ObIND]
            elif currentObj == self.ball12Ob:
                self.ball12ObIND = 0
                self.ball12ObcurrentMove = self.order[self.ball12ObIND]
            elif currentObj == self.ball21Ob:
                self.ball21ObIND = 0
                self.ball21ObcurrentMove = self.order[self.ball21ObIND]
            elif currentObj == self.ball22Ob:
                self.ball22ObIND = 0
                self.ball22ObcurrentMove = self.order[self.ball22ObIND]
            
        if self.canvas.coords(currentObj)[1] - 61 > -.2 and self.canvas.coords(currentObj)[1] - 61 < 0 and self.canvas.coords(currentObj)[0] == 35:
            self.canvas.move(currentObj, 0, -1.84999999999968)
      
    #called by timer repeatedly
    def drawNext(self):
        
        self.drawCounter += 1
        
        
        #moves each image every timer interval

        if self.drawCounter % self.speed1 == 0:
            if self.progTypeFlag.get():
                #regular 1 at a time checker
                self.checkMoves(self.ball11Ob)
            else:
                #allows two balls to go the same way
                self.checkMoves2Bridge(self.ball11Ob)
                        
            self.canvas.move(self.ball11Ob, self.ball11ObcurrentMove[0], self.ball11ObcurrentMove[1])
        
        if self.drawCounter % self.speed2 == 0:
            if self.progTypeFlag.get():
                #regular 1 at a time checker
                self.checkMoves(self.ball12Ob)
            else:
                #allows two balls to go the same way
                self.checkMoves2Bridge(self.ball12Ob)
                        
            self.canvas.move(self.ball12Ob, self.ball12ObcurrentMove[0], self.ball12ObcurrentMove[1])
            
        if self.drawCounter % self.speed3 == 0:
            if self.progTypeFlag.get():
                #regular 1 at a time checker
                self.checkMoves(self.ball21Ob)
            else:
                #allows two balls to go the same way
                self.checkMoves2Bridge(self.ball21Ob)
                        
            self.canvas.move(self.ball21Ob, self.ball21ObcurrentMove[0], self.ball21ObcurrentMove[1])    
            
        if self.drawCounter % self.speed4 == 0:
            if self.progTypeFlag.get():
                #regular 1 at a time checker
                self.checkMoves(self.ball22Ob)
            else:
                #allows two balls to go the same way
                self.checkMoves2Bridge(self.ball22Ob)
                        
            self.canvas.move(self.ball22Ob, self.ball22ObcurrentMove[0], self.ball22ObcurrentMove[1])  
            
        #print(self.speed1,self.speed2,self.speed3,self.speed4)
        #print(self.waiting)
        
        if self.drawCounter == 100:
            self.drawCounter = 1
        
    
    def onSpeedScale1(self, value1):
        self.speed1 = int(float(value1))
        if self.speed1 == 0:
            self.speed1 = 1
 
    def onSpeedScale2(self, value2):
        self.speed2 = int(float(value2))
        if self.speed2 == 0:
            self.speed2 = 1
    
    def onSpeedScale3(self, value3):
        self.speed3 = int(float(value3))
        if self.speed3 == 0:
            self.speed3 = 1
            
    def onSpeedScale4(self, value4):
        self.speed4 = int(float(value4))
        if self.speed4 == 0:
            self.speed4 = 1
    
    #updates the speed up the simulation when the slider is moved        
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