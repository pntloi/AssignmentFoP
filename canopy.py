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
        self.colour = ["red", "green", "blue"]
        self.initialTemp = 25
    
    def generate_land(self):
        land = np.zeros((self.y_lim, self.x_lim))
        return land
    
    def generate_park(self, axis):
        width = (self.x_lim)//2 - 10
        height = self.y_lim
        axis.add_patch(Rectangle((0, 0), width, height, 
                        fill=True,
                        color=self.colour[1],
                        linewidth=2))
        
    def generate_residential_area(self, axis):
        width = (self.x_lim)//2 - 10
        height = self.y_lim
        axis.add_patch(Rectangle(((self.x_lim)//2 + 10, 0), width, height, 
                        fill=True,
                        color=self.colour[2],
                        linewidth=2))
        
    def __str__(self):
        return f"The initial temperature is {self.initialTemp} degree. And the width of the land is {self.x_lim} meters and the height of the land is {self.y_lim} meters"
        
class StaticObject():
    myclass = None
    colour = "green"
    size = 3
    type = None
    name = None
    def __init__(self, x1, y1, x2, y2, size, colour, objTemp, envTemp=25):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.size = size
        self.colour = colour
        self.objTemp = objTemp
        self.shape = None
        self.envTemp = envTemp
        
    def plot_obj_name(self, axis):
        x = (self.x1 + self.x2) // 2
        y = (self.y1 + self.y2) // 2
        x, y = swap_coords(x, y)
        axis.text(x, y, f"{self.name}", color="Black")
        
    def draw_obj(self, area):
        area[self.x1:self.x2, self.y1:self.y2] = self.type


class House(StaticObject):
    myclass = "House"
    def __init__(self, x1, y1, x2, y2, size, colour, objTemp, envTemp, airCond=False):
        super().__init__(x1, y1, x2, y2, size, colour, objTemp)
        
    def draw_house(self):
        pass

class WorkOffice(House):
    myclass = "WorkOffice"
    def __init__(self, x1, y1, x2, y2, size, colour, objTemp, envTemp, airCond, time):
        super().__init__(x1, y1, x2, y2, size, colour, objTemp, envTemp, airCond, time)
    
    def ac_on(self):
        if self.envTemp > 26 & self.time > 8 & self.time < 17:
            self.airCond = True
        else:
            self.airCond = False
    
    
    def __str__(self):
        if self.airCond == True:
            return f"The AC is on. The temperature of the building is {self.objTemp}"
        else:
            return f"No one in the office, and the AC is off. The temperature of the building is {self.objTemp}"
    
    

class SmallHouse(House):
    myclass = "SmallHouse"
    def __init__(self, x1, y1, x2, y2, size, colour, objTemp, envTemp, airCond):
        super().__init__(x1, y1, x2, y2, size, colour, objTemp, envTemp, airCond)
    
    def cal_sh_temp(self):
        if self.envTemp > 29:
            self.objTemp = self.envTemp - 2
        elif self.envTemp < 22:
            self.objTemp = self.envTemp + 0.5
    
    def __str__(self):
        return f"The temperature of the building is {self.objTemp}"
    


class Tree(StaticObject):
    myclass = "Tree"
    pass

class Road(StaticObject):
    myclass = "Road"
    type = 3
    def __init__(self, x, y, axis, colour, objTemp):
        super().__init__(colour, objTemp)
        axis[x//2, 0] = self.type
        
        
class Car(StaticObject):
    pass


