# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt 
import os
import DictManips as DM


# pour mémoire, les données sont issues de la manip 2019_04_09_P_S_M2
# le film a été fait avec les images du plot 'Distribution de la masse'

"""
prévoir //:
from joblib import Parallel, delayed
import multiprocessing
# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)
def processInput(i):
     return i * i
num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)

"""

def PARAMS( manip):
    # chemins des fichiers data
    path = '../' + manip + '/VST/outputData/mass_distribution/'
    return path


def plot_distribution_radius( path, filename, name):

    f = np.loadtxt( path + filename)

    import re
    m = re.search( 'regMovie_', filename)
    frame_number = filename[ m.end(): m.end()+2 ]

    if len(f) is not 0:
        radius = np.sqrt( f[:,0]**2 + f[:,1]**2 )

        sort = np.argsort( radius)
        radius = radius[sort]
        f = f[sort,:]

        # distribution de la masse
        nbins = 50
        radius_bins = np.linspace( 0, np.max(radius), nbins)
        DM = np.array([])
        for inc in range(nbins-1) :
            DM = np.append( DM, np.sum(f[(radius > radius_bins[inc]) & (radius < radius_bins[inc+1]),2]))

        fname = 'Distribution des distance au centre des segments'
        plt.close( fname)
        plt.figure( fname)
        plt.hist( radius, bins=50)
        plt.title(filename)
        plt.xlabel('RADIUS')
        plt.savefig( path + 'mass_distribution_' + frame_number + '_' + name + '_1.png')

        fname = 'Distribution des longueurs des segments'
        plt.close( fname)
        plt.figure( fname)
        plt.hist( f[:,2], bins=50)
        plt.title(filename)
        plt.xlabel('LENGTH')
        plt.savefig( path + 'mass_distribution'  + frame_number + '_' + name + '_2.png')

        fname = 'Localisation des segments'
        plt.close( fname)
        plt.figure( fname)
        plt.title(filename)
        plt.plot( f[:,0], -1*f[:,1], '.k')
        plt.savefig( path  + 'mass_distribution' + frame_number + '_' + name + '_3.png')

        fname = 'Distribution de la masse'
        plt.close( fname)
        plt.figure( fname)
        deltaR = np.diff( radius_bins )[0]
        deltaS = np.pi *  deltaR*( deltaR + 2*radius_bins[1:] )
        plt.plot(radius_bins[1:], DM / deltaS, '-ok')
        #    plt.plot(radius_bins[1:], DM , '-or')
        plt.title(filename)
        plt.xlabel('R0')
        plt.ylabel('sum Mass / dS')
        plt.savefig( path  + 'mass_distribution' + frame_number + '_' + name  + '_4.png')

    else:
        f = 0
        radius = 0
        radius_bins = 0
        DM = 0
    # plt.show()

    return f, radius, radius_bins, DM





def main():
    import DictManips as DM
    manips = DM.MANIPS(0)
    names = [manips[inc]['name'] for inc in manips.keys()]
    # names = names[0]
    for name in names:
        print('\t ' + name)
        path = PARAMS( name)
        allfiles = os.listdir( path)
        files = [ fname for fname in allfiles if fname.endswith('.gpickle.txt')]

        for inc in range(len(files)):
            f, radius, radius_bins, DM = plot_distribution_radius( path , files[inc], name)

if __name__ == "__main__":
    main()

