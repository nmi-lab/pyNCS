#-----------------------------------------------------------------------------
# Purpose:
#
# Author: <authors name>
#
# Copyright : University of Zurich, Giacomo Indiveri, Emre Neftci, Sadique Sheik, Fabio Stefanini
# Licence : GPLv2
#-----------------------------------------------------------------------------
#ConfAPI
#Biases and mapper
#Api for modules having pyAMDA-like functionality
#Api for modules having pyAEX-like functionality

from types import GeneratorType  # For checking generator type
from contextlib import contextmanager
from lxml import etree
import warnings

class Parameter:
    def __init__(self, param_name, params_dict):
        '''
        Parameter(parameters, configurator)
        params_dict: dictionary of parameters and values
        This object is designed to be used with the configurator to set parameters
        '''
        self.param_data = dict(parameters)
        self.SignalName = param_name

    def __str__(self):
        return str(self.param_data)


