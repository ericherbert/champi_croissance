# coding: utf-8


import os
import numpy as np
import matplotlib.pyplot as plt
import sys as sys
import DictManips as DM
import plot_all_nodes as plot_all_nodes


import importlib
importlib.reload( DM )


def arrange_plot( figures):
    plt.rc('font', family='serif')
    plt.rc('text', usetex=True)
    fs = 20
    for figure in figures :
        plt.figure( figure )
        plt.xticks([0,1,2,3],['M0','0.5$\\times$M2','M2','2$\\times$M2'], fontsize=fs-5)
        plt.xlabel(r' Growth Medium', fontsize=fs)
        plt.tick_params(labelsize=fs-5)
        if figure == 'prefacteur':
            plt.ylabel(r' Prefactor [mm]', fontsize=fs)
        elif figure == 'exposant':
            plt.ylabel(r' Exponent [min$^{-1}$]', fontsize=fs)

        plt.tight_layout()

def init(figures):
    for figure in figures:
        plt.close( figure )

def close( path, figures):
    for figure in figures:
        plt.figure( figure)
        plt.savefig( path + figure, dpi=300)
    plt.show()

def do_plot( path):
    ab = np.loadtxt( path + 'fit_values.txt')
    stdab = np.loadtxt( path + 'std_fit_values.txt')

    manips = DM.MANIPS(0)
    names = [manips[inc]['name'] for inc in manips.keys()]

    for manip,inc in zip( names , range(len(names)) ) :

        print('\nmanip : ' + manip)
        ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
        marker = manips[ref+1]['marker']

        ref = np.where([manips[inc]['name']==manip for inc in manips.keys()])[0][0]
        milieu = manips[ref+1]['milieu']
        if milieu=='M0':
            ref = 0
        elif milieu=='M2x0.5':
            ref = 1
        if milieu=='M2':
            ref = 2
        if milieu=='M2x2':
            ref = 3

        nstd = 3
        plt.figure( 'prefacteur' )
        plt.plot( ref, ab[2*inc], marker)
        plt.errorbar( ref, ab[2*inc], yerr=nstd*stdab[2*inc], fmt = marker)

        plt.figure( 'exposant' )
        plt.plot( ref, ab[2*inc+1], marker)
        plt.errorbar( ref, ab[2*inc+1], yerr=nstd*stdab[2*inc+1], fmt = marker)

def main():

    figures = [ 'exposant' , 'prefacteur' ]
    init( figures)

    paths = ['./FIG/t0_300min/',
             './FIG/t0_500min/',
             './FIG/t0_700min/']

    for path in paths:
        do_plot( path)

    arrange_plot( figures)

    close( './FIG/', figures)

    return

if __name__ == "__main__":
    main()

