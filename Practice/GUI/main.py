import tkinter as tk
from tkinter import ttk
import customtkinter
from roboticstoolbox import SerialLink, RevoluteDH, PrismaticDH

class RoboticProgram(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("GUI Programming")
        self.label = ttk.Label(text = "Hello World")
        self.label.pack()
        
        self.result = ttk.Label(text = "Result: ")
        self.result.pack()
        
        self.entry = ttk.Entry(width = 10)
        self.entry.pack()
        
        self.button = ttk.Button(text = "Display", command = self.printVal)
        self.button.pack()
        
    def printVal(self):
        self.result["text"] = self.entry.get()

robot = RoboticProgram()
robot.mainloop()

