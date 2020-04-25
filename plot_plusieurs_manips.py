# coding: utf-8


import os
import numpy as np
import matplotlib.pyplot as plt
import sys as sys
import DictManips as DM
import plot_all_nodes as plot_all_nodes


import importlib
importlib.reload( plot_all_nodes )
importlib.reload( DM )


def SI( nodes, deltat, pix):
    nodes[:,0] = nodes[:,0] * deltat / 60
    nodes[:,3] = nodes[:,3] * pix * 1e-3
    return nodes

def arrange_plot():

    pltnames = plot_all_nodes.plotnames()

    for pltname,inc in zip( pltnames, range(len(pltnames)) ) :
        plt.figure( pltname + '_log' )
        plt.xlabel('Time [min]')

        plt.figure( pltname + '_lin' )
        # plt.ylim( -1000, 10000)
        # plt.xlim( 0, 300)
        plt.xlabel('Time [min]')


def main():
    plt.close('all')
    manips = DM.MANIPS(0)
    names = [manips[inc]['name'] for inc in manips.keys()]
    fit_values = np.array([])
    std_fit_values = np.array([])
    for manip,inc in zip( names , range(len(names)) ) :
        print('\nmanip : ' + manip)
        path, path_s, s_name, file_time = plot_all_nodes.PARAMS( manip)
        nodes = plot_all_nodes.get_nodes( path, s_name)

        ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
        deltat = manips[ref+1]['deltat']
        ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
        pix = manips[ref+1]['pix']
        nodes = SI( nodes, deltat, pix )

        ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
        marker = manips[ref+1]['marker']

        # plot_all_nodes.plot_nodes( nodes, path + path_s, s_name, marker)
        popt, pcov = plot_all_nodes.plot_nodes_fit( nodes, path + path_s, s_name, marker)

        fit_values = np.append( fit_values, popt)
        std0 = np.sqrt(np.diag(pcov))[0]
        std1 = np.sqrt(np.diag(pcov))[1]
        std_fit_values = np.append( std_fit_values, np.array([ std0, std1]))

    arrange_plot()
    path = './FIG/t0_700min/'
    plot_all_nodes.save_plot( path)
    print('\n\t Fig saved in ' + path)

    np.savetxt( path + 'fit_values.txt', fit_values, delimiter=',')
    np.savetxt( path + 'std_fit_values.txt', std_fit_values, delimiter=',')
    return fit_values

if __name__ == "__main__":
    main()

