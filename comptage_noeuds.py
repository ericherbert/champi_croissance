# coding: utf-8

import numpy as np
#from numpy import arctan2, sqrt
#import numexpr as ne
import math
import networkx as nx
import scipy.interpolate


#center = (3858,3501) ## rentrer le centre du réseau
#filepath = '/home/hyphes/NETwork_ectraction_master/'
#filename = 'img_t1_z1_c1_graph_p5_r1.gpickle'


def comptage_noeuds( filepath, filename) :

    # import données
    DG = nx.read_gpickle(filepath + filename) 
    # pour etre sur que l'indexation des noeuds est ordonnée
    DG = nx.convert_node_labels_to_integers(DG, first_label=0, ordering='default', label_attribute=None)  

    ###longeur totale
    ltot=0
    for e in DG.edges(data=True):
            ltot+=e[2]['weight']

#    x_ord=nx.get_node_attributes(DG,'x')
#    x_ord=np.array([val for (key,val) in x_ord.iteritems()],dtype=int)-center[0]

#    y_ord=nx.get_node_attributes(DG,'y')
#    y_ord=np.array([val for (key,val) in y_ord.iteritems()],dtype=int)-center[1]

#    degrees = DG.degree()
#    degrees = np.array([val for (key,val) in degrees.iteritems()],dtype=int)
    
    graph = DG
    graph = nx.convert_node_labels_to_integers(graph, first_label=0, 
                                               ordering='default', 
                                               label_attribute=None)

    degrees = np.array([degree for node, degree in nx.degree(graph)], dtype=int) 
    
    
    indices_tips = np.where(degrees==1)[0]  ## degrees=1 -> pointes 
    indices_hyphes = np.where(degrees==2)[0]  ## degrees=2 intermédiaires
    indices_nodes = np.where(degrees==3)[0]  ## degrees=3 -> branchements 

#    x_ord=x_ord[indices_tips]+center[0]
#    y_ord=y_ord[indices_tips]+center[1]


    print('Nombre apex:')
    print(len(indices_tips))
    print('Nombre noeuds:')
    print(len(indices_nodes))
    print('Longueur totale:')
    print(ltot)
    
    return len(indices_tips), len(indices_nodes), ltot

