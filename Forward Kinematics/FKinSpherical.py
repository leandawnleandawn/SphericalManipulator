import numpy as np
# Exercise 1: Creating a Denavit Hartenberg Calculator given the Parameters
# Objective:
#     to solve and to create the Denavit Hartenberg Matrix to 
#     simplify the following Transformation of the Mechanical 
#     Manipulator (In this case, Spherical)

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
    return a1, a2, a3

def defineJoints():
    theta_1 = float(input("Revolute Joint 1 [deg]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    d_3 = float(input("Prismatic Joint 3 [mm]>>>"))
    return theta_1, theta_2, d_3

def dhMatrix(theta, alpha, radius, distance):
    return np.array([
		[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), distance],
        [0,0,0,1],		
	])
    
def convert_to_meters(mm):
    return mm / 100

def convert_to_radians(deg):
    return deg * (np.pi/180)


a1, a2, a3 = defineLinks()
theta1, theta2, d3 = defineJoints()
theta1 = convert_to_radians(theta1)
theta2 = convert_to_radians(theta2)

# Take Note: This is derived from the Denavit Hartenberg Parametric Table in columns of 
# Theta, Alpha, R, and D

paramteric_table = [[theta1,np.pi/2,0,a1],
                    [np.pi/2 + theta2, np.pi/2, 0, 0],
                    [0, 0, 0, a2+a3+d3],
                    ]

htm = {}

for i in range(3):
	htm[i] = dhMatrix(paramteric_table[i][0], paramteric_table[i][1], paramteric_table[i][2], paramteric_table[i][3])

for i,j in htm.items():
    print(f"HTM # {i+1}")
    print(np.round(j, 2))
    
result = np.dot(np.dot(htm[0], htm[1]), htm[2])
print("H0_3")
print(np.round(result, 2))
