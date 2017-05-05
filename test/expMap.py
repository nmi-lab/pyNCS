#!/bin/python
#-----------------------------------------------------------------------------
# Author: Emre Neftci
#
# Creation Date : Fri 05 May 2017 01:03:41 AM PDT
# Last Modified : 
#
# Copyright : (c) 
# Licence : GPLv2
#----------------------------------------------------------------------------- 
from expPop import *
M = np.eye(256, dtype = 'bool')
kwargs = {'connection':M}
conn1 = pyNCS.Connection(pop_exc1,pop_exc2,synapse='exc_fast',fashion='by_boolean_matrix', fashion_kwargs=kwargs)


