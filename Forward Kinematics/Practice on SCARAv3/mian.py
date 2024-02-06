
import numpy as np
import scipy as sp
import math
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
#		Laboratory 1: Forward Kinematics
#		Objective:
# 			To create and to manipulate the following joint variables, to move in a certain position
#		Preqrequisites Subjects:
# 			- Review the following Denavit Hartenberg Parametric Table
#		No more specifications on type of manipulator since it is a SCARA Manipulator 


a_1 = 0.06
a_2 = 0.07
a_3 = 0.03
a_4 = 0.05

SCARA_V3 = DHRobot([RevoluteDH(a_1,a_2,0, 0, qlim  = [(-90/180)*np.pi,(90/180)*np.pi]),
                    RevoluteDH(0,0,(3*np.pi)/2, np.pi/2, qlim  = [(-90/180)*np.pi,(90/180)*np.pi]),
                    PrismaticDH(0, 0, 0, a_3+a_4, qlim=[0,0.03])
                    ])

print(SCARA_V3)
SCARA_V3.teach([0,0,0])
