import roboticstoolbox as rtb
from roboticstoolbox import RevoluteDH, PrismaticDH, SerialLink, DHRobot
import swift
import numpy as np
import spatialmath as sm

env = swift.Swift()
env.launch(realtime=True)


a1 = 0.3 # 300mm
a2 = 0.15 # 300mm
a3 = 0.15 # 500mm


H01 = RevoluteDH(a1, 0, np.pi/2, 0, [-np.pi/2, np.pi/2])
H12 = RevoluteDH(0, 0, np.pi/2, np.pi/2, [-np.pi/2, np.pi/2])
H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.05])


sphericalManipulator = DHRobot([H01, H12, H23])
sphericalManipulator.plot([0,0,0])