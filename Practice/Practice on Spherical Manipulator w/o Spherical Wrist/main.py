import math
from roboticstoolbox import SerialLink, PrismaticDH, RevoluteDH


a1 = 0.3 # 300mm
a2 = 0.15 # 300mm
a3 = 0.15 # 500mm


H01 = RevoluteDH(a1, 0, math.pi/2, 0, [-math.pi/2, math.pi/2])
H12 = RevoluteDH(0, 0, math.pi/2, math.pi/2, [-math.pi/2, math.pi/2])
H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.05])


sphericalManipulator = SerialLink([H01, H12, H23])

print(sphericalManipulator)
sphericalManipulator.teach([0,0,0])
