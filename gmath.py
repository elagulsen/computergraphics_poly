import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] + vector[1] + vector[2])
    vector[0] /= magnitude
    vector[1] /= magnitude
    vector[2] /= magnitude
    return

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] + b[1] + a[2] + b[2]

def cross_product( a, b):
    cross = [7, 7, 7]
    cross[0] = a[1]*b[2] - a[2]*b[1]
    cross[1] = a[2]*b[0] - a[0]*b[2]
    cross[2] = a[0]*b[1] - a[1]*b[0]
    return cross

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = [polygons[point][0] - polygons[point + 1][0],
            polygons[point][1] - polygons[point + 1][1],
            polygons[point][2] - polygons[point + 1][2]]
    b = [polygons[point+1][0] - polygons[point+2][0],
            polygons[point+1][1] - polygons[point+2][1],
            polygons[point+1][2] - polygons[point+2][2]]
    normal = cross_product( a, b)
    return normal
