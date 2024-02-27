import tkinter as tk
from tkinter import ttk
import customtkinter
from roboticstoolbox import SerialLink, RevoluteDH, PrismaticDH

class RoboticProgram(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("GUI Programming")
        self.label = tk.Label(text = "Hello World")
        self.label.pack()
        
        self.result = tk.Label(text = "Result: ")
        self.result.pack()
        
        self.entry = tk.Entry(width = 10)
        self.entry.pack()
        
        self.button = tk.Button(text = "Display", command = self.printVal)
        self.button.pack()
        
    def printVal(self):
        self.result["text"] = f"Result: {self.entry.get()}"

robot = RoboticProgram()
robot.mainloop()

