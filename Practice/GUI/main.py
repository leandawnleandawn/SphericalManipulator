import tkinter as tk
import numpy as np
import customtkinter as ctk
from roboticstoolbox import SerialLink, RevoluteDH, PrismaticDH

class RoboticProgram(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Kinematic Analysis")
        self.windowTitle = tk.Label(text="Kinematic Analysis Calculator")
        self.windowTitle.pack()
        
        FKin = tk.Button(text = "Forward Kinematics", command = FkinWindow)
        FKin.pack()
        
        IKin = tk.Button(text = "Inverse Kinematics", command= IkinWindow)
        IKin.pack()
        
        JBin = tk.Button(text = "Jacobian Matrix", command= Window)
        JBin.pack()
        
        
class Window(RoboticProgram):
    def __init__(self):
        self.windowTitle = tk.Toplevel(master = robot)
        
        LL = tk.LabelFrame(master=self.windowTitle, text = "Link Length and Joint Variables", font=(5))
        LL.grid(row = 0, column = 0)
        
        a1L = tk.Label(LL, text = ("a1 = "), font=(10))
        self.a1data = tk.Entry(LL,width=5, font=(10))
        cm1 = tk.Label(LL, text = ("cm"), font=(10))
        
        a2L = tk.Label(LL, text = ("a2 = "), font=(10))
        self.a2data = tk.Entry(LL,width=5, font=(10))
        cm2 = tk.Label(LL, text = ("cm"), font=(10))
        
        a3L = tk.Label(LL, text = ("a3 = "), font=(10))
        self.a3data = tk.Entry(LL,width=5, font=(10))
        cm3 = tk.Label(LL, text = ("cm"), font=(10))
        
        a1L.grid(row=0,column=0)
        self.a1data.grid(row=0,column=1)
        cm1.grid(row=0,column=2)
        
        a2L.grid(row=1,column=0)
        self.a2data.grid(row=1,column=1)
        cm2.grid(row=1,column=2)
        
        a3L.grid(row=2,column=0)
        self.a3data.grid(row=2,column=1)
        cm3.grid(row=2,column=2)
        
        JV= tk.LabelFrame(master=self.windowTitle, text = "Joint Variables", font=(5))
        JV.grid(row = 0, column = 1)
        
        t1L = tk.Label(JV, text = ("T1 = "), font=(10))
        self.T1data = tk.Entry(JV,width=5, font=(10))
        deg1 = tk.Label(JV, text = ("deg"), font=(10))
        
        t2L = tk.Label(JV, text = ("T2 = "), font=(10))
        self.T2data = tk.Entry(JV,width=5, font=(10))
        deg2 = tk.Label(JV, text = ("deg"), font=(10))
        
        d3L = tk.Label(JV, text = ("d3 = "), font=(10))
        self.d3data = tk.Entry(JV,width=5, font=(10))
        cm4 = tk.Label(JV, text = ("cm"), font=(10))
        
        t1L.grid(row=0, column=0)
        self.T1data.grid(row=0, column=1)
        deg1.grid(row=0, column=2)
        
        t2L.grid(row=1, column=0)
        self.T2data.grid(row=1, column=1)
        deg2.grid(row=1, column=2)
        
        d3L.grid(row=2, column=0)
        self.d3data.grid(row=2, column=1)
        cm4.grid(row=2, column=2)
        
        PV = tk.LabelFrame(master=self.windowTitle, text = "Position Vector", font=(5))
        PV.grid(row = 2, column = 0)
        
        XL = tk.Label(PV, text = ("X = "), font=(10))
        self.Xdata = tk.Entry(PV,width=5, font=(10))
        cm5 = tk.Label(PV, text = ("cm"), font=(10))
        
        YL = tk.Label(PV, text = ("Y = "), font=(10))
        self.Ydata = tk.Entry(PV,width=5, font=(10))
        cm6 = tk.Label(PV, text = ("cm"), font=(10))
        
        ZL = tk.Label(PV, text = ("Z = "), font=(10))
        self.Zdata = tk.Entry(PV,width=5, font=(10))
        cm7 = tk.Label(PV, text = ("cm"), font=(10))
        
        XL.grid(row=0, column=0)
        self.Xdata.grid(row=0, column=1)
        cm5.grid(row=0, column=2)
        
        YL.grid(row=1, column=0)
        self.Ydata.grid(row=1, column=1)
        cm6.grid(row=1, column=2)
        
        ZL.grid(row=2, column=0)
        self.Zdata.grid(row=2, column=1)
        cm7.grid(row=2, column=2)
        
    def reset(self):
        self.a1data.delete(0,'end')
        self.a2data.delete(0, 'end')
        self.a3data.delete(0, 'end')
        self.T1data.delete(0, 'end')
        self.T2data.delete(0,'end')
        self.d3data.delete(0, 'end')
        
        
class FkinWindow(Window):	
    def __init__(self):
        super().__init__()
        self.windowTitle.title("Foward Kinematics")
        
        BF = tk.LabelFrame(master=self.windowTitle, font=(5))
        BF.grid(row=1, column=0)
        
        forward = tk.Button(BF, text = "Foward", command=self.fkin)
        forward.grid(row=0, column=0)
        reset = tk.Button(BF, text = "Reset", command=self.reset)
        reset.grid(row=0, column=1)
        
    def fkin(self):
        try:
            a1 = float(self.a1data.get()) / 100
            a2 = float(self.a2data.get()) / 100
            a3 = float(self.a3data.get()) / 100
            t1 = float(self.T1data.get())
            t2 = float(self.T2data.get())
            d3 = float(self.d3data.get()) / 100
        except ValueError:
            pop_up = tk.Toplevel(master= robot)
            label = tk.Label(pop_up, text = "Use the approriate syntax (float)")
            label.pack()
            
        parametric_table = [[t1, np.pi/2, 0, a1],
                            [np.pi/2 + t2, np.pi/2, 0, 0 ],
                            [0,0,0,a2+a3+d3]]
        htm = {}
        
        for i in range(3):
            htm[i] = self.dhMatrix(parametric_table[i][0], parametric_table[i][1], parametric_table[i][2], parametric_table[i][3])
            
        for i,j in htm.items():
            print(f"HTM # {i+1}")
            print(np.round(j, 2))
            
        result = np.dot(np.dot(htm[0], htm[1]), htm[2])
        print(np.round(result,2))
        
        self.Xdata.insert(tk.END, np.round(result[0,3],2))
        self.Ydata.insert(tk.END, np.round(result[1,3],2))
        self.Zdata.insert(tk.END, np.round(result[2,3],2))
        
    def dhMatrix(self, theta, alpha, radius, distance):
    	return np.matrix([
			[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        	[np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        	[0, np.sin(alpha), np.cos(alpha), distance],
        	[0,0,0,1],		
		])
    
class IkinWindow(Window):
    def __init__(self):
        super().__init__()
        self.windowTitle.title("Inverse Kinematics")
        
        BF = tk.LabelFrame(master=self.windowTitle, font=(5))
        BF.grid(row=1, column=0)
        
        inverse= tk.Button(BF, text = "Inverse")
        inverse.grid(row=0, column=0)
        reset = tk.Button(BF, text = "Reset")
        reset.grid(row=0, column=1)
        
class JBinWindow(Window):
    def __init__(self):
        super().__init__()
        self.windowTitle.title("Jacobian Kinematics")
        
        BF = tk.LabelFrame(master=self.windowTitle, font=(5))
        BF.grid(row=1, column=0)
        
        jacobian= tk.Button(BF, text = "Inverse")
        jacobian.grid(row=0, column=0)
        reset = tk.Button(BF, text = "Reset")
        reset.grid(row=0, column=1)
        
robot = RoboticProgram()
robot.mainloop()

