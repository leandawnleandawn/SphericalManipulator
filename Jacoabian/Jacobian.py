import numpy as np
import sympy as syp



def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    a4 = float(input("a_4 Link [mm]>>>"))
    return a1, a2, a3, a4

def defineJoints():
    d_1 = float(input("Prismatic Joint 1 [mm]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    theta_3 = float(input("Revolute Joint 3 [deg]>>>"))
    return d_1, theta_2, theta_3

def dhMatrix(theta, alpha, radius, distance):
    return np.matrix([
		[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), distance],
        [0,0,0,1],		
	])
    
def convert_to_meters(mm):
    return mm / 100

def convert_to_radians(deg):
    return deg * (np.pi/180)


a1, a2, a3, a4 = defineLinks()
a1 = convert_to_meters(a1)
a2 = convert_to_meters(a2)
a3 = convert_to_meters(a3)
a4 = convert_to_meters(a4)
d1, theta2, theta3 = defineJoints()
d1 = convert_to_meters(d1)
theta2 = convert_to_radians(theta2)
theta3 = convert_to_radians(theta3)

# Take Note: This is derived from the Denavit Hartenberg Parametric Table in columns of 
# Theta, Alpha, R, and D
paramteric_table = [[0,0,0,a1+d1],
                    [theta2, 0, a2, 0],
                    [theta3, 0, a4, a3],
                    ]

htm = {}

for i in range(3):
	htm[i] = dhMatrix(paramteric_table[i][0], paramteric_table[i][1], paramteric_table[i][2], paramteric_table[i][3])

for i,j in htm.items():
    print(i, j)
    
result = np.dot(np.dot(htm[0], htm[1]), htm[2])

print(result)

print("Storing the following values in HTM Vales")

H0_1 = htm[0]
H1_2 = htm[1]
H0_2 = np.dot(htm[0], htm[1])
H2_3 = htm[2]
H0_3 = np.dot(np.dot(htm[0], htm[1]), htm[2])


# Creating the following Jacobian

#Prismatic 1
R0_0 = np.identity(3)
z0_1 = np.array([[0],[0],[1]])
z0_0 = np.zeros((3,1))
#Revolute 2
R0_1 = H0_1[0:3, 0:3]
d0_3 = H0_3[0:3, 3]
d0_1 = H0_1[0:3, 3]

#Revolute 3
R0_2 = H0_1[0:3, 0:3]
d0_2 = H0_2[0:3, 3]

#Creating the Following Jacobian

Jv_1 = np.dot(R0_0, z0_1)
Jw_1 = z0_0


Jv_2 = np.cross(np.dot(R0_1, z0_1), (d0_3-d0_1), axis = 0)
Jw_2 = np.dot(R0_1, z0_1)

Jv_3 = np.cross(np.dot(R0_2, z0_1), (d0_3-d0_2), axis = 0)
Jw_3 = np.dot(R0_2, z0_1)

Jv = np.concatenate([Jv_1, Jv_2, Jv_3], 1)

Jw = np.concatenate([Jw_1, Jw_2, Jw_3], 1)

J = np.concatenate([Jv, Jw], 0)

# Creating the following Unknown Variables

t = syp.Symbol("t")

x = syp.Function("x")
y=  syp.Function("y")
z = syp.Function("z")
theta_x = syp.Function("theta_x")
theta_y = syp.Function("theta_y")
theta_z = syp.Function("theta_z")

d1 = syp.Function("d_1")
theta_2 = syp.Function("theta_2")
theta_3 = syp.Function("theta_3")


q = syp.Matrix([[syp.diff(d1(t))], [syp.diff(theta_2(t))], [syp.diff(theta_3(t))]])
p = syp.Matrix([[syp.diff(x(t))], [syp.diff(y(t))], [syp.diff(z(t))], [syp.diff(theta_x(t))], [syp.diff(theta_y(t))], [syp.diff(theta_z(t))]])
syp.init_printing()
print(J)
Jacobian_matrix = syp.Eq(p, J*q)


print(syp.pretty(Jacobian_matrix))



