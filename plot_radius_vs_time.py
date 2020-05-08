# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt 
import os
import DictManips as DM



# plot le rayon du thalle construit suivant les methodes suivantes:
# 1. valeur la plus probable de la distribution de la masse (pas la densité)
# 2. médiane de la distribution de la masse (pas la densité)
# 3. ?


def PARAMS( manip):
    # chemins des fichiers data
    path = '../' + manip + '/VST/outputData/mass_distribution/'
    return path

def plot_init( fig_list):
    for fname in fig_list:
        plt.close( fname)
        plt.figure( fname)

def dir_exist( directory):
    if not os.path.exists( directory ):
        os.makedirs( directory )

def Frame_Number( filename):
    import re
    m = re.search( 'regMovie_', filename)
    frame_number = filename[ m.end(): m.end()+2 ]
    return frame_number

def distribution_radius( fig_list, path, filename, name, norm_dist):
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
        criteres_bins = np.linspace( 0, np.max(radius), nbins)
        DM = np.array([])
        for inc in range(nbins-1) :
            DM = np.append( DM, np.sum(f[(radius > criteres_bins[inc]) & (radius < criteres_bins[inc+1]),2]))

        fname = 'Distribution de la masse'
        plt.figure( fname)
        plt.plot( criteres_bins[1:], DM, 'o')
        plt.title(filename)
        plt.xlabel(' ')

        return  f, radius, criteres_bins[1:], DM

def methode_max( x, y):
    critere = np.argmax(y)
    return x[critere], y[critere]

def methode_median( x, y):
    int_y = np.cumsum( y)
    # calcul median 
    x = x[int_y / int_y[-1] > 0.5]
    x = x[0]
    y = y[int_y / int_y[-1] > 0.5]
    y = y[0]
    return x, y

def methode_seuil_densite( radius_bins, DM):
    deltaR = np.diff( radius_bins )[0]
    deltaS = np.pi *  deltaR * ( deltaR + 2*radius_bins )
    x, y = radius_bins, DM / deltaS
    densite_moyenne = np.cumsum(y)[-1] / len(x)
    seuil = .5        # 1 = seuil à 100% de la densité moyenne
    seuil = densite_moyenne * seuil
    x = x[ y > seuil ][-1]  # rayon au seuil
    # y = y[ y > seuil ][-1] # calcul de la densité au seuil si besoin
    y = DM[ y > seuil ][-1]     # on recupere la masse pour comparaison avec autres methodes
    return x, y

def plot_methode( x, y, methode):
    critere = np.argsort( x)
    x = x[critere]
    y = y[critere]
    if methode == 'max':
        color = 'r'
    elif methode == 'median':
        color = 'b'
    elif methode == 'densite':
        color = 'g'

    plt.plot( x, y,  linewidth=3, color=color)

def save_metode(NN, x, y, methode):
    todo



def plot_temp( NN, x, methode):

    critere = np.argsort( x)
    x = x[critere]
    if methode == 'max':
        plt.loglog( NN, x/np.max(x), 'or')
    elif methode == 'median':
        plt.loglog( NN, x/np.max(x), 'sb')
    elif methode == 'densite':
        plt.loglog( NN, x/np.max(x), '*g')
    elif not np.isnan(methode):
        slope = methode
        plt.loglog( NN, (x/np.max(x))**slope, '-k')





def main():

    fig_list = [ 'Distribution de la masse' ]

    # names = [ '2019_04_11_P_S_M2' ]
    names = [ '2019_03_27_P_S_M0' ]
    # quelle frame utilisée ?
    NN = np.array([5, 30, 45, 60, 75])
    print('on utilise les frame : ' + str(NN) )

    plot_init( fig_list)

    for name in names:
        print('\t ' + name)
        path = PARAMS( name)
        allfiles = os.listdir( path)
        files = [ fname for fname in allfiles if fname.endswith('.gpickle.txt')]
        rmax = np.array([])
        Mmax = np.array([])
        rmed = np.array([])
        Mmed = np.array([])
        rdensite = np.array([])
        Mdensite = np.array([])

        for inc in range(len(files)): 
            fname = files[inc]
            frame_number = np.uint(Frame_Number( fname))
            if frame_number in NN:
                print(frame_number)
                f, radius, radius_bins, DM = distribution_radius(fig_list, path , fname, name, 0)

                x, y = methode_max( radius_bins, DM)
                rmax = np.append( rmax, x)
                Mmax = np.append( Mmax, y)

                x, y = methode_median( radius_bins, DM)
                rmed = np.append( rmed, x)
                Mmed = np.append( Mmed, y)

                x, y = methode_seuil_densite( radius_bins, DM)
                rdensite = np.append( rdensite, x)
                Mdensite = np.append( Mdensite, y)

        plot_methode( rmax, Mmax, 'max')
        plot_methode( rmed, Mmed, 'median')
        plot_methode( rdensite, Mdensite, 'densite')

        # plt.close('temp')
        plt.figure('temp')
        plot_temp( NN, rmax, 'max')
        plot_temp( NN, rmed, 'median')
        plot_temp( NN, rdensite, 'densite')
        plot_temp( NN, NN, 0.5)  # plot la loi de puissance selon argument numerique

    plt.show()



if __name__ == "__main__":
    main()


