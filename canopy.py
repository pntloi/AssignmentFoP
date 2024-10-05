'''
canopy.py - module of files for canopy simulations

Student Name: Nguyen Trung Loi Pham
Student ID: 22317009


'''
import numpy as np
import math
from matplotlib.patches import Circle, Ellipse, Polygon, Rectangle

# 1.1 code ref
class Land():
    # Constructor of the class Land
    def __init__(self, x_lim=180, y_lim=180, land_temp=25, road_temp=25, road_color="gray", residential_area_color="sandybrown", park_color="lightgreen"):
        self.x_lim = x_lim # x limit of the land
        self.y_lim = y_lim # y limit of the land
        self.road_color = road_color 
        self.residential_area_color = residential_area_color
        self.park_color = park_color
        self.land_temp = land_temp
        self.road_temp = road_temp
        self.generate()
    
    # 1.1.1 code ref
    ## Input: name of the component, their amounts
    def init_components(self, name, nb):
        # Number of objects
        count = 0
        # Create instances
        while 1:
            if name == "WorkOffice":
                obj = WorkOffice(self.residential_area)
            elif name == "SmallHouse":
                obj = SmallHouse(self.residential_area)
            elif name == "Tree":
                obj = Tree(self.park)
            pointer = 0
            if name in ["WorkOffice", "SmallHouse"]:
                for o in self.houses:
                    # d is the distance between 2 houses
                    ## The formula to calculate the distance between two center of two houses
                    d = math.sqrt(((o.x + o.width/2) - (obj.x + obj.width/2))**2 + ((o.y + o.height/2) - (obj.y + obj.height/2))**2)
                    ## The distance of two houses must be higher than the total space between 2 center of the two houses
                    if d < (o.circular_space + obj.circular_space):
                        break
                    # Loop through the houses list
                    if pointer != (len(self.houses) - 1):
                        pointer += 1
                    else:   
                        count += 1
                        self.houses.append(obj)
                # If there is no houses in the list -> add house
                if not self.houses:
                    count += 1
                    self.houses.append(obj)
                    print(f"The temp of {name} is {obj.temp} degree")
            elif name == "Tree":
                for o in self.trees:
                    # d is the distance between 2 trees
                    ## The formula to calculate the distance between two center of two trees
                    d = math.sqrt(((o.x + o.width/2) - (obj.x + obj.width/2))**2 + ((o.y + o.height/2) - (obj.y + obj.height/2))**2)
                    ## The distance of two trees must be higher than the total space between 2 center of the two trees
                    if d < (o.circular_space + obj.circular_space):
                        break
                    # Loop through the trees list
                    if pointer != (len(self.trees) - 1):
                        pointer += 1
                    else:
                        count += 1
                        self.trees.append(obj)
                # If there is no trees in the list -> add tree
                if not self.trees:
                    count += 1
                    self.trees.append(obj)
                    print(f"The temp of {name} is {obj.temp} degree")
            # Stop condition
            if count == nb:
                break
            
    # 1.1.2 code ref
    ## Input: number of big houses/small houses/trees
    def init_objects(self, small_house_nb, big_house_nb, tree_nb):
        self.houses = [] 
        self.trees = []
        
        self.init_components("WorkOffice", big_house_nb)
        self.init_components("SmallHouse", small_house_nb)
        self.init_components("Tree", tree_nb)

    # 1.1.3 code ref
    ## Topleft/topright/bottomright/bottomleft of the park
    def _generate_park(self):
        self.park = {"tl": (self.road["tr"][0] + 1, 0),
                    "tr": (self.x_lim, 0),
                    "br": (self.x_lim, self.y_lim),
                    "bl": (self.road["br"][0] + 1, self.y_lim)}

    # 1.1.4 code ref
    ## Topleft/topright/bottomright/bottomleft of the residential area
    def _generate_residential_area(self):
        self.residential_area = {"tl": (0, 0),
                                "tr": (self.road["tl"][0] - 1, 0),
                                "br": (self.road["bl"][0] - 1, self.y_lim),
                                "bl": (0, self.y_lim)}

    # 1.1.5 code ref
    ## Generate road based on a random angle
    def _generate_road(self):
        angle = np.array((np.random.rand() - 0.5)*np.pi/6 + np.pi/2)
        x_road_range = round((np.random.rand()*0.1 + 0.1)*self.x_lim)
        if x_road_range % 2 == 0:
            x_road_range += 1
        x_road_begin = round(np.random.rand()*10)
        x_road_top = [self.x_lim//2 - x_road_begin, self.x_lim//2 - x_road_begin + x_road_range]
        x_road_bottom = x_road_top.copy()
        for i in range(len(x_road_bottom)):
            x_road_bottom[i] += self.y_lim/np.tan(angle)
        self.road = {"tl": (x_road_top[0], 0),
                    "tr": (x_road_top[1], 0),
                    "br": (round(x_road_bottom[1]), self.y_lim),
                    "bl": (round(x_road_bottom[0]), self.y_lim)}

    # 1.1.6 code ref
    ## Generate map's road/park/residential area
    def generate(self):
        self._generate_road()
        self._generate_park()
        self._generate_residential_area()
    
    # 1.1.7 code ref
    ## Using attribute in 1.1.3, 1.1.4, 1.1.5 to plot thermal map
    def plot_thermal_objects(self, obj_name, axis, ScalarMappable):
        obj = getattr(self, obj_name)
        if obj_name == "road":
            temp = self.road_temp
        else:
            temp = self.land_temp
            
        temp_as_cmap = (temp - ScalarMappable.norm.vmin)/ScalarMappable.norm.vmax
        coors_as_poly = list(obj.values())
        if obj_name == "road":
            axis.add_patch(Polygon(coors_as_poly,
                                edgecolor="w", linestyle="--", linewidth=1,
                                facecolor=ScalarMappable.get_cmap()(temp_as_cmap)))
            
        else:
            axis.add_patch(Polygon(coors_as_poly, fill=True, color=ScalarMappable.get_cmap()(temp)))
        return axis
    
    # 1.1.8 code ref
    ## Using attribute in 1.1.3, 1.1.4, 1.1.5 to plot the road RGB map
    def _plot_road(self, axis):
        axis = self._plot_area("road", self.road_color, axis)
        # Middle break line of the road
        x_mid = [(self.road["tl"][0] + self.road["tr"][0])//2, (self.road["bl"][0] + self.road["br"][0])//2]
        y_mid = [0, self.y_lim]

        x_left_road = [self.road["tl"][0], self.road["bl"][0]]
        y_left_road = [0, self.y_lim]
        x_right_road = [self.road["tr"][0], self.road["br"][0]]
        y_right_road = [0, self.y_lim]

        axis.plot(x_mid, y_mid, '--', color="white")
        axis.plot(x_left_road, y_left_road, color="black")
        axis.plot(x_right_road, y_right_road, color="black")
        return axis

    # 1.1.9 code ref
    ## Use to plot residential area/park area
    def _plot_area(self, obj_name, obj_color, axis):
        obj = getattr(self, obj_name)
        coors_as_poly = list(obj.values())
        axis.add_patch(Polygon(coors_as_poly, fill=True, color=obj_color))
        return axis

    # 1.1.10 code ref
    ## Plot the areas and the components into the RGB map
    def plot_RGB(self, axis):
        axis = self._plot_road(axis)
        axis = self._plot_area("residential_area", self.residential_area_color, axis)
        axis = self._plot_area("park", self.park_color, axis)
        if self.houses or self.trees:
            for o in (self.houses + self.trees):
                axis = o.plot_RGB(axis)
        else:
            print("No houses or trees have been created yet.")
        return axis 

    # 1.1.11 code ref
    ## Plot the areas and the components into the map
    def plot_thermal(self, axis, ScalarMappable):
        axis = self.plot_thermal_objects("road", axis, ScalarMappable)
        axis = self.plot_thermal_objects("residential_area", axis, ScalarMappable)
        axis = self.plot_thermal_objects("park", axis, ScalarMappable)
        if self.houses or self.trees:
            for o in (self.houses + self.trees):
                axis = o.plot_thermal(axis, ScalarMappable)
        else:
            print("No houses or trees have been created yet.")
        return axis
    
    # 2.1 code ref
    ## Initial temp: 25 degrees
    ## 29C at 8 oclock, 37C at 12 oclock, 25C at 0 oclock
    def env_update(self, env_time):
        temp_clock = np.array([0.5,]*8 + [2,]*4 + [-1,]*12)
        time_0 = 0
        temp_0 = 25

        self.land_temp = round(temp_0 + temp_clock[:(env_time - time_0)].sum())
        self.road_temp = self.land_temp

        if self.houses or self.trees:
            for o in (self.houses + self.trees):
                o.env_update(self.land_temp, env_time)
    
    def __str__(self):
        print(f"The temperature is {self.land_temp} degree. And the width of the land is {self.x_lim} meters and the height of the land is {self.y_lim} meters")

# 1.2 code ref
class StaticObject():
    def __init__(self, size=[10, 10], color="k", temp=24):
        self.color = color
        self.temp = temp
        self.width = size[0]
        self.height = size[1]
        # Calculate the radius of the circle around the obj 
        self.circular_space = math.sqrt((self.width/2)**2 + (self.height/2)**2)
# 1.3 code ref
class House(StaticObject):
    def __init__(self, area, size=[10, 10], color="k", temp=24):
        super().__init__(size, color, temp)
        self._init_pos(area)
    # 1.3.1 code ref
    def _init_pos(self, area):
        A = (area["tr"][1] - area["br"][1])/(area["tr"][0] - area["br"][0])
        b = area["tr"][1] - A*area["tr"][0]
        
        x_min = area["tl"][0]
        x_max = area["tr"][0] if area["tr"][0] >= area["br"][0] else area["br"][0]
        
        y_min = area["tr"][1]
        y_max = area["br"][1]
        
        while 1:
            x = np.random.randint(x_min, x_max - self.width)
            y = np.random.randint(y_min, y_max - self.height)
            x_circle = x + self.width/2
            y_circle = y + self.height/2
            dist_bound = (A*x_circle - y_circle + b)/math.sqrt(A**2 + 1)
            if (((dist_bound < 0 and A > 0) or (dist_bound > 0 and A < 0)) and
                abs(dist_bound) > self.circular_space):
                break
        self.x = x
        self.y = y
        
    # 1.3.2 code ref
    def plot_RGB(self, axis):
        axis.add_patch(Rectangle((self.x, self.y), self.width, self.height, fill=True, color=self.color))
        return axis
    
    # 1.3.3 code ref
    def plot_thermal(self, axis, ScalarMappable):
        temp_as_cmap = (self.temp - ScalarMappable.norm.vmin)/ScalarMappable.norm.vmax
        axis.add_patch(Rectangle((self.x, self.y), self.width, self.height,
                                edgecolor="w", linestyle="--", linewidth=1,
                                facecolor=ScalarMappable.get_cmap()(temp_as_cmap)))
        return axis

# 1.4 code ref
class WorkOffice(House):
    def __init__(self, area, size=[15, 30], color="m", temp=25, airCond=24):
        super().__init__(area, size, color, temp)
        self.airCond = airCond
    
    # 2.2 code ref
    ## If the temperature of the environment more than 26, and in the working hours(8AM to 5PM) 
    ## -> the temp of the building = temp of the air cond
    def env_update(self, env_temp, env_time):
        if env_temp > 28 & env_time > 8 & env_time < 17:
            self.temp = self.airCond
        else:
            self.temp = env_temp
    
    def __str__(self):
        if self.airCond == True:
            print(f"The AC is on. The temperature of the building is {self.temp}")
        else:
            print(f"No one in the office, and the AC is off. The temperature of the building is {self.temp}")

# 1.5 code ref
class SmallHouse(House):
    def __init__(self, area, size=[10, 10], color="c", temp=25):
        super().__init__(area, size, color, temp)

    # 2.3 code ref
    # Small house don't have air cond. 
    ## When the temperature of the environment > 29 -> The house cooler 2 degrees than the env
    ## When the temperature of the environment < 22 -> The house warmer 0.5 degrees than the env
    def env_update(self, env_temp, env_time):
        if env_temp > 29:
            self.temp = env_temp - 2
        elif env_temp < 22:
            self.temp = env_temp + 0.5
        else:
            self.temp = env_temp

    def __str__(self):
        return f"The temperature of the building is {self.temp}"

# 1.6 code ref
class Tree(StaticObject):
    def __init__(self, area, size=[3, 3], color="g", temp=25):
        super().__init__(size, color, temp)
        self._init_pos(area)
    # 1.6.1 code ref
    def _init_pos(self, area):
        # 
        A = (area["tl"][1] - area["bl"][1])/(area["tl"][0] - area["bl"][0])
        b = area["tl"][1] - A*area["tl"][0]
        
        x_min = area["tl"][0] if area["tl"][0] >= area["bl"][0] else area["bl"][0]
        x_max = area["tr"][0]
        
        y_min = area["tr"][1]
        y_max = area["br"][1]
        
        while 1:
            x = np.random.randint(x_min, x_max - self.width)
            y = np.random.randint(y_min, y_max - self.height)
            x_circle = x + self.width/2
            y_circle = y + self.height/2
            dist_bound = (A*x_circle - y_circle + b)/math.sqrt(A**2 + 1)
            if (((dist_bound < 0 and A < 0) or (dist_bound > 0 and A > 0)) and
                abs(dist_bound) > self.circular_space):
                break
        self.x = x
        self.y = y
    
    # 
    ## If the temp of the environment > 28 the tree can cool themself, their temp reduce by 3 degree
    ## If the temp of the environment < 22 the tree can warm themself, their temp increase by 2 degree
    def env_update(self, env_temp, env_time):
        if env_temp > 28:
            self.temp = env_temp - 2
        elif env_temp < 22:
            self.temp = env_temp + 2
        else:
            self.temp = env_temp


    # 1.6.2 code ref
    def plot_RGB(self, axis):
        if self.width != self.height:
            axis.add_patch(Ellipse((self.x + self.width/2, self.y + self.height/2), self.width, self.height, fill=True, color=self.color))
        else:
            axis.add_patch(Circle((self.x + self.width/2, self.y + self.height/2), radius=self.width, fill=True, color=self.color))
        return axis
    # 1.6.3 code ref
    def plot_thermal(self, axis, ScalarMappable):
        temp_as_cmap = (self.temp - ScalarMappable.norm.vmin)/ScalarMappable.norm.vmax
        if self.width != self.height:
            axis.add_patch(Ellipse((self.x + self.width/2, self.y + self.height/2), self.width, self.height,
                                edgecolor="w", linestyle="--", linewidth=1,
                                facecolor=ScalarMappable.get_cmap()(temp_as_cmap)))
        else:
            axis.add_patch(Circle((self.x + self.width/2, self.y + self.height/2), radius=self.width,
                                edgecolor="w", linestyle="--", linewidth=1,
                                facecolor=ScalarMappable.get_cmap()(temp_as_cmap)))
        return axis

    def __str__(self):
        return f"The temperature of the tree is {self.temp}"