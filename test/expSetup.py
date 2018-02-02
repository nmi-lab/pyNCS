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

nsetup = build_setup()

U0 = nsetup.chips['U0']
U1 = nsetup.chips['U1']
U2 = nsetup.chips['U2']
U3 = nsetup.chips['U3']


if __name__ == '__main__':
    pass

