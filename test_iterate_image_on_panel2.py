'''
Created on 30-Oct-2021

@author: Sundar
'''

from tkinter import messagebox
from os import system, name
from time import sleep
import numpy as np
import os
import glob
import serial

import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
import PIL.Image, PIL.ImageTk
import cv2
import time
import imutils
from tkinter import *
import time
from PIL import Image, ImageChops, ImageStat
from numpy import asarray # To convert 
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog as tkFileDialog 
im = "cat.jpg"

class Album(tk.Frame):
    def __init__(self, parent, window):
        self.wd = 400
        self.path = None
        self.totalPath = None
        self.count = 0
        self.fileList = None
        self.choice = [0,1,2]
        
        self.countFPNG = 0
        self.countBPNG = 0
        self.countKeeperPNG = 0
        
        self.countFJPG = 0
        self.countBJPG = 0
        self.countKeeperJPG = 0
        
        self.stateOfChoice = self.choice[0]
        self.fileCount = 0
        
        
        self.backButton = Button(root, text="<",font=("Verdana",25,"bold"), command=self.iterateBackThroughImages)
        self.backButton.place(x=1050, y=700)
        
        self.forwardButton = Button(root, text=">", font=("Verdana",25,"bold"),command=self.iterateForwardThroughImages)
        self.forwardButton.place(x=1100, y=700)
        
        self.resetButton = Button(root, text='RST',font=("Verdana",15,"bold"),command=self.resetButtons)
        self.resetButton.place(x=1070,y=800)

        self.imageCountLabel = Label(root, text="Image Count")
        
        self.imageCountLabel.place(x=50, y=20)
        
        self.imageCount = Label(root, text=str(self.count))
        self.imageCount.place(x=150, y=20)
        
        self.fileListLabel = Label(root, text="Total Files")
        self.fileListLabel.place(x=50, y=80)
        
        self.fileListCount = Label(root, text="")
        self.fileListCount.place(x=150, y=80)
        
        self.folderPathLabel = Label(root, text="Folder path")
        self.folderPathLabel.place(x=50, y=140)
        
        self.folderPath = Label(root, text="")
        self.folderPath.place(x=150,y=140)
        
        self.fileNameLabel = Label(root, text="File name")
        self.fileNameLabel.place(x=50, y=200)
        
        self.fileName = Label(root, text="")
        self.fileName.place(x=150, y=200)
        
        self.fileTypes = Label(root, text="Image types")
        self.fileTypes.place(x=50, y= 260)
        
        self.files = Label(root, text="")
        self.files.place(x=150, y=260)

        self.choosePathButton = Button(root, text="Choose Folder",command=self.getFolderPath)
        self.choosePathButton.place(x=50, y= 320)
        self.theFileName = []
        # Dropdown menu
        options = [
                        "All Image Files",
                        "PNG *.png",
                        "JPG *.jpg"
                        ]
        def getFileTypes():
            global panelA      
            self.typeOfFile = self.clicked.get()
            #print(clicked.get())
            if self.typeOfFile == options[0]:
                total = 0
                print("All")
                self.files.config(text="All")
                
                self.totalPath = self.path + "/" +"*.png"
                print(self.totalPath)
                self.fileList = glob.glob(self.totalPath)
                print(self.fileList)
                total = len(self.fileList)
                self.fileCount = total
                
                self.totalPath = self.path + "/" +"*.jpg"
                print(self.totalPath)
                self.fileList = glob.glob(self.totalPath)
                print(self.fileList)
                total = total + len(self.fileList)
                
                print(total)
                self.fileListCount.config(text=str(total))
                                
            elif self.typeOfFile == options[1]:
                print("PNG")
                self.files.config(text="*.png")
                self.totalPath = self.path + "/" +"*.png"
                print(self.totalPath)
                self.fileList = glob.glob(self.totalPath)
                print("File List",self.fileList)
                self.fileCount = len(self.fileList)
                self.fileListCount.config(text=str(len(self.fileList)))
                self.stateOfChoice = self.choice[1] # Setting state of choice to *.png
                
                self.theFileName = self.fileList[0].split('\\')
                self.fileName.config(text=self.theFileName[1])
                im = self.fileList[0]
                image = cv2.imread(im)
                image = imutils.resize(image,width=self.wd)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
                # convert the images to PIL format...
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
                panelA = tk.Label(image=image)
                panelA.image = image
                panelA.place(x=900,y=150)
                
            elif self.typeOfFile == options[2]:
                print("JPG")
                self.files.config(text="*.jpg")
                self.totalPath = self.path + "/" +"*.jpg"
                print(self.totalPath)
                self.fileList = glob.glob(self.totalPath)
                print(self.fileList)
                self.fileCount = len(self.fileList)
                self.fileListCount.config(text=str(len(self.fileList)))
                self.stateOfChoice = self.choice[2] # Setting state of choice to *.jpg
                
                self.theFileName = self.fileList[0].split('\\')
                self.fileName.config(text=self.theFileName[1])
                im = self.fileList[0]
                image = cv2.imread(im)
                image = imutils.resize(image,width=self.wd)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
                # convert the images to PIL format...
                image = Image.fromarray(image)
                image = ImageTk.PhotoImage(image)
                panelA = tk.Label(image=image)
                panelA.image = image
                panelA.place(x=900,y=150)
        
        self.clicked = StringVar()

        self.clicked.set("")
        
        self.dropDown = OptionMenu(root, self.clicked, *options)
        self.dropDown.place(x=150, y= 380)
        
        self.dropDownLabel = Label(root, text="File types")
        self.dropDownLabel.place(x=50, y=380)
        
        self.dropDownButton = Button(root, text="Click",command=getFileTypes)
        self.dropDownButton.place(x=300, y=380)
        
        self.messageLabel = Label(root, text="")
        self.messageLabel.place(x=400, y=380)
        
        self.dropDownButton.config(state='disabled')
        self.typeOfFile = None
        self.width = 300
        self.height = 300
        #self.getImage()
    
    def getFolderPath(self):
        self.path = tkFileDialog.askdirectory() # Choose Directory
        self.folderPath.config(text=self.path)
        self.dropDownButton.config(state='normal')
        self.messageLabel.config(text="Click this after choosing file types from dropdown")
          
    def getImage(self):
        # grab a reference to the image panels
        global panelA
        image = cv2.imread(im)
        image = imutils.resize(image,width=self.wd)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
        # convert the images to PIL format...
        image = Image.fromarray(image)
        image = image.resize((self.width,self.height))
        image = ImageTk.PhotoImage(image)
        panelA = tk.Label(image=image)
        panelA.image = image
        panelA.place(x=900,y=150)
    
    def iterateForwardThroughImages(self):
        global panelA
        if self.stateOfChoice == 0:
            print("All")
            #panelA.image = ''
            self.fileList = glob.glob('*.*')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            image = cv2.imread(self.fileList[self.count])
            self.fileName.config(text=self.fileList[self.count])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.count))
            self.count +=1
        elif self.stateOfChoice == 1:
            print("png")
            panelA.image = ''
            self.countKeeperPNG +=1
            #print("Keeper F",self.countKeeperPNG)
            self.countFPNG=self.countKeeperPNG
            self.fileList = glob.glob('*.png')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            image = cv2.imread(self.fileList[self.countFPNG])
            self.fileName.config(text=self.fileList[self.countFPNG])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.countFPNG))
            #self.countKeeperPNG +=1

        elif self.stateOfChoice == 2:
            print("jpg")
            panelA.image = ''
            self.countKeeperJPG +=1
            self.countFJPG=self.countKeeperJPG
            self.fileList = glob.glob('*.jpg')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            image = cv2.imread(self.fileList[self.countFJPG])
            self.fileName.config(text=self.fileList[self.countFJPG])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.countFJPG))
        
    def iterateBackThroughImages(self):
        global panelA
        if self.stateOfChoice == 0:
            print("All")
            #panelA.image = ''
            self.countBPNG=self.countKeeperPNG
            self.fileList = glob.glob('*.*')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            self.fileCount -= 1
            print((self.fileCount) - 1)
            
            image = cv2.imread(self.fileList[ self.fileCount ] )
            self.fileName.config(text=self.fileList[ self.fileCount ])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.count))
        elif self.stateOfChoice == 1:
            print("png")
            panelA.image = ''
            self.fileList = glob.glob('*.png')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            self.countKeeperPNG -= 1
            print("Keeper B",self.countKeeperPNG)
            self.countBPNG = self.countKeeperPNG
            
            image = cv2.imread(self.fileList[ self.countBPNG ] )
            self.fileName.config(text=self.fileList[ self.countBPNG ])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.countBPNG))
        elif self.stateOfChoice == 2:
            print("jpg")
            panelA.image = ''
            self.countKeeperJPG -=1
            self.countBJPG=self.countKeeperJPG
            self.fileList = glob.glob('*.jpg')
            if self.count >= len(self.fileList):
                self.forwardButton.config(state='disabled')
            image = cv2.imread(self.fileList[self.countBJPG])
            self.fileName.config(text=self.fileList[self.countBJPG])
            image = imutils.resize(image,width=self.wd) 
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Absence of this will make the image look blue colored
            # convert the images to PIL format...
            image = Image.fromarray(image)
            image = image.resize((self.width,self.height))
            image = ImageTk.PhotoImage(image)            
            panelA = tk.Label(image=image)
            panelA.image = ''
            panelA.image = image
            panelA.place(x=900,y=150)
            self.imageCount.config(text=str(self.countBJPG))
            
    
    def resetButtons(self):
        self.forwardButton.config(state='normal')
        self.backButton.config(state='normal')

panelA = None

if __name__ == "__main__":
    root = Tk()
    root.title("Photo Album")
    root.geometry('1034x740')
    root.state('zoomed')
    widget = Album(root, root)
    
    root.mainloop()
