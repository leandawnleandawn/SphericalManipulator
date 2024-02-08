import numpy as np
import math

# Exercise 1: Creating a Denavit Hartenberg Calculator given the Parameters
# Objective:
#     to solve and to create the Denavit Hartenberg Matrix to 
#     simplify the following Transformation of the Mechanical 
#     Manipulator (In this case, SCARAV3)

# Algorithm:
#     1. Identify the Link Length
#     2. Create a Denavit Hartenberg Paramteric Table
#     3. Plug-in the Matrix of the following Manipulator
#     4. Matrix Multiply the Transformation Matrices.
    
# Conventions Used:
#     a_<number> - Constant Link Length
#     theta = Joint Offset
#     alpha = Link Twist
#     r = Link Length
#     d = Link Offset
    
def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    a4 = float(input("a_4 Link [mm]>>>"))
    return a1, a2, a3, a4

def defineJoints():
    d_1 = float(input("Prismatic Joint 1 [mm]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    theta_3 = float(input("Revolute Joint 3 [deg]>>>"))
    return d_1, theta_2, theta_3

def dhMatrix(theta, alpha, radius, distance):
    return np.matrix([
		[math.cos(theta), -math.sin(theta)*math.cos(alpha), math.sin(theta)*math.sin(alpha), radius*math.cos(theta)],
        [math.sin(theta), math.cos(theta)*math.cos(alpha), -math.cos(theta)*math.sin(alpha), radius*math.sin(theta)],
        [0, math.sin(alpha), math.cos(alpha), distance],
        [0,0,0,1],		
	])
    
def convert_to_meters(mm):
    return mm / 100

def convert_to_radians(deg):
    return deg * (math.pi/180)


a1, a2, a3, a4 = defineLinks()
a1 = convert_to_meters(a1)
a2 = convert_to_meters(a2)
a3 = convert_to_meters(a3)
a4 = convert_to_meters(a4)
d1, theta2, theta3 = defineJoints()
d1 = convert_to_meters(d1)
theta2 = convert_to_radians(theta2)
theta3 = convert_to_radians(theta3)

paramteric_table = [[0,0,0,a1+d1],
                    [theta2, 0, a2, 0],
                    [theta3, 0, a4, a3],
                    ]

htm = {}

for i in range(3):
	htm[i] = dhMatrix(paramteric_table[i][0], paramteric_table[i][1], paramteric_table[i][2], paramteric_table[i][3])


for i,j in htm.items():
    print(i, j)
    
result = np.dot(np.dot(htm[0], htm[1]), htm[2])

print(result)
