from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 153, 255]
edges = []
polygons = []
transform = new_matrix()

parse_file( 'korbs', edges, polygons, transform, screen, color )
