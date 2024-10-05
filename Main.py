'''
main.py - main file for canopy simulations

Student Name: Nguyen Trung Loi Pham
Student ID: 22317009


'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
import matplotlib.colors as mcolors
from canopy import *
from wrapt_timeout_decorator import *


@timeout(5)
def create_view(SMALL_HOUSE_NB, WORKOFFICE_NB, TREE_NB, TIME):
    fig, axis = plt.subplots(ncols=2)
    ax1, ax2 = axis
    
    land = Land()
    land.init_objects(SMALL_HOUSE_NB, WORKOFFICE_NB, TREE_NB)
    
    ax1 = land.plot_RGB(ax1)
    ax1.set_title("RGB view")
    ax1.set_xlim([0, land.x_lim])
    ax1.set_ylim([0, land.y_lim])
    
    land.env_update(TIME)
    # Set up thermal view
    t_min = 20
    t_max = 35
    
    cmap = mcolors.LinearSegmentedColormap.from_list("", ["blue", "white", "yellow", "red"])
    norm = Normalize(vmin=t_min, vmax=t_max)
    cmap = cm.get_cmap(cmap)
    sm = cm.ScalarMappable(norm=norm, cmap=cmap)
    
    ax2 = land.plot_thermal(ax2, sm)
    ax2.set_title("Thermal view")
    ax2.set_xlim([0, land.x_lim])
    ax2.set_ylim([0, land.y_lim])
    
    plt.colorbar(sm, ax = ax2)
    plt.show(block=False)
    print(f"The time is {TIME} oclock")
    
    plt.pause(3)
    plt.close()
    

def input_data(name, var):
    if name == "SIMULATION_NB":
        var_name = "simulation"
    elif name == "SMALL_HOUSE_NB":
        var_name = "small houses"
    elif name == "WORKOFFICE_NB":
        var_name = "work offices"
    elif name == "TREE_NB":
        var_name = "trees"
    else:
        var_name = "time"    
    
    # Input the data
    if var_name == "time":
        while var < 0 or var > 23:
            try:
                var = int(input(f"Please enter the {var_name}: ")) 
            except:
                print(f"The {var_name} must between 0h to 24h. Please try again")
                var = int(input(f"Please enter the {var_name}: ")) 
    else:
        while var <= 0:
                try:
                    var = int(input(f"Please enter the number of {var_name}: "))
                except:
                    print(f"The number of {var_name} must be a positive integer. Please try again")
                    var = int(input(f"Please enter the {var_name}: "))
    return var

#  this is the func that call all other stuffs to get things done
def main():
    SIMULATION_NB = 0
    SMALL_HOUSE_NB = 0
    WORKOFFICE_NB = 0
    TREE_NB = 0
    time = -1
    
    try:
        # Input the number of simulation/smallhouse/workoffice/tree
        SIMULATION_NB = input_data("SIMULATION_NB", SIMULATION_NB)
        SMALL_HOUSE_NB = input_data("SMALL_HOUSE_NB", SMALL_HOUSE_NB)
        WORKOFFICE_NB = input_data("WORKOFFICE_NB", WORKOFFICE_NB)
        TREE_NB = input_data("TREE_NB", TREE_NB)
        time = input_data("TIME", time)
        
        # Create view
        for sim in range(SIMULATION_NB):
            create_view(SMALL_HOUSE_NB, WORKOFFICE_NB, TREE_NB, time)
            time += 1
            if time > 23:
                time = 0
            
        
    except TimeoutError as e:
        print(f"Not enough space on the map: {e}\n Please reduce the number of houses or trees")


# This runs the Python file (in case u dont know type python3 file name)
if __name__ == "__main__":
    main()