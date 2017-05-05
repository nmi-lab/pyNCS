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

c0 = nsetup.chips['dynapse_u0']
c1 = nsetup.chips['dynapse_u1']
c2 = nsetup.chips['dynapse_u2']
c3 = nsetup.chips['dynapse_u3']


if __name__ == '__main__':
    pass

