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
    r1 = np.sqrt((x_03**2) + (y_03**2))
    phi1 = np.arccos((a4**2 - r1**2 - a2**2)/(-2*r1*a2))*(180/np.pi)
    theta2 = (phi2 - phi1)
    phi3 = np.arccos((r1**2 - a2**2 - a4**2)/(-2*a2*a4))*(180/np.pi)
    theta3 = 180 - phi3
    d1 = z_03 - a1 - a3
    return theta2, theta3, d1

def dhMatrix(theta, alpha, radius, distance):
    return np.matrix([
		[np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), radius*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), radius*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), distance],
        [0,0,0,1],		
	])
    
a1, a2, a3, a4 = defineLinks()
x_03, y_03, z_03 = defineJoints()
theta2, theta3, d1 = invKins(a1, a2, a3, a4, x_03, y_03, z_03)

print(f"The Joint Variables are: {np.around(d1, 3)}, {np.around(theta2, 3)}, {np.around(theta3, 3)}")

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