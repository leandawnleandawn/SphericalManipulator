import numpy as np

def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    a4 = float(input("a_4 Link [mm]>>>"))
    return a1, a2, a3, a4

def defineJoints():
    x_03 = float(input("x_03 >>>"))
    y_03 = float(input("y_03 >>>"))
    z_03 = float(input("z_03 >>>"))
    return x_03, y_03, z_03

def invKins(a1, a2, a3, a4, x_03, y_03, z_03):
    phi2 = np.arctan(y_03/x_03)*(180/np.pi)
    r1 = np.sqrt((x_03^2) + (y_03^2))
    phi1 = np.arccos((a4^2 - r1^2 - a2^2)/(-2*r1*a2))*(180/np.pi)
    theta2 = (phi2 - phi1)
    phi3 = np.arccos((r1^2 - a2^2 - a4^2)/(-2*a2*a4))*(180/np.pi)
    theta3 = 180 - phi3
    return theta2, theta3


a1, a2, a3, a4 = defineJoints()
x_03, y_03, z_03 = defineJoints()

invKins(a1, a2, a3, a4, x_03, y_03, z_03)



