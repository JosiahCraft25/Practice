#Scratch pad for random stuff

import math
def circle_or_square(rad, area):
    circ = (2 * (3.14*rad))**2
    param = (math.sqrt(area)*4)

    if (circ > param):
        return(True)
    else:
        return(False)
    
    