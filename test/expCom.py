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

def clear_sram_memory(sramId = 1, coreId = 0, chipid = 0):
    for neuronId in range(256):
        #we loop over all cores
        dx = 0;
        sx = 0;
        dy = 0;
        sy = 0;
        destcoreId = 0;        
        bits = neuronId << 7 | sramId << 5 | coreId << 15 | 1 << 17 | 1 << 4 | destcoreId << 18 | sy << 27 | dy << 25 | dx << 22 | sx << 24 | coreId << 28 | chipid <<30;
        send_dynapse_event(bits)

def set_neurons_sram(
        chipid,
        coreId,
        sramId = 1,
        neurons = range(256),
        destcoreId = 0,
        dx = 0,
        sx = 0,
        dy = 0,
        sy = 0,
        ):

    for neuronId in neurons:
        #we loop over all cores
        bits = neuronId << 7 | sramId << 5 | coreId << 15 | 1 << 17 | 1 << 4 | destcoreId << 18 | sy << 27 | dy << 25 | dx << 22 | sx << 24 | coreId << 28 | chipid <<30;
        send_dynapse_event(bits)

def clear_camId(
        chipid,
        coreId,
        camId,
        neuronId = 0):
    bits = chipid << 30 | 1 << 17 |coreId << 15 | neuronId<<5 ;
    send_dynapse_event(bits)

def clear_core_cam( chipid,
                    coreId,
                    ):
    for row in range(1024):
        bits = []
        for col in range(16):
            bits.append(chipid << 30 | 1 << 17 |coreId << 15 | row <<5 | col );
        send_dynapse_event(bits)

def set_neuron_cam(
        chipid,
        camId,
        ei = 1,
        fs = 1,
        srcneuronId = 0,
        destneuronId = 0,
        srccoreId = 0,
        destcoreId = 0):
    bits = []
    synapse_row = camId;                 # cam ID
    nrn_1 = (destneuronId & 0xf0)>>4
    nrn_2 = destneuronId & 0x0f
    bits .append( chipid << 30 | ei << 29 | fs << 28 | srcneuronId << 20 | srccoreId << 18 | 1 << 17 | destcoreId << 15 | nrn_1 << 11 | camId << 5 | nrn_2 );
    send_dynapse_event(bits)




def send_dynapse_event(events):
    sock.send(np.array(events).astype('uint64').tobytes())

if __name__ == '__main__':
    clear_sram_memory(sramId=1,coreId=3,chipid=0)
    set_neurons_sram(chipid=0, coreId=0,sramId=1,neurons=range(256), destcoreId=8)
    #core 3 is 0b1000 = 3
    for j in range(0,16<<4,16):
        for i in range(32):
            set_neuron_cam(chipid=0,
                    camId=i,
                    ei=1,
                    fs=1,
                    srcneuronId=i,
                    destneuronId=j,
                    srccoreId=0,
                    destcoreId=3)
