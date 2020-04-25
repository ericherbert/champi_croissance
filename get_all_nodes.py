# coding: utf-8

# enregistre tous les noeuds, apex et Ltot dans le fichier nodes
# si le temps existe, il est ajouté en derniere colonne de nodes
# modifer les parametres et exectuer avec:
# python3 get_all_nodes.py

import comptage_noeuds as cn
import read_time
import os
import numpy as np

def PARAMS():
    path = '/home/eh/DD2/recherche/hyphes_croissance/data/2019_04_09_P_S_M2/VST/'
    path_s =  '/outputData/'
    s_name = "all_nodes"
    file_time = 'log.txt'
    return path, path_s, s_name, file_time


def get_nodes( path, path_s, s_name):

    allfiles = os.listdir(path)
    files = [ fname for fname in allfiles if fname.endswith('.gpickle')]
    #print files

    nodes = np.zeros( (len(files), 4))

    for inc in range(len(files)):
#    print(files[inc])
        apex, embranchements, Ltot = cn.comptage_noeuds( path, files[inc])
        nodes[inc,1] = apex
        nodes[inc,2] = embranchements
        nodes[inc,3] = Ltot
        temp = files[inc]
        nodes[inc,0] = np.uint8( temp[ str.find(temp,'Movie_')+6 : str.find(temp,'_gr') ] )

#    nodes[inc,0] = files[inc][16:-20]

    ordre = np.argsort( nodes[:,0])
    nodes[:,0] = nodes[ordre,0]
    nodes[:,1] = nodes[ordre,1]
    nodes[:,2] = nodes[ordre,2]
    nodes[:,3] = nodes[ordre,3]
    return nodes



if __name__ == "__main__":

    path, path_s, s_name, file_time = PARAMS()
    nodes = get_nodes( path, path_s, s_name)

    if os.path.isfile( file_time):
        time = read_time( file_time)
        nodes = np.append( nodes, time)
    else:
        print(' ====> NO TIME FILE FOUND <=====')

    if not os.path.exists(path + path_s):
        os.makedirs(path + path_s)

    np.savetxt( path + path_s + s_name + '.txt', nodes )



