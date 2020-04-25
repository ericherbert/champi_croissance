# coding: utf-8
# center = centre en pixel relevé via ImageJ
# deltat = intervalle de temps entre 2 panos. J'ai pris 1040 secondes pour les acquisitions sans log
# milieu = milieu de culture
# operateur = personnes qui a fait la manip
# Light = WHITE ou FLUO

# pour utiliser:
# import DictManips as DM
# manips = DM.MANIPS( 0)
# names = [manips[inc]['name'] for inc in manips.keys()]
# for name,inc in zip( names , range(len(names)) ) :
#     plot_all_nodes.main( name )

"""
entrée vierge:
    update = {'name' : '2019_05_02_P_S_M0' ,
                'center' : (0,0),
                'deltat': 1,
                'milieu' : 'Mx',
                'operateur' : 'temp' }
"""


def MANIPS( print_lst):
    DictKeys = ManipList()
    temp = dict.fromkeys(DictKeys, None) 

    ############################ M2 * 2
    inc = 1
    update = {'name' : '2019_04_01_P_S_M22x' ,
              'center' : (2735,3400),
              'deltat': 1037,
              'milieu' : 'M2x2',
              'operateur' : 'sabrina',
              'marker' : 'r.',
              'color' : 'r',
              'pix' : 3.516,
              'Nmax':78}
    tempus_fugit = {inc:update}

    inc += 1
    update = {'name' : '2019_04_04_P_S_M22x' ,
              'center' : (2850,3280),
              'deltat': 1037,
              'milieu' : 'M2x2',
              'operateur' : 'sabrina',
              'marker' : 'r+',
              'color' : 'r',
              'pix' : 3.516,
              'Nmax':75}
    tempus_fugit[inc] = update

            ############################ M2

    inc += 1
    update = {'name' : '2019_04_09_P_S_M2' ,
              'center' : (2883,3337),
              'deltat' : 1037,
              'milieu' : 'M2',
              'operateur' : 'sabrina',
              'marker' : 'g.',
              'color' : 'g',
              'pix' : 3.516,
              'Nmax':71}
    tempus_fugit[inc] = update

    inc += 1
    update = {'name' : '2019_04_11_P_S_M2' ,
              'center' : (2970,3324),
              'deltat': 1037,
              'milieu' : 'M2',
              'operateur' : 'sabrina',
              'color' : 'g',
              'marker' :  'g+',
              'pix' : 3.516,
              'Nmax':76}
    tempus_fugit[inc] = update

    inc += 1
    update = {'name' : '2019_04_29_P_S_M2' ,
              'center' : (2800,3300),
              'deltat': 1037,
              'milieu' : 'M2',
              'operateur' : 'sabrina',
              'marker' : 'gx',
              'color' : 'g',
              'pix' : 3.516,
              'Nmax':72}
    tempus_fugit[inc] = update

        ############################ M2 * 0.5

    inc += 1
    update = {'name' : '2019_03_28_P_S_M2_05x' ,
              'center' : (3000,3370),
              'deltat': 1037,
              'milieu' : 'M2x0.5',
              'operateur' : 'sabrina',
              'marker' : 'b.',
              'color' : 'b',
              'pix' : 3.516,
              'Nmax':66}
    tempus_fugit[inc] = update

    inc += 1
    update = {'name' : '2019_04_18_P_S_M2_05x' ,
              'center' : (2800,3450),
              'deltat': 1037,
              'milieu' : 'M2x0.5',
              'operateur' : 'sabrina',
              'marker' :  'b+',
              'color' : 'b',
              'pix' : 3.516,
              'Nmax':81}
    tempus_fugit[inc] = update


        ############################ M0

    inc += 1
    update = {'name' : '2019_03_27_P_S_M0' ,
              'center' : (3005,3336),
              'deltat': 1037,
              'milieu' : 'M0',
              'operateur' : 'sabrina',
              'marker' :  'k.',
              'color' : 'k',
              'pix' : 3.516,
              'Nmax':76}
    tempus_fugit[inc] = update

    inc += 1
    update = {'name' : '2019_04_10_P_S_M0' ,
              'center' : (2950,3510),
              'deltat': 1037,
              'milieu' : 'M0',
              'operateur' : 'sabrina',
              'marker' : 'k+',
              'color' : 'k',
              'pix' : 3.516,
              'Nmax':76 }
    tempus_fugit[inc] = update

    inc += 1
    update = {'name' : '2019_05_02_P_S_M0' ,
              'center' : (2930,3330),
              'deltat': 1037,
              'milieu' : 'M0',
              'operateur' : 'sabrina',
              'marker' :  'kx',
              'color' : 'k',
              'pix' : 3.516,
              'Nmax':76}
    tempus_fugit[inc] = update


    if print_lst:
        print(' -- ')
        print(' -- Liste des manips disponibles :')
        print(' -- ')
        print( [tempus_fugit[inc]['name'] for inc in tempus_fugit.keys()] )

    return tempus_fugit



def ManipList( ):

    DictKeys = {'name',
                'center',
                'deltat',
                'milieu' ,
                'operateur',
                'ImageSize',
                'Light',
                'FrameNumber'}

    return DictKeys


def main():
    MANIPS( 1)

if __name__ == "__main__":
    main()
