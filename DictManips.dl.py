# coding: utf-8
# center = centre en pixel relevé via ImageJ
# deltat = intervalle de temps entre 2 panos. J'ai pris 1040 secondes pour les acquisitions sans log
# milieu = milieu de culture
# operateur = personnes qui a fait la manip
# Light = WHITE ou FLUO

# pour utiliser:
# import DictManips as DM
# DictKeys, lst = DM.ManipList(1) retourne la liste de toutes les manips et les keys disponibles
# PARAMS =  DM.MANIPS(manip) retourne les parametres de la manip 'manip'
# exemple d'utilisation: PARAMS['name'] donne le nom


"""
entrée vierge:
    elif manip == '2019_05_02_P_S_M0':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1,
                  'milieu' : 'Mx',
                  'operateur' : 'temp' }
"""

def MANIPS(manip):

    DictKeys, lst = ManipList(0)
    PARAMS = dict.fromkeys(DictKeys, None) 

    ############################ M2 * 2

    if manip == '2019_04_01_P_S_M22x':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1037,
                  'milieu' : 'M2x2',
                  'operateur' : 'sabrina',
                  'marker' : 'ro'}

    elif manip == '2019_04_04_P_S_M22x':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1037,
                  'milieu' : 'M2x2',
                  'operateur' : 'sabrina',
                  'marker' : 'r*'}


        ############################ M2

    elif manip == '2019_04_09_P_S_M2':
        update = {'name' : manip ,
                  'center' : (2883,3337),
                  'deltat' : 1037,
                  'milieu' : 'M2',
                  'operateur' : 'sabrina',
                  'marker' : 'go'}

    elif manip == '2019_04_11_P_S_M2':
        update = {'name' : manip ,
                  'center' : (2970,3324),
                  'deltat': 1037,
                  'milieu' : 'M2',
                  'operateur' : 'sabrina',
                  'marker' :  'g*'}

    elif manip == '2019_04_29_P_S_M2':
        update = {'name' : manip ,
                  'center' : (2970,3324),
                  'deltat': 1037,
                  'milieu' : 'M2',
                  'operateur' : 'sabrina',
                  'marker' : 'gs'}

        ############################ M2 * 0.5

    elif manip == '2019_03_28_P_S_M2_05x':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1037,
                  'milieu' : 'M2x0.5',
                  'operateur' : 'sabrina',
                  'marker' : 'bo'}

    elif manip == '2019_04_18_P_S_M2_05x':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1037,
                  'milieu' : 'M2x0.5',
                  'operateur' : 'sabrina',
                  'marker' :  'b*'}


        ############################ M0

    elif manip == '2019_03_27_P_S_M0':
        update = {'name' : manip ,
                  'center' : (3005,3336),
                  'deltat': 1037,
                  'milieu' : 'M0',
                  'operateur' : 'sabrina',
                  'marker' :  'ko'}

    elif manip == '2019_04_10_P_S_M0':
        update = {'name' : manip ,
                  'center' : (2950,3510),
                  'deltat': 1037,
                  'milieu' : 'M0',
                  'operateur' : 'sabrina',
                  'marker' : 'k*' }

    elif manip == '2019_05_02_P_S_M0':
        update = {'name' : manip ,
                  'center' : (0,0),
                  'deltat': 1037,
                  'milieu' : 'M0',
                  'operateur' : 'sabrina',
                  'marker' :  'ks'}
    else:
        PARAMS = ' ERROR  '
        print( '--\n\t -- PAS DE MANIP À CE NOM \n\t --')


    PARAMS.update( update)

    return PARAMS

def ManipList( print_lst ):

    lst = ['2019_04_01_P_S_M22x',
           '2019_04_04_P_S_M22x',
           '2019_04_09_P_S_M2',
           '2019_04_11_P_S_M2',
           '2019_04_29_P_S_M2',
           '2019_03_28_P_S_M2_05x',
           '2019_04_18_P_S_M2_05x',
           '2019_03_27_P_S_M0',
           '2019_04_10_P_S_M0',
           '2019_05_02_P_S_M0' ]

    DictKeys = {'name',
                'center',
                'deltat',
                'milieu' ,
                'operateur',
                'ImageSize',
                'Light',
                'FrameNumber'}

    if print_lst:
        print(' -- ')
        print(' -- Liste des manips disponibles :')
        print(' -- ')
        print(lst)

    return DictKeys, lst


def main():

    DictKeys, lst = ManipList(0)

    fname = lst[0] # '2019_04_09_P_S_M2'
    PARAMS = MANIPS(fname)

if __name__ == "__main__":
    main()
