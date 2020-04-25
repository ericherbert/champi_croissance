import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func_power_law( XX, a, b):
    return a * XX**b

def func_exp( XX, a, b):
    return a * np.exp( b*XX )

def func_lin( XX, a, b):
    return  a * XX + b

def Ltot_error(XX):
    # retourne l'estimateur de l'incertitude sur la longueur totale en mm
    a = 0.27 # 0.027
    b = 0.610
    return a * XX**b

def plot_data( x, y):
    #plt.semilogy(x,y,'k.')
    plt.plot( x, y, 'k.')
    error =  Ltot_error( y )
    plt.errorbar( x, y, yerr=error, fmt='k.')

def fit_exp_error( x, y, error, print_fit='0'):
    popt, pcov = curve_fit( func_exp, x, y, sigma=error, absolute_sigma=True, p0=[ 5, 0.005 ] )
    if print_fit :
        print( 'fonction fit f(t) = a * np.exp( b*t )' )
        print( ' b = ' + str(popt[1]) + ' +/- ' + str( np.sqrt(np.diag(pcov))[1] ) )
        print( ' a = ' + str(popt[0]) + ' +/- ' + str( np.sqrt(np.diag(pcov))[0] ) )
    return popt, pcov


def plot_fit( x, popt, pcov):
    plt.plot( x, func_exp( x, *popt), '-k')
    nstd = 3
    popt_up = popt + nstd * np.sqrt(np.diag(pcov))
    popt_dw = popt - nstd * np.sqrt(np.diag(pcov))
    fit_up = func_exp(  x, *popt_up)
    fit_dw = func_exp(  x, *popt_dw)
    plt.fill_between( x, fit_up, fit_dw, alpha=.25, color='k')
    return



def main( x, y):
    error =  Ltot_error( y )
    popt, pcov = fit_exp_error( x, y, error, 1)
    plot_fit( x, popt, pcov)
    return popt, pcov

if __name__ == "__main__":
    x = np.linspace(1,10,100)
    y = np.exp( x) * (np.random.rand(100)+1)/5
    plt.close('all')
    plt.figure('temp')
    plot_data( x, y)
    main( x, y)
    plt.show()
