'''
canopy.py - module of files for canopy simulations

Student Name: 
Student ID  :


'''
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def swap_coords(x, y):
    return (y, x)

class Land():
    def __init__(self, x_lim, y_lim, colour=None):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.colour = colour
    
    def generate_land(self):
        land = np.zeros((self.y_lim, self.x_lim))
        return land
    
    def generate_park(self, axis):
        width = (self.x_lim)//2 - 10
        height = self.y_lim
        axis.add_patch(Rectangle((0, 0), width, height, 
                        fill=True,
                        color="green",
                        linewidth=2))
        
    def generate_residential_area(self, axis):
        width = (self.x_lim)//2 - 10
        height = self.y_lim
        axis.add_patch(Rectangle(((self.x_lim)//2 + 10, 0), width, height, 
                        fill=True,
                        color="blue",
                        linewidth=2))
        
        
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