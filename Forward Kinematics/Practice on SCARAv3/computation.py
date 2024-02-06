import numpy as np
import scipy as sp
import sympy as syp
from matplotlib.pyplot import plot
import os
import time
class Robot:
    
def mainMenu():
    while True:
        os.system("cls")
        print("*_" * 20)
        print("     Denavit Hartenberg Frame and Table Creator     ")
        print("[C]		  			Create a Mechanical Manipulator")
        print("[M]		Manual on DH Parameters and Robotics Design")
        print("[q]											   Quit")
        user_input = input("...")
        if user_input == 'q':
            quitting()
            break	
        if user_input == "C":
            os.system("cls")
            createManipulator()
            continue
        if user_input == "M":
            continue

def quitting():
    os.system("cls")
    print("Exiting in", end = " ")
    for i in range(3):
        print(3-i, end = "\0")
        for i in range(3):
            print(".", flush = True, end="\0")
            time.sleep(1)
    os.system("cls")

def createManipulator():
    print("We are know creating a Manipulator")
    print("   What type of Joint Variable?   ")
    print("[R]          Revolute             ")
    print("[P]          Pristmatic           ")
    user_input = input("...")
    if user_input == 'R':
        print("indicate what orientation of its z-axis")
        orientation = input("")
    pass




mainMenu()