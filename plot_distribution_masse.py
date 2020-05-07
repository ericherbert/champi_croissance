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

def plot_init( fig_list):
    for fname in fig_list:
        plt.close( fname)
        plt.figure( fname)

def plot_close( fig_list, figname, norm_dist=0):
    path = './FIG/mass_distribution/temp/'
    dir_exist( path)

    for fname in fig_list:
        plt.figure( fname)
        if norm_dist: fname =  'pdf_' + fname
        plt.savefig( path + figname + '_' + fname + '.png', dpi=300)

def dir_exist( directory):
    if not os.path.exists( directory ):
        os.makedirs( directory )

def Frame_Number( filename):
    import re
    m = re.search( 'regMovie_', filename)
    frame_number = filename[ m.end(): m.end()+2 ]
    return frame_number


def pdf( x, y, angular=0 ):
    # pdf de la distribution au rayon normalisé
    if angular is 0:
        x = x / (np.max(x)-np.min(x))
    deltax = np.diff(x)[0]
    Surface = np.sum(deltax * y)
    y = y / Surface
    # print(np.sum(deltax*y))
    return x, y

def plot_distribution_radius( fig_list, path, filename, name, norm_dist):
    import DictManips as DM

    f = np.loadtxt( path + filename)

    frame_number = Frame_Number( filename)

    manips = DM.MANIPS(0)
    ref = np.where([manips[inc]['name']==name for inc in manips.keys()])[0][0]
    marker = manips[ref+1]['marker']

    
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
            # on sommes les masses des noeuds dans la gamme
            # de chaque bin
            DM = np.append( DM, np.sum(f[(radius > radius_bins[inc]) & (radius < radius_bins[inc+1]),2]))


        fname = 'Distribution des distance au centre des segments'
        plt.figure( fname)
        plt.hist( radius, bins=50)
        plt.title(filename)
        plt.xlabel('RADIUS')
  
        fname = 'Distribution des longueurs des segments'
        plt.figure( fname)
        plt.hist( f[:,2], bins=50)
        plt.title(filename)
        plt.xlabel('LENGTH')
  
        fname = 'Localisation des segments'
        plt.figure( fname)
        plt.title(filename)
        plt.plot( f[:,0], -1*f[:,1], marker)
  
        fname = 'Distribution de la masse'
        plt.figure( fname)
        deltaR = np.diff( radius_bins )[0]
        deltaS = np.pi *  deltaR * ( deltaR + 2*radius_bins[1:] )
        x, y = radius_bins[1:], DM / deltaS
        if norm_dist:
            x , y = pdf( x, y )
        plt.plot( x, y,  marker)
        #    plt.plot(radius_bins[1:], DM , '-or')
        plt.title(filename)
        plt.xlabel('R0')
        plt.ylabel('sum Mass / dS')


    else:
        f = 0
        radius = 0
        radius_bins = 0
        DM = 0
    # plt.show()

    return f, radius, radius_bins, DM


def plot_distribution_angle( fig_list, path, filename, name, norm_dist):
    import DictManips as DM

    f = np.loadtxt( path + filename)

    frame_number = Frame_Number( filename)

    manips = DM.MANIPS(0)
    ref = np.where([manips[inc]['name']==name for inc in manips.keys()])[0][0]
    marker = manips[ref+1]['marker']

    if len(f) is not 0:
        critere = np.arctan2( f[:,0], f[:,1] )

        sort = np.argsort( critere)
        critere = critere[sort]
        f = f[sort,:]

        # distribution de la masse
        nbins = 50
        criteres_bins = np.linspace( -np.pi, np.pi, nbins)
        DM = np.array([])
        for inc in range(nbins-1) :
            DM = np.append( DM, np.sum(f[(critere > criteres_bins[inc]) & (critere < criteres_bins[inc+1]),2]))


        fname = 'Distribution angulaire  des segments'
        plt.figure( fname)
        plt.hist( critere, bins=50)
        plt.title(filename)
        plt.xlabel('Angle')

        fname = 'Distribution angulaire de la masse'
        plt.figure( fname)
        deltaTheta = np.diff( criteres_bins )[0]
        radius = np.mean(np.sqrt( f[:,0]**2 + f[:,1]**2 ))
        deltaS = deltaTheta * radius
        x, y = criteres_bins[1:], DM / deltaS
        if norm_dist:
            x , y = pdf( x, y , angular=1)
        plt.plot( x/np.pi, y,  marker+'-')
        #    plt.plot(radius_bins[1:], DM , '-or')
        plt.title(filename)
        plt.xlabel('angle')
        plt.ylabel('sum Mass / dS')


    else:
        f = 0
        radius = 0
        radius_bins = 0
        DM = 0
    # plt.show()

    return f, critere, criteres_bins, DM



def main():
    import DictManips as DM
    import re

    fig_list = ['Distribution des distance au centre des segments'
                ,'Distribution des longueurs des segments'
                ,'Localisation des segments'
                ,'Distribution de la masse'
                ,'Distribution angulaire  des segments'
                ,'Distribution angulaire de la masse']


    plot_init( fig_list)



    ####
    # 1 manip ou toutes les manips:       #
    AllManip = 0
    if AllManip:
        manips = DM.MANIPS(0)
        names = [manips[inc]['name'] for inc in manips.keys()]
        # names = names[0]
        # quelle frame utilisée ? attention une seule
        NN = (50,)
        print('on utilise la frame : ' + str(NN) )
    else:
        names = [ '2019_04_11_P_S_M2']
        # quelle frame utilisée ?
        NN = (5, 30, 45, 60, 75)
        print('on utilise les frame : ' + str(NN) )

    norm_dist = 1
    print('normalisation : ' +  str(norm_dist))

    for name in names:
        print('\t ' + name)
        path = PARAMS( name)
        allfiles = os.listdir( path)
        files = [ fname for fname in allfiles if fname.endswith('.gpickle.txt')]

        for inc in range(len(files)):
            fname = files[inc]
            frame_number = np.uint(Frame_Number( fname))
            if frame_number in NN:
                f, radius, radius_bins, DMr = plot_distribution_radius(fig_list, path , fname, name, norm_dist)
                f, angle, angle_bins, DMa = plot_distribution_angle(fig_list, path , fname, name, norm_dist)

    if AllManip :
        plot_close( fig_list, str(NN[0]), norm_dist )
    else:
        plot_close( fig_list, name, norm_dist )

if __name__ == "__main__":
    main()

