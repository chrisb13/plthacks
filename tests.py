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
import itertools

def Grid_example(plotoutputs):
    """function to test and demo the utility of the Grid Class
    :returns: a bunch of plots
    """
    colormaps=itertools.cycle(['Accent', 'Dark2', 'Paired', 'Pastel1',\
            'Pastel2', 'Set1', 'Set2', 'Set3'])
    plotdict=collections.OrderedDict()
    dimlab=collections.OrderedDict()
    colorbars=collections.OrderedDict()
    cnts=[str(cnt) for cnt in np.arange(12)+1]
    for cnt in cnts:
        #plotdict[cnt]=np.random.rand(200,150)
        plotdict[cnt]=np.random.rand(20,15)
        dimlab[cnt]=('xlabel','ylabel')
        colorbars[cnt]=colormaps.next()

    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,sepcbar=True,outputpath=plotoutputs+'GridEgDimLabSepcbar.png')
    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,cbars=colorbars,outputpath=plotoutputs+'GridEgDimLabcbars.png')
    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,cbars=colorbars,clevels=8,outputpath=plotoutputs+'GridEgDimLabclevelscbars.png')

    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,globalcbar='True',clevels=20,sharex=True,sharey=True,outputpath=plotoutputs+'GridEgDimLabShareXShareYglobalcbarclevels.png')

    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,globalcbar='Accent',clevels=20,sharex=True,sharey=True,outputpath=plotoutputs+'GridEgDimLabShareXShareYglobalcbarAccentclevels.png')

    # plth.Grid(plotdict,(4,3),sharex=True,outputpath=plotoutputs+'GridEgShareX.png')
    # plth.Grid(plotdict,(4,3),sharey=True,outputpath=plotoutputs+'GridEgSHareY.png')
    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,outputpath=plotoutputs+'GridEgShareXShareY.png')
    # plth.Grid(plotdict,(4,3),dimlabels=dimlab,outputpath=plotoutputs+'GridEgDimLab.png')
    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,outputpath=plotoutputs+'GridEgShareXShareYDimLab.png')

    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,globalcbar='seismic',globalcbarmiddle=0,clevels=20,outputpath=plotoutputs+'GridEgShareXShareYDimLabGlobalcbarCustomGlobalcbarmiddleClevs.png')
    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,globalcbar='seismic',globalcbarmiddle=0,outputpath=plotoutputs+'GridEgShareXShareYDimLabGlobalcbarCustomGlobalcbarmiddle.png')
    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,globalcbar='True',globalcbarmiddle=0.8,outputpath=plotoutputs+'GridEgShareXShareYDimLabGlobalcbarCustomGlobalcbarmiddle.png')

    # plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,globalcbar='True',globalcbarmiddle=0.8,zoom=((3,5),(5,10)),outputpath=plotoutputs+'GridEgShareXShareYDimLabGlobalcbarCustomGlobalcbarmiddleZoom.png')

    plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,globalcbar='seismic',globalcbarmiddle=0.3,globalclimits=(0.15,0.78),outputpath=plotoutputs+'GridEgShareXShareYDimLabGlobalcbarCustomGlobalcbarmiddleGlobalclimits.png')

if __name__ == "__main__": 
    from _cblogger import _LogStart
    _lg=_LogStart().setup()
    #put useful code here!

    plot_output_folder='/home/chris/codescratch/plthacks/testplots/'
    plot_output_folder='/home/chris/repos/plthacks/testplots/'
    plot_output_folder='/tmp/testplots/'

    Grid_example(plot_output_folder)

    _lg.info('')
    localtime = time.asctime( time.localtime(time.time()) )
    _lg.info("Local current time : "+ str(localtime))
    _lg.info('SCRIPT ended')
