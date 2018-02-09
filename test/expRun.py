#!/bin/python
#-----------------------------------------------------------------------------
# File Name : 
# Author: Emre Neftci
#
# Creation Date : Thu 13 Apr 2017 04:45:01 PM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#----------------------------------------------------------------------------- 
from expSetup import *
from pyNCSre.monitors import *

#Create Populations
pop_exc1=pyNCS.Population(name='myU0C0_pop')
pop_exc1.populate_by_addr_list(nsetup, chipid = 'U0', neurontype = 'neuron', id_list = [[i,0] for i in range(256)])

pop_exc2=pyNCS.Population(name='myU1C2_pop')
pop_exc2.populate_by_addr_list(nsetup, chipid = 'U1', neurontype = 'neuron', id_list = [[i,2] for i in range(256)])

#Create Monitors
mon_pop1 = nsetup.monitors.create(pop_exc1)
mon_pop2 = nsetup.monitors.create(pop_exc2)

#Create Connections
M = np.eye(len(mon_pop1), dtype = 'bool') #Custom Matrix
conn1 = pyNCS.Connection(
        pop_exc1,pop_exc2, 
        synapse='exc_fast',
        fashion = 'by_boolean_matrix',
        fashion_kwargs = {'connection':M})

#Prepare setup
#nsetup.prepare()

#Run (stimulus not supported yet)
nsetup.run(None, duration = 1000)    
RasterPlot(nsetup.monitors)


