#!/usr/bin/python3

import time
from tkinter import *
from PIL import ImageTk, Image, ImageDraw

board = 

class myGUI(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(width=500, height=500, bg='white')
        self.canvas.pack()
        self.start_coordinates = (0, 0, 10, 10)
        self.add_rectangle()
        self.root.mainloop()

    def add_rectangle(self):
        self.canvas.create_rectangle(self.start_coordinates, fill="black")

        x1, y1, x2, y2 = self.start_coordinates
        x1 += 10
        y1 += 10
        x2 += 10
        y2 += 10
        self.start_coordinates = (x1, y1, x2, y2)

        self.root.after(2000, self.add_rectangle)

if __name__ == "__main__":
    gui = myGUI()