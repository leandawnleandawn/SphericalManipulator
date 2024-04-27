import numpy as np
import sympy as syp

def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    return a1, a2, a3

def defineJoints():
    theta_1 = float(input("Revolute Joint 1 [deg]>>>"))
    theta_2 = float(input("Revolute Joint 2 [deg]>>>"))
    d_3 = float(input("Prismatic Joint 3 [mm]>>"))
    return theta_1, theta_2, d_3

def dhMatrix(theta, alpha, radius, distance):
    return np.array([
		[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), distance],
        [0,0,0,1],		
	])
    
def convert_to_meters(mm):
    return mm / 100

def convert_to_radians(deg):
    return deg * (np.pi/180)


a1, a2, a3 = defineLinks()
theta1, theta2, d3 = defineJoints()
theta1 = convert_to_radians(theta1)
theta2 = convert_to_radians(theta2)

# Take Note: This is derived from the Denavit Hartenberg Parametric Table in columns of 
# Theta, Alpha, R, and D

paramteric_table = [[theta1,np.pi/2,0,a1],
                    [np.pi/2 + theta2, np.pi/2, 0, 0],
                    [0, 0, 0, a2+a3+d3],
                    ]

htm = {}

for i in range(3):
	htm[i] = dhMatrix(paramteric_table[i][0], paramteric_table[i][1], paramteric_table[i][2], paramteric_table[i][3])

for i,j in htm.items():
    print(f"HTM # {i+1}")
    print(j, 2)
    
result = np.dot(np.dot(htm[0], htm[1]), htm[2])
print("H0_3")
print(result, 2)


print("Storing the following values in HTM Vales")

H0_1 = htm[0]
H1_2 = htm[1]
H0_2 = np.dot(htm[0], htm[1])
H2_3 = htm[2]
H0_3 = np.dot(np.dot(htm[0], htm[1]), htm[2])


# Creating the following Jacobian


# Revolute 1

R0_0 = np.identity(3)
z0_1 = np.array([[0],[0],[1]])
d0_3 = d0_3 = H0_3[0:3, 3]
d0_0 = 0

# Revolute 2
R0_1 = H0_1[0:3, 0:3]
d0_3 = H0_3[0:3, 3]
d0_1 = H0_1[0:3, 3]

# Prismatic 3
R0_2 = H0_2[0:3, 0:3]
z0_0 = np.zeros((3,1))


Jv_1 = np.cross(np.dot(R0_0, z0_1), (d0_3-d0_0), axis = 0)
Jw_1 = np.dot(R0_0, z0_1)


Jv_2 = np.cross(np.dot(R0_1, z0_1), (d0_3-d0_1), axis = 0)
Jw_2 = np.dot(R0_1, z0_1)

Jv_3 = np.dot(R0_2, z0_1)
Jw_3 = z0_0

Jv = np.concatenate([Jv_1, Jv_2, Jv_3], 1)

Jw = np.concatenate([Jw_1, Jw_2, Jw_3], 1)

J = np.concatenate([Jv, Jw], 0)

print(J)

# Creating the following Unknown Variables

t = syp.Symbol("t")

x = syp.Function("x")
y=  syp.Function("y")
z = syp.Function("z")
theta_x = syp.Function("theta_x")
theta_y = syp.Function("theta_y")
theta_z = syp.Function("theta_z")

theta_1 = syp.Function("theta_1")
theta_2 = syp.Function("theta_2")
d_3 = syp.Function("d_3")


joint_variables = syp.Matrix([[syp.diff(theta_1(t))], [syp.diff(theta_2(t))], [syp.diff(d_3(t))]])
position_variables = syp.Matrix([[syp.diff(x(t))], [syp.diff(y(t))], [syp.diff(z(t))], [syp.diff(theta_x(t))], [syp.diff(theta_y(t))], [syp.diff(theta_z(t))]])
syp.init_printing()
print(J)
Jacobian_matrix = syp.Eq(position_variables, J*joint_variables)


print(syp.pretty(Jacobian_matrix))

singularity = np.linalg.det(Jv)

print(singularity)

inverseJacobian = np.linalg.inv(Jv)

print(inverseJacobian)