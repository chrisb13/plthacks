#!/usr/bin/env python 
#   Author: Christopher Bull. 
#   Affiliation: Climate Change Research Centre and ARC Centre of Excellence for Climate System Science.
#                Level 4, Mathews Building
#                University of New South Wales
#                Sydney, NSW, Australia, 2052
#   Contact: z3457920@student.unsw.edu.au
#   www:     christopherbull.com.au
#   Date created: Tue, 08 Mar 2016 01:43:11
#   Machine created on: chris-VirtualBox2
#

"""
Tests for plthacks package
"""
import os
import sys
import time
#add one dirs up to path
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import plthacks as plth 
import collections
import numpy as np

def Grid_example(plotoutputs):
    """@todo: Docstring for Grid_example
    :returns: @todo
    """
    plotdict=collections.OrderedDict()
    dimlab=collections.OrderedDict()
    cnts=[str(cnt) for cnt in np.arange(11)+1]
    for cnt in cnts:
        plotdict[cnt]=np.random.rand(20,15)
        dimlab[cnt]=('xlabel','ylabel')

    plth.Grid(plotdict,(4,3),sharex=True,outputpath=plotoutputs+'GridEgShareX.png')
    plth.Grid(plotdict,(4,3),sharey=True,outputpath=plotoutputs+'GridEgSHareY.png')
    plth.Grid(plotdict,(4,3),sharex=True,sharey=True,outputpath=plotoutputs+'GridEgShareXShareY.png')
    plth.Grid(plotdict,(4,3),dimlabels=dimlab,outputpath=plotoutputs+'GridEgDimLab.png')
    plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,outputpath=plotoutputs+'GridEgShareXShareYDimLab.png')

if __name__ == "__main__": 
    from _cblogger import _LogStart
    _lg=_LogStart().setup()
    #put useful code here!

    plot_output_folder='/home/chris/codescratch/plthacks/testplots/'

    Grid_example(plot_output_folder)

    _lg.info('')
    localtime = time.asctime( time.localtime(time.time()) )
    _lg.info("Local current time : "+ str(localtime))
    _lg.info('SCRIPT ended')
