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
from expPop import *

c = nsetup.chips['u0']
tls = []
sls = []
for i in range(0,255,15):
    c.configurator.set_parameter('C0_IF_DC_P.fineValue', i)
    nsetup.run(None, duration = 1000)    
    tls.append(mon_core1.copy())
    sls.append(mon_core1.mean_rate())

