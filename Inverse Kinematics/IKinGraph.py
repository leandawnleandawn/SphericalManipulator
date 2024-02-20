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

a1, a2, a3, a4 = defineJoints()
x_03, y_03, z_03 = defineJoints()

phi2 = np.arctan(y_03/x_03)
