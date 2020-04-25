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


def main( ):
    manips = DM.MANIPS( 0)
    names = [manips[inc]['name'] for inc in manips.keys()]
    for name,inc in zip( names , range(len(names)) ) :
        plot_all_nodes.main( name )


if __name__ == "__main__":
    main( )


