#!/bin/python
#-----------------------------------------------------------------------------
# File Name : expCom.py
# Author: Emre Neftci
#
# Creation Date : Fri 21 Apr 2017 11:15:31 AM PDT
# Last Modified : 
#
# Copyright : (c) UC Regents, Emre Neftci
# Licence : GPLv2
#----------------------------------------------------------------------------- 
import numpy as np
import warnings, socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('128.200.83.67', 8890))
sock.settimeout(1.0)

def send_dynapse_event(events):
    sock.send(np.array(events).astype('uint64').tobytes())
