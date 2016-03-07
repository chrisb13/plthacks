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
Main file for plthacks package
"""

from _cblogger import _LogStart
_lg=_LogStart().setup()

import itertools
from matplotlib import gridspec
import matplotlib.pyplot as plt
import os

#for inset axes
#hacked from:
#http://matplotlib.org/examples/axes_grid/inset_locator_demo.html
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

def mkdir(p):
    """make directory of path that is passed"""
    try:
       os.makedirs(p)
       _lg.info("output folder: "+p+ " does not exist, we will make one.")
    except OSError as exc: # Python >2.5
       import errno
       if exc.errno == errno.EEXIST and os.path.isdir(p):
          pass
       else: raise

def inset_title_box(ax,title,bwidth="20%",location=1):
    """
    Function that puts title of subplot in a box
    
    :ax:    Name of matplotlib axis to add inset title text box too
    :title: 'string to put inside text box'
    :returns: @todo
    """

    axins = inset_axes(ax,
                       width=bwidth, # width = 30% of parent_bbox
                       height=.30, # height : 1 inch
                       loc=location)

    plt.setp(axins.get_xticklabels(), visible=False)
    plt.setp(axins.get_yticklabels(), visible=False)
    axins.set_xticks([])
    axins.set_yticks([])

    axins.text(0.5,0.3,title,
            horizontalalignment='center',
            transform=axins.transAxes,size=10)

class Grid(object):
    """
    Class to create a gridded set of subplots from a dictionary.

    Parameters
    ----------
    pdict: dictionary containing the arrays to plot, titles are taken from the key
    pdims: tuple with (rowdim,coldim)
    sharex (optional): share all the x axis in the grid
    sharey (optional): share all the y axis in the grid
    dimlabels (optional): dictionary containing tuples of xlabel and ylabels 
    outputpath (optional): full path of file to put plot in (if left out it won't be created)

    Returns
    -------
    
    Notes
    -------
    

    Example
    --------
    >>> plotdict=collections.OrderedDict()
    >>> dimlab=collections.OrderedDict()
    >>> #create something to plot...
    >>> cnts=[str(cnt) for cnt in np.arange(11)+1]
    >>> for cnt in cnts:
    >>>     plotdict[cnt]=np.random.rand(20,15)
    >>>     dimlab[cnt]=('xlabel','ylabel')

    >>> plth.Grid(plotdict,(4,3),sharex=True,outputpath=plotoutputs+'GridEgShareX.png')
    >>> plth.Grid(plotdict,(4,3),sharey=True,outputpath=plotoutputs+'GridEgSHareY.png')
    >>> plth.Grid(plotdict,(4,3),sharex=True,sharey=True,outputpath=plotoutputs+'GridEgShareXShareY.png')
    >>> plth.Grid(plotdict,(4,3),dimlabels=dimlab,outputpath=plotoutputs+'GridEgDimLab.png')
    >>> plth.Grid(plotdict,(4,3),sharex=True,sharey=True,dimlabels=dimlab,outputpath=plotoutputs+'GridEgShareXShareYDimLab.png')
    """
    def __init__(self, pdict,pdims,sharex=False,sharey=False,dimlabels={},outputpath=''):
        _lg.info("Creating a gridded plot from your passed dict")
        self.pdict,self.pdims = pdict,pdims
        self.sharex,self.sharey=sharex,sharey
        self.dimlabels=dimlabels
        self.outputpath=outputpath
        self.mkplot()

    def mkplot(self ):
        """@todo: Docstring for mkplot
        :returns: @todo
        """
        #set up for gridspec plot...

        subplotnum=len(self.pdict)

        plt.close('all')
        #width then height
        fig=plt.figure(figsize=(self.pdims[0]*4, self.pdims[1]*4))
        #the other option
        #fig.set_size_inches(7.5,15.5)
        
        if self.sharex:
            hs=.06
        else:
            hs=.225

        if self.sharey:
            ys=.06
        else:
            ys=.08

        gs = gridspec.GridSpec(self.pdims[0], self.pdims[1],hspace=hs,wspace=ys)

        names=itertools.cycle(self.pdict.keys())
        fields=itertools.cycle(self.pdict.values())
        if len(self.dimlabels.keys())!=0:
            labels=itertools.cycle(self.dimlabels.values())
            labelme=True
        else:
            labelme=False

        ax_xshares=[]
        ax_yshares=[]
        self.paxis={}
        for rownum in range(self.pdims[0]):
            for colnum in range(self.pdims[1]):
                # print rownum,colnum

                #contour plot
                name=names.next()
                field=fields.next()
                if labelme:
                    label=labels.next()

                #put it in a list so we can append
                # self.pdict[name]=[self.pdict[name]]

                if rownum==0:
                    ax=plt.subplot(gs[rownum,colnum])
                    ax_xshares.append(ax)

                #this if needs to be separate from the one above
                if colnum==0:
                    ax=plt.subplot(gs[rownum,colnum])
                    ax_yshares.append(ax)

                if self.sharex and rownum>0:
                    ax=plt.subplot(gs[rownum,colnum],sharex=ax_xshares[colnum])

                if self.sharey and colnum>0:
                    ax=plt.subplot(gs[rownum,colnum],sharey=ax_yshares[rownum])

                    # make labels invisible
                    plt.setp(ax.get_yticklabels(),visible=False)

                if not self.sharey and not self.sharex:
                    ax=plt.subplot(gs[rownum,colnum])
                    if labelme:
                        ax.set_xlabel(label[0])
                        ax.set_ylabel(label[1])

                # self.pdict[name]=self.pdict[name].append(ax)
                self.paxis[name]=ax
                ax.contourf(field)

                # make xlabels invisible
                if self.sharex and rownum<self.pdims[0]-1:
                    plt.setp(ax.get_xticklabels(),visible=False)

                #labeling when we are sharing axis
                if labelme:
                    if colnum==0:
                        ax.set_ylabel(label[1])

                    if rownum==0:
                        ax.set_xlabel(label[0])

                # ax.set_title(name)
                inset_title_box(ax,name)

        if self.outputpath!='':
            mkdir(os.path.dirname(self.outputpath))
            plt.savefig(self.outputpath,dpi=300)
        else:
            plt.show()

        return self
    

if __name__ == "__main__": 
    pass
