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

pop_exc1=pyNCS.Population(name='core0')
pop_exc1.populate_by_addr_list(nsetup, 'dynapse_u0', 'neuron',[[i,0] for i in range(32)])
pop_exc2=pyNCS.Population(name='core3')
pop_exc2.populate_by_addr_list(nsetup, 'dynapse_u0', 'neuron',[[i,3] for i in range(16)])

mon_core1 = nsetup.monitors.import_monitors_otf(pop_exc1)
mon_core2 = nsetup.monitors.import_monitors_otf(pop_exc2)

if __name__ == '__main__':
    c0 = nsetup.chips['dynapse_u0']
    c1 = nsetup.chips['dynapse_u1']
    c2 = nsetup.chips['dynapse_u2']
    c3 = nsetup.chips['dynapse_u3']




