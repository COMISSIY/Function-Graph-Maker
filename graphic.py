import pygame
from math import *
pygame.init()

#System variables:

sc = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
widht, height = sc.get_width(), sc.get_height()
c_x, c_y = sc.get_width() // 2, sc.get_height() // 2


#Graphic parameter's:

x = -100 #param. x
size = 50 #grid and point size
func = "sin(x)" #math function


#Code:

def draw_graphic(points):
    for n, i in enumerate(points[2::], 1):
        pygame.draw.line(sc, (0, 255, 0), points[n-1], points[n])


def find_points(func, ox, size):
    points = []
    for x in range(-abs(ox), abs(ox)):
        y = eval(func)*-1
        points.append((c_x+x*size, c_y+y*size))
    return points
    

def draw_grid(size, rad):
    for x in range(size, widht, size):
        pygame.draw.line(sc, (255, 255, 255), [x, 0], [x, height], rad)
    for y in range(size, height, size):
        pygame.draw.line(sc, (255, 255, 255), [0, y], [widht, y], rad)


def draw_xy(size):
    pygame.draw.line(sc, (0, 0, 255), [c_x, 0], [c_x, height], size)
    pygame.draw.line(sc, (255, 0, 0), [0, c_y], [widht, c_y], size)


while True:
    [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
    clock.tick(10)
    sc.fill((0, 0, 0))
    draw_grid(size, 1)
    draw_xy(3)
    draw_graphic(find_points(func, x, size))
    pygame.display.update()