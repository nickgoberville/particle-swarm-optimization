#! /usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import matplotlib
import my_pso_v2 as pso
import scipy.io 
import numpy as np
import scipy.interpolate as itp
import time

plt.rcParams['font.family'] = 'Times New Roman'

def matlab_import():
    '''
    Input the desired .mat file to minimize and define x, y, and f matrices
    '''
    mat_file = 'Ackley.mat'
    mat = scipy.io.loadmat(mat_file)
    if mat_file == 'Ackley.mat':
        f = mat['f']
        x = mat['x'][:]
        y = mat['y'][:]
    elif mat_file == 'Anaxagoras.mat':
        f = mat['vA']
        x = mat['xA'][:]
        y = mat['yA'][:]
    elif mat_file == 'Von_Karman.mat':
        f = mat['vq']
        x = mat['xq'][:]
        y = mat['yq'][:]
    print(x.shape)
    return x, y, f

def plotit(x, y, f):
    '''
    Generation of the 3D Plot of the .mat file data
    '''
    X, Y = np.meshgrid(x, y)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X,Y,f,cmap=cm.plasma, antialiased=True)
    ax.set_title('Ackley Data File', fontsize=25)
    ax.set_xlabel('X (input)', fontsize=15)
    ax.set_ylabel('Y (input)', fontsize=15)
    ax.set_zlabel('f (cost function)', fontsize=15)
    ax.xaxis.set_tick_params(labelsize=15)
    ax.yaxis.set_tick_params(labelsize=15)
    ax.zaxis.set_tick_params(labelsize=15)

    #ax.yaxis._axinfo['label']['space_factor'] = 50.0
    #ax.xaxis._axinfo['label']['space_factor'] = 3.0 
    #plt.title('Ackley Data File')
    plt.show()

def interp_mat(x, y, f):
    global x_vals
    x_vals = itp.interp2d(x, y, f)

def function(x):
    '''
    Function used for the optimization algorithm
    '''
    return x_vals(x[0], x[1])

def solver(costFunc, n, Np, x0=None, bounds=None, k_max=100, acc=0.1, c1=2, c2=2, w=0.5):
    x, y, f = matlab_import()
    plotit(x,y,f)
    interp_mat(x, y, f)
    start_time = time.time()
    pnt, val, k, parts = pso.pso(costFunc, n, Np, x0, bounds, k_max, acc, c1, c2, w)
    stop_time = time.time()
    run_time = stop_time - start_time
    return pnt, val, k, run_time, parts

def main():
    '''
    Main Function to plot .mat data and optimize function
    '''
    pnt, val, k, run_time, parts = solver(function, 2, 100, acc=0.0001)
    print('Minimum = {}; Point = {}; Iterations = {}'.format(val, pnt, k))
    print('PSO Runtime = {}'.format(run_time))
     

if __name__ == '__main__':
    main()