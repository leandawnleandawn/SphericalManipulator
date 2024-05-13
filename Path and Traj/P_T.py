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
sphericalManipulator.teach([0,0,0])

def defineJoints():
    theta_1 = float(input("Revolute Joint 1 [deg]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    d_3 = float(input("Prismatic Joint 3 [mm]>>>"))
    return theta_1, theta_2, d_3

theta_11, theta_21, d_31 = defineJoints()
theta_12, theta_22, d_32 = defineJoints()
theta_13, theta_23, d_33 = defineJoints()

q1 = np.array(theta_11, theta_21, d_31)
q2 = np.array(theta_12, theta_22, d_32)
q3 = np.array(theta_13, theta_23, d_33)


traj1 = rtb.jtraj(q1, q2, 20)
traj2 = rtb.jtraj(q2, q3, 20)
traj3 = rtb.jtraj(q3, q1, 20)


sphericalManipulator.plot(traj1)