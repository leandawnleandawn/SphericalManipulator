import numpy as np
import roboticstoolbox as rtb
from roboticstoolbox import SerialLink, PrismaticDH, RevoluteDH 


def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    return a1, a2, a3

a1, a2, a3 = defineLinks()

H01 = RevoluteDH(a1, 0, np.pi/2, 0, [-np.pi/2, np.pi/2])
H12 = RevoluteDH(0, 0, np.pi/2, np.pi/2, [-np.pi/2, np.pi/2])
H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.05])


sphericalManipulator = SerialLink([H01, H12, H23])

print(sphericalManipulator)

def defineJoints():
    theta_1 = float(input("Revolute Joint 1 [deg]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    d_3 = float(input("Prismatic Joint 3 [mm]>>>"))
    return theta_1, theta_2, d_3

def invKins(a1, x_03, y_03, z_03):
    s = z_03 - a1
    r = np.sqrt((x_03**2) + (y_03**2))
    theta1 = np.arctan(y_03/x_03) * 180/np.pi
    theta2 = np.arctan(s/r) * 180/np.pi
    d3 = np.sqrt((r**2) + (s**2)) - a2 - a3
    return theta1, theta2, d3

def convert_to_meters(mm):
    return mm / 100

def convert_to_radians(deg):
    return deg * (np.pi/180)

conveyor_beltT1, conveyor_beltT2, conveyor_beltd3 = invKins(a1, 10, 0, 3)
box1T1, box1T2, box1d3 = invKins(a1, -5*np.sin(np.pi/4), -5*np.cos(np.pi/4), 2)

conveyor_beltT1 = convert_to_radians(conveyor_beltT1)
conveyor_beltT2 = convert_to_radians(conveyor_beltT2)
box1T1 = convert_to_radians(box1T1)
box1T2 = convert_to_radians(box1T2)


q0 = np.array([0, 0, 0])
q1 = np.array([conveyor_beltT1, conveyor_beltT2, conveyor_beltd3])
q2 = np.array([box1T1, box1T2, box1d3])

t = np.linspace(0, 20, num = 50)
traj1 = rtb.jtraj(q0, q1, t)
traj2 = rtb.jtraj(q1, q0, t)
traj3 = rtb.jtraj(q0, q2, t)
traj4 = rtb.jtraj(q2, q0, t)

print(traj1)

while True:
    sphericalManipulator.plot(traj1.s, limits = [-5, 30, -10, 10, 0, 30])
    sphericalManipulator.plot(traj2.s, limits = [-5, 30, -10, 10, 0, 30])
    sphericalManipulator.plot(traj3.s, limits = [-5, 30, -10, 10, 0, 30])
    sphericalManipulator.plot(traj4.s, limits = [-5, 30, -10, 10, 0, 30])