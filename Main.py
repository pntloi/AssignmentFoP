import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from canopy import *


SMALL_HOUSE_NB = 3
BIG_HOUSE_NB = 2
TREE_NB = 10

#  this is the func that call all other stuffs to get things done
def main():
    # define the w and h parameters
    
    fig, axis = plt.subplots(ncols=2)
    ax1, ax2 = axis
    
    land = Land()
    land.init_objects(SMALL_HOUSE_NB, BIG_HOUSE_NB, TREE_NB)
    ax1 = land.plot(ax1)
    ax1.set_title("RGB view")
    ax1.set_xlim([0, land.x_lim])
    ax1.set_ylim([0, land.y_lim])

    land.env_update(12)

    # Set up thermal view
    t_min = 20
    t_max = 30
    cmap = "hot"
    norm = Normalize(vmin=t_min, vmax=t_max)
    cmap = cm.get_cmap(cmap)
    sm = cm.ScalarMappable(norm=norm, cmap=cmap)
    ax2 = land.plot_thermal(ax2, sm)
    ax2.set_title("Thermal view")
    ax2.set_xlim([0, land.x_lim])
    ax2.set_ylim([0, land.y_lim])
    plt.colorbar(sm, ax = ax2)
    plt.show()

# This runs the Python file (in case u dont know type python3 file name)
if __name__ == "__main__":
    main()