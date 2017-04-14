import pyNCSre.pyST as pyST
import time,sys,random
import pyNCSre as pyNCS
import numpy as np
from pyNCSre.neurosetup import NeuroSetup
from pylab import *
import warnings

# C O N F I G # # # # # # # # # # # # # # # # # # # # # #

def build_setup(setupfile = 'setupfiles/dynapse_setuptype.xml'):
    nsetup = NeuroSetup(
            setupfile,
            offline=False)
    return nsetup

if __name__ == '__main__':
    nsetup = build_setup()
    out = nsetup.run(None, duration = 1000)
    out[1].raster_plot()
    show()

