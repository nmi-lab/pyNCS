#!/bin/python
#-----------------------------------------------------------------------------
# File Name : expPop.py
# Author: Emre Neftci
#
# Creation Date : Thu 13 Apr 2017 03:40:23 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#----------------------------------------------------------------------------- 
from expSetup import *
nsetup = build_setup()
pop_exc=pyNCS.Population(name='core0')
pop_exc.populate_by_addr_list(nsetup, 'dynapse_u0', 'neuron',[[i,0] for i in range(128)])

mon_core1 = nsetup.monitors.import_monitors_otf(pop_exc)




