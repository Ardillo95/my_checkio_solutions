import numpy as np
import math

"""     EQUATIONS
    x1*x1 + y1*y1 = x1 * a + y1 * b + c
    x2*x2 + y2*y2 = x2 * a + y2 * b + c
    x3*x3 + y3*y3 = x3 * a + y3 * b + c
"""
    
def three_points_circle(data):
    
    # Coordinates for each point
    x1, x2, x3 = int(data[1]), int(data[7]), int(data[13])
    y1, y2, y3 = int(data[3]), int(data[9]), int(data[15])
    
    # This solve the system equations
    first = np.array([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]])
    second = np.array([x1*x1 + y1*y1, x2*x2 + y2*y2, x3*x3 + y3*y3])
    a, b, c = np.linalg.solve(first, second)
    
    # Getting values rounded
    d = round(math.sqrt(c + (a/2)*(a/2) + (b/2)*(b/2)), 2)
    a, b, c = round(a/2, 2), round(b/2, 2), round(c, 2)
    
    # Geting rid of zeros
    if (a*10) % 10 == 0:
        a = int(a)
    if (b*10) % 10 == 0:
        b = int(b)
    if (d*10) % 10 == 0:
        d = int(d)
        
    # Final equation
    sol = '(x' + str(-a) + ')^2+(y' + str(-b) + ')^2=' + str(d) + '^2'
    return sol
