#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import my_pso_v2 as pso
import time
import cost_functions as func
import ackley_solver as ack

plt.rcParams['font.family'] = 'Times New Roman'
fig = plt.figure()
bounds = [(-15,15), (-15,15)]
ax = plt.axes(xlim=bounds[0], ylim=bounds[1])
line, = ax.plot([],[], 'o', color='r', markeredgewidth = 1, markeredgecolor='k')
ax.grid()
ax.set_xlabel('$x_1$', fontsize=30)
ax.set_ylabel('$x_2$', fontsize=30)

def init():
    line.set_data([], [])
    return line,

Np = 100
function = ack.function
if function == ack.function:
    x, y, f = ack.matlab_import()
    ack.interp_mat(x, y, f)

n = func.num_vars(function)
pos, val, k, parts = pso.pso(function, n, 100, bounds=bounds, acc=0.0001)
global x1, x2
x1 = parts[:,:,0]
x2 = parts[:,:,1]
xdata, ydata= [], []

def animate(i):
    while i < k:
        xdata = x1[i]
        ydata = x2[i]
        line.set_data(xdata, ydata)
        plt.title('Iteration: {}'.format(i), fontsize=30)
        return line,


ani = animation.FuncAnimation(fig, animate, init_func=init, interval=300)
plt.show()

