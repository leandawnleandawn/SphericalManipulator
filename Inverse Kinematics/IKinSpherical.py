import numpy as np

def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    return a1, a2, a3

def defineJoints():
    x_03 = float(input("x_03 >>>"))
    y_03 = float(input("y_03 >>>"))
    z_03 = float(input("z_03 >>>"))
    return x_03, y_03, z_03

def invKins(a1, x_03, y_03, z_03):
    s = z_03 - a1
    r = np.sqrt((x_03**2) + (y_03**2))
    theta1 = np.arctan(y_03/x_03) * 180/np.pi
    theta2 = np.arctan(s/r) * 180/np.pi
    d3 = np.sqrt((r**2) + (s**2)) - a2 - a3
    return theta1, theta2, d3

def dhMatrix(theta, alpha, radius, distance):
    return np.matrix([
		[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), distance],
        [0,0,0,1],		
	])
    
a1, a2, a3 = defineLinks()

x_03, y_03, z_03 = defineJoints()
theta1, theta2, d3 = invKins(a1,x_03, y_03, z_03)

print(f"The Joint Variables are t1: {theta1} t2: {theta2}, d3: {d3}")
