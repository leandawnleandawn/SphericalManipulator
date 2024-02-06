import numpy as np
import scipy as sp
import sympy as syp
from matplotlib.pyplot import plot
import os
import time


class Robot:
    '''The Following Blueprint of the Robot
	Child: Joint, and Link
    '''
    number_joint = 0
    number_link = 0

class Joint(Robot):
    '''The Following Blueprint of the Joints connecting the Robot
	Child: Prismatic and Revolute
    '''
    orientation = np.array([0,0,0])
    
class Prismatic(Joint):
    '''The Following Blueprint of the Prismatic
	Child: Prismatic and Revolute
    '''
    joint_limit = [0, 5]

class Revolute(Joint):
    '''The Following Blueprint of the Revolute Joints connecting the Robot
	Child: Prismatic and Revolute
    '''
    joint_limit = [-90, 90]

def mainMenu():
    while True:
        os.system("cls")
        print("*_" * 20)
        print("     Denavit Hartenberg Frame and Table Creator     ")
        print("[C]		Create a Mechanical Manipulator")
        print("[M]		Manual on DH Parameters and Robotics Design")
        print("[q]		Quit")
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
    print("Exiting", end = "\0")
    for i in range(3):
        print(".", flush = True, end="\0")
        time.sleep(1)
    os.system("cls")

def createManipulator():
    joints = {}
    robot = Robot()
    i = 0
    while True:
        print("We are creating a Manipulator")
        print("   What type of Joint Variable?   ")
        print("[R]          Revolute             ")
        print("[P]          Pristmatic           ")
        print("[V]         View Joints           ")
        print("[-1]         End the Operation     ")
        user_input = input("...")
        joints[i] = 0
        if user_input == 'R':
            print("indicate what orientation of its z-axis")
            orientation_input = input("([F]orward, [B]ackward, [L]eft, [R]ight, [U]p, [D]own)...")
            joints[i] = Revolute()
            if orientation_input == "L":
                joints[i].orientation = np.array([1, 0, 0])
            if orientation_input == "R":
                joints[i].orientation = np.array([-1, 0, 0])
            if orientation_input == "F":
                joints[i].orientation = np.array([0, -1, 0])
            if orientation_input == "B":
                joints[i].orientation = np.array([0, 1, 0])
            if orientation_input == "U":
                joints[i].orientation = np.array([0, 0, 1])
            if orientation_input == "U":
            	joints[i].orientation = np.array([0, 0, -1])
            i += 1
        if user_input == 'P':
            print("indicate what orientation of its z-axis")
            orientation_input = input("([F]orward, [B]ackward, [L]eft, [R]ight, [U]p, [D]own)...")
            joints[i] = Prismatic()
            if orientation_input == "L":
                joints[i].orientation = np.array([1, 0, 0])
            if orientation_input == "R":
                joints[i].orientation = np.array([-1, 0, 0])
            if orientation_input == "F":
                joints[i].orientation = np.array([0, -1, 0])
            if orientation_input == "B":
                joints[i].orientation = np.array([0, 1, 0])
            if orientation_input == "U":
                joints[i].orientation = np.array([0, 0, 1])
            if orientation_input == "U":
            	joints[i].orientation = np.array([0, 0, -1])
            i += 1
        if user_input == 'V':
            print(joints)
        if user_input == "-1":
            print("Exiting the following menu", end = " ")
            for i in range(3):
                print(".", flush = True, end="\0")
                time.sleep(1)
            break




mainMenu()