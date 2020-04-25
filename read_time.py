# coding: utf-8

# donne le temps en secondes du fichier file
# le format doit être:
# ['92', '2019-10-10', '14:51:31.145424']



def read_time( file):

    from datetime import datetime
    import numpy as np
    import sys

    f = np.genfromtxt( file, skip_header=14, dtype=str)

    time = np.zeros(np.shape(f)[0])
    for inc in range( 0, np.shape(f)[0]-1):
#    a[inc] = datetime.strptime(tt[2,1],"%Y-%m-%d")
        temp = datetime.strptime( f[inc+1,2], "%H:%M:%S.%f") - datetime.strptime( f[inc,2], "%H:%M:%S.%f")
        time[inc+1] = temp.seconds

    time = np.cumsum( time)

    return time

if __name__ == "__main__":
    import os
    import sys

#    file = '../Clara/2019_10_09_P_S_M2/log.txt'
    file = sys.argv[1]

    if os.path.isfile( file ):
        time = read_time( file)
    #    aa = np.genfromtxt( file, dtype=str)
        print( time)
    else:
        print( ' -- FILE < ' + file  + ' > DOES NOT EXIST -- ' )

