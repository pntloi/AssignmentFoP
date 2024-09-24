'''
canopy.py - module of files for canopy simulations

Student Name: 
Student ID  :


'''
import random
import numpy as np
import matplotlib.pyplot as plt

def swap_coords(x, y):
    return (y, x)

class StaticObject():
    myclass = None
    colour = "green"
    size = 3
    type = None
    name = None
    def __init__(self, x1, y1, x2, y2, size, colour, objTemp):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.size = size
        self.colour = colour
        self.objTemp = objTemp
        self.shape = None
        
    def plot_obj_name(self, axis):
        x = (self.x1 + self.x2) // 2
        y = (self.y1 + self.y2) // 2
        x, y = swap_coords(x, y)
        axis.text(x, y, f"{self.name}", color="Black")
        
    def draw_obj(self, area):
        area[self.x1:self.x2, self.y1:self.y2] = self.type


class Road(StaticObject):
    pass

class Tree(StaticObject):
    pass

class House(StaticObject):
    pass