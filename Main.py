import random
import numpy as np
import matplotlib.pyplot as plt
from canopy import *
from matplotlib.patches import Rectangle


#  this is the func that call all other stuffs to get things done
def main():
    # define the w and h parameters
    
    fig, axis = plt.subplots(ncols=2)
    
    ax1, ax2 = axis
    
    land_RGB = Land()
    landview_RGB = land_RGB.generate_land()
    
    land_RGB.generate_park(ax1) # Generate park
    land_RGB.generate_residential_area(ax1) # Generate residential area
    
    land_RGB.generate_road_line(ax1)
    
    
    im1 = ax1.imshow(landview_RGB)
    fig.colorbar(im1)
    
    plt.show()

# This runs the Python file (in case u dont know type python3 file name)
if __name__ == "__main__":
    main()