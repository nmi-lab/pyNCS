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
pop_exc0=pyNCS.Population(name='myU0C2_pop')
pop_exc0.populate_by_addr_list(nsetup, chipid = 'U0', neurontype = 'neuron', id_list = [[i,0] for i in range(64)])

pop_exc1=pyNCS.Population(name='myU0C1_pop')
pop_exc1.populate_by_addr_list(nsetup, chipid = 'U0', neurontype = 'neuron', id_list = [[i,1] for i in range(64)])

pop_exc2=pyNCS.Population(name='myU0C2_pop')
pop_exc2.populate_by_addr_list(nsetup, chipid = 'U0', neurontype = 'neuron', id_list = [[i,2] for i in range(64)])

#Create Monitors
mon_pop0 = nsetup.monitors.create(pop_exc0)
mon_pop1 = nsetup.monitors.create(pop_exc1)
mon_pop2 = nsetup.monitors.create(pop_exc2)

#Create Connections
M = np.ones([len(mon_pop1),len(mon_pop1)], dtype = 'bool') #Custom Matrix
conn1 = pyNCS.Connection(
        pop_exc1,pop_exc2, 
        synapse='exc_fast',
        fashion = 'by_boolean_matrix',
        fashion_kwargs = {'connection':M})

#conn2 = pyNCS.Connection(
#        pop_exc0,pop_exc2, 
#        synapse='exc_fast',
#        fashion = 'by_boolean_matrix',
#        fashion_kwargs = {'connection':M})

#Prepare setup and connections
nsetup.prepare()
#U0.set_parameter('C0_IF_DC_P.fineValue',0)
#U0.set_parameter('C1_IF_DC_P.fineValue',0)
#U0.set_parameter('C2_IF_DC_P.fineValue',0)
#U0.set_parameter('C1_NPDPIE_THR_F_P.coarseValue',5)
#U0.set_parameter('C1_NPDPIE_THR_F_P.fineValue',50)
#U0.set_parameter('C1_PS_WEIGHT_EXC_F_N.coarseValue',1)
#U0.set_parameter('C1_PS_WEIGHT_EXC_F_N.fineValue',50)
#U0.set_parameter('C2_NPDPIE_THR_F_P.coarseValue',5)
#U0.set_parameter('C2_NPDPIE_THR_F_P.fineValue',50)
#U0.set_parameter('C2_PS_WEIGHT_EXC_F_N.coarseValue',1)
#U0.set_parameter('C2_PS_WEIGHT_EXC_F_N.fineValue',50)

#Run (stimulus not supported yet)
#nsetup.run(None, duration = 1000)    
#RasterPlot(nsetup.monitors)


