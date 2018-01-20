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

def clear_sram_memory(sramId = 1, coreId = 0, chipId = 0):
    for neuronId in range(256):
        #we loop over all cores
        dx = 0;
        sx = 0;
        dy = 0;
        sy = 0;
        destcoreId = 0;  #one hot coded    
        bits = neuronId << 7 | sramId << 5 | coreId << 15 | 1 << 17 | 1 << 4 | destcoreId << 18 | sy << 27 | dy << 25 | dx << 22 | sx << 24 | coreId << 28 | chipId <<30;
        send_dynapse_event(bits)

def set_neurons_sram(
        chipId,
        coreId,
        sramId = 1,
        neurons = range(256),
        destcoreId = 0,
        dx = 0,
        sx = 0,
        dy = 0,
        sy = 0,
        ):

    if hasattr(destcoreId, '__len__'):
        destcoreId = sum([2**i for i in destcoreId])

    for neuronId in neurons:
        #we loop over all cores
        bits = neuronId << 7 | sramId << 5 | coreId << 15 | 1 << 17 | 1 << 4 | destcoreId << 18 | sy << 27 | dy << 25 | dx << 22 | sx << 24 | coreId << 28 | chipId <<30;
        send_dynapse_event(bits)

def clear_camId(
        chipId,
        coreId,
        camId,
        neuronId = 0):
    bits = chipId << 30 | 1 << 17 |coreId << 15 | neuronId<<5 ;
    send_dynapse_event(bits)

def clear_core_cam( chipId,
                    coreId,
                    ):
    bits = []
    for row in range(1024):
        for col in range(16):
            bits.append(chipId << 30 | 1 << 17 |coreId << 15 | row <<5 | col );
    send_dynapse_event(bits)

def set_neuron_cam(
        chipId,
        camId,
        ei = 1, #excitatory
        fs = 1, #fast
        srcneuronId = 0, #sending neuron
        destneuronId = 0, #receiving neuron
        srccoreId = 0, #sending core (= extratag)
        destcoreId = 0): #receiving core (not 1 hot coded)
    bits = []
    synapse_row = camId;                 # cam ID
    nrn_1 = (destneuronId & 0xf0)>>4
    nrn_2 = destneuronId & 0x0f
    bits .append( chipId << 30 | ei << 29 | fs << 28 | srcneuronId << 20 | srccoreId << 18 | 1 << 17 | destcoreId << 15 | nrn_1 << 11 | camId << 5 | nrn_2 );
    send_dynapse_event(bits)

def send_dynapse_event(events):
    sock.send(np.array(events).astype('uint64').tostring())

def tau1_core_set(chipId,coreId):
    bits = chipId << 30 |\
            1 << 12 |\
            0 << 11 |\
            coreId << 8
    send_dynapse_event(bits)

def tau2_core_set(chipId,coreId):
    bits = chipId << 30 |\
            1 << 12 |\
            1 << 11 |\
            coreId << 8
    send_dynapse_event(bits)

def tau2_set(chipId,coreId,neuronId):
    bits = chipId << 30 |\
            1 << 10 |\
            coreId << 8 |\
            neuronId
    send_dynapse_event(bits)


def init_core(chipId, coreId):
    clear_core_cam(chipId=chipId, coreId=coreId)
    clear_sram_memory(chipId=chipId, sramId=1, coreId=coreId)
    clear_sram_memory(chipId=chipId, sramId=2, coreId=coreId)
    clear_sram_memory(chipId=chipId, sramId=3, coreId=coreId)
#core 3 is 0b1000 = 8

