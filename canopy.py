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
    def __init__(self, x_lim=180, y_lim=180, colour=None):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.colour = ["red", "green", "blue"]
        self.initialTemp = 25
    
    def generate_land(self):
        land = np.zeros((self.y_lim, self.x_lim))
        return land
    
    def generate_residential_area(self, axis):
        width = (self.x_lim)//2 - 10
        for part in range(0, self.y_lim, 3):
            if part % 2 == 1:
                axis.add_patch(Rectangle((0, part), width, 10, 
                                fill=True,
                                color=self.colour[2],
                                linewidth=3))
            else:
                width -= 0.5
                axis.add_patch(Rectangle((0, part), width, 10, 
                                fill=True,
                                color=self.colour[2],
                                linewidth=3))

        
    def generate_park(self, axis):
        width = (self.x_lim)//2 - 10
        starting_point = (self.x_lim)//2 + 10
        for part in range(self.y_lim + 1, 0, -3):
            if part % 2 == 1:
                axis.add_patch(Rectangle((starting_point, part), width, 10, 
                                fill=True,
                                color=self.colour[1],
                                linewidth=3))
            else:
                width -= 0.5
                starting_point += 0.5
                axis.add_patch(Rectangle((starting_point, part), width, 10, 
                                fill=True,
                                color=self.colour[1],
                                linewidth=3))
        
    def generate_road_line(self, axis):
        road = Road(self.x_lim, self.y_lim, axis, 25)
        road.draw_line()
        
        
    def __str__(self):
        return f"The initial temperature is {self.initialTemp} degree. And the width of the land is {self.x_lim} meters and the height of the land is {self.y_lim} meters"
        
class StaticObject():
    myclass = None
    colour = "green"
    size = 3
    type = None
    name = None
    def __init__(self, x, y, axis, size, colour, objTemp, envTemp=25):
        self.x = x
        self.y = y
        self.axis = axis
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
        area[self.x:self.x + self.size, self.y:self.y + self.size] = self.type


class House(StaticObject):
    myclass = "House"
    def __init__(self, x, y, axis, size, colour, objTemp, envTemp, airCond=False):
        super().__init__(x, y, axis, size, colour, objTemp, envTemp)
        
    def draw_house(self):
        pass

class WorkOffice(House):
    myclass = "WorkOffice"
    def __init__(self, x, y, axis, width, height, colour, objTemp, envTemp, airCond, time):
        super().__init__(x, y, axis, colour, objTemp, envTemp, airCond)
        self.width = width
        self.height = height
        self.time = time
    
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
    type = 2
    def __init__(self, x, y, axis, size, colour, objTemp, envTemp, airCond):
        super().__init__(x, y, axis, size, colour, objTemp, envTemp, airCond)
    
    def cal_sh_temp(self):
        if self.envTemp > 29:
            self.objTemp = self.envTemp - 2
        elif self.envTemp < 22:
            self.objTemp = self.envTemp + 0.5
    
    def add_small_house(self, numSmallHouse):
        for sh in range(numSmallHouse):
            self.axis[self.x:self.x + self.size, self.y:self.y + self.size] = self.type
            
            
            
            
    def __str__(self):
        return f"The temperature of the building is {self.objTemp}"
    


class Tree(StaticObject):
    myclass = "Tree"
    pass

class Road():
    myclass = "Road"
    type = 3
    def __init__(self, x_lim, y_lim, axis, objTemp):
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.axis = axis
        self.objTemp = objTemp
        
    def draw_line(self):
            
        x_rl = [self.x_lim//2 + 8, self.x_lim//2 - 6]
        y_rl = [0, self.y_lim]
        
        x_left_road = [self.x_lim//2 - 9, self.x_lim//2 - 23]
        y_left_road = [0, self.y_lim]
        
        x_right_road = [self.x_lim//2 + 25, self.x_lim//2 + 10]
        y_right_road = [0, self.y_lim]
        
        self.axis.plot(x_rl, y_rl, 'g--', color="white")
        self.axis.plot(x_left_road, y_left_road, color="black")
        self.axis.plot(x_right_road, y_right_road, color="black")
        
        
        
class Car(StaticObject):
    pass


