# coding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import sys as sys
import DictManips as DM


def PARAMS( manip):
    path = '../' + manip + '/VST/outputData/'
    path_s =  'FIG/'
    s_name = "all_nodes.txt"
    file_time = 'log.txt'

    return path, path_s, s_name, file_time

def get_nodes( path, s_name):
    nodes = np.loadtxt( path + s_name)

    return nodes

def dir_exist( directory):
    if not os.path.exists( directory ):
        os.makedirs( directory )

    return

def plotnames():
    pltnames = [ 'Apex'
                 ,'N3'
                 ,'Length' ]
    return pltnames

def plot_nodes( nodes, path_s, s_name, marker):

    pltnames = plotnames()

    for pltname,inc in zip( pltnames, range(len(pltnames)) ) :
        plt.figure( pltname + '_log' )
        plt.semilogy( nodes[:,0], nodes[:,inc+1], marker)

        plt.figure( pltname + '_lin' )
        plt.plot( nodes[:,0], nodes[:,inc+1], marker)

    return

def plot_nodes_fit( nodes, path_s, s_name, marker, fitsur='Length'):

    import fit as fit
    import importlib
    importlib.reload( fit )
    t0 = 700
    print('fit pour les t > ' + str(t0) + ' min')
    pltnames = plotnames()
    for pltname,inc in zip( pltnames, range(len(pltnames)) ) :
        plt.figure( pltname + '_log' )
        plt.semilogy( nodes[:,0], nodes[:,inc+1], marker)
        if pltname==fitsur :
            x = nodes[( nodes[:,0]> t0 ),0]
            y = nodes[( nodes[:,0]> t0 ),inc+1]
            popt, pcov = fit.main( x, y )

        plt.figure( pltname + '_lin' )
        plt.plot( nodes[:,0], nodes[:,inc+1], marker)
        if pltname==fitsur :
            x = nodes[( nodes[:,0]> t0 ),0]
            y = nodes[( nodes[:,0]> t0 ),inc+1]
            fit.main( x, y )

    return popt, pcov

def arrange_plot():
    pltnames = plotnames()

    for pltname,inc in zip( pltnames, range(len(pltnames)) ) :
        plt.figure( pltname + '_log' )
        plt.xlabel('Frame Number')

        plt.figure( pltname + '_lin' )
        plt.xlabel('Frame Number')

def save_plot( p ):

    dir_exist( p )

    pltnames = plotnames()

    for pltname,inc in zip( pltnames, range(len(pltnames)) ) :
        plt.figure( pltname + '_log' )
        plt.savefig( p + pltname + '_log'  + '.png', dpi=300)

        plt.figure( pltname + '_lin' )
        plt.savefig( p + pltname + '_lin'  + '.png', dpi=300)

    return

def main( manip ):
    plt.close('all')
    print('\nmanip : ' + manip)
    path, path_s, s_name, file_time = PARAMS( manip)
    nodes = get_nodes( path, s_name)

    manips = DM.MANIPS(0)
    ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
    marker = manips[ref+1]['marker']

    plot_nodes( nodes, path + path_s, s_name, marker)
    arrange_plot()
    save_plot(path + path_s)
    print('Fig saved in ' + path + path_s)

    return

if __name__ == "__main__":
#    manip = '2019_04_09_P_S_M2'
    manip = sys.argv[1]
    main( manip )


