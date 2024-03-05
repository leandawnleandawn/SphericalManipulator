import tkinter as tk
import customtkinter as ctk
from roboticstoolbox import SerialLink, RevoluteDH, PrismaticDH

class RoboticProgram(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("Kinematic Analysis")
        self.windowTitle = tk.Label(text="Kinematic Analysis Calculator")
        self.windowTitle.pack()
        
        self.FKin = tk.Button(text = "Forward Kinematics", command = FKinWindow)
        self.FKin.pack()
        
        self.IKin = tk.Button(text = "Inverse Kinematics", command= IKinWindow)
        self.IKin.pack()
        
        self.JBin = tk.Button(text = "Jacobian Matrix", command= IKinWindow)
        self.JBin.pack()

class FKinWindow:
    def __init__(self):
        self.windowTitle = tk.Toplevel(master = robot)
        
        
class IKinWindow:
    def __init__(self):
        self.windowTitle = tk.Toplevel(master = robot)
        
class JBinWindow:
    def __init__(self):
        self.windowTitle = tk.Toplevel(master = robot)
        
robot = RoboticProgram()
robot.mainloop()

