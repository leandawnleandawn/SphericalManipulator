import math
from roboticstoolbox import SerialLink, PrismaticDH, RevoluteDH


a1 = 0.3 # 300mm
a2 = 0.15 # 300mm
a3 = 0.15 # 500mm
a4 = 0.002 # 20mm
a5 = 0.002 # 20mm
a6 = 0.001 # 20mm


H01 = RevoluteDH(a1, 0, math.pi/2, 0, [-math.pi/2, math.pi/2])
H12 = RevoluteDH(0, 0, math.pi/2, math.pi/2, [-math.pi/2, math.pi/2])
H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.05])
H34 = RevoluteDH(a4,0, (math.pi*3)/2, 0,[-math.pi/2, math.pi/2])
H45 = RevoluteDH(0,0, (math.pi)/2, 0,[-math.pi/2, math.pi/2])
H56 = RevoluteDH(a5+a6,0, 0, 0, [-math.pi/2, math.pi/2])


sphericalManipulator = SerialLink([H01, H12, H23, H34, H45, H56])

print(sphericalManipulator)
sphericalManipulator.teach([0,0,0,0,0,0])
