#! /usr/bin/env python3
import random as rand
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from pso_params import *

# Cost function
def func(vect):
    return 400*(0.5*3.1415*vect[0]**2 + 3.1415*vect[0]*vect[1]) - 350*vect[1] - 200*vect[0] + 80

def particle_swarm(f=func):
    # Initial position vector population & x_G determination
    for i in range(Np):
        for j in range(n):
            x[i,j] = x_L[i,j] + rand.random()*(x_U[i,j] - x_L[i,j])
        x_p[i] = x[i]
        try:
            if lowest_f > f(x[i]):
                x_G = x[i]
                lowest_f = f(x[i])
        except:
            lowest_f = f(x[i])
            x_G = x[i]

    k = 1
    while k < k_max:
        for i in range(Np):
            r1 = rand.random() # Random number between 0 and 1
            r2 = rand.random() # Random number between 0 and 1
            v[i] = v[i] + c1*r1*(x_p[i] + c2*r2*(x_G - x[i]))
            x[i] = x[i] + v[i]

            # Check x[i] is within lower, upper limits
            for j in range(n):
                if (x[i,j] <= x_L[i,j]) or (x[i,j] >= x_U[i,j]):
                    x[i] = x_p[i]

            # Check if x[i] is better than x_p[i]
            if f(x[i]) <= f(x_p[i]):
                x_p[i] = x[i]

            if f(x_p[i]) <= f(x_G):
                x_G = x_p[i]
            parts[k,i] = x[i]
        k += 1

    return x_G, parts

if __name__ == "__main__":
    optimum, parts = particle_swarm()
    print("x_G: {}".format(optimum))
    print("Cost: {}".format(func(optimum)))
    
