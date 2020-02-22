#! /usr/bin/env python3

import cost_functions as func
import random
import time
import numpy as np

# Creating a class for particle, will contain all values of the particles in the swarm
class particle:
    def __init__(self, bounds, n):
        '''
        Initialization of the particle's position and velocity.
        '''
        self.position = []
        self.velocity = []
        self.best_position = []
        for i in range(n):
            r = random.random()
            if bounds:                     
                lower = bounds[i][0]
                upper = bounds[i][-1]
            else:                           
                lower = random.random()*-100
                upper = random.random()*100
            pos = lower + r*(upper-lower)
            self.position.append(pos)      
            self.velocity.append(0)         

    def evaluate_particle(self, costFunc):
        '''
        Calculation of the cost value for a particle
        '''
        self.costvalue = costFunc(self.position)
        try:
            if self.costvalue < self.best_costvalue:
                self.best_costvalue = self.costvalue
                self.best_position = self.position
            elif self.costvalue > self.best_costvalue:
                self.position = self.best_position
        except:
            self.best_costvalue = self.costvalue
            self.best_position = self.position
        self.costvalue = costFunc(self.position)

    def update_particle_velocity(self, n, global_best_position, c1, c2, w):
        '''
        Updating particle velocity using cognitive and social influences
        '''
        for i in range(n):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1*r1*(self.best_position[i] - self.position[i])
            social = c2*r2*(global_best_position[i] - self.position[i])
            self.velocity[i] = w*self.velocity[i] + cognitive + social

    def update_particle_position(self, n, bounds):
        '''
        Updating particle position using previous position and current velocity
        '''
        for i in range(n):
            self.position[i] = self.position[i] + self.velocity[i]
            try:
                if self.position[i] < bounds[i][0]:
                    self.position[i] = bounds[i][0]
                elif self.position[i] > bounds[i][1]:
                    self.position[i] = bounds[i][1]
            except:
                continue

def pso(costFunc, n, Np, x0=None, bounds=None, k_max=100, acc=0.1, c1=2, c2=2, w=0.5):
    '''
    Particle Swarm Optimization
    '''
    # Initialize best global costvalue, position, and the swarm list
    best_val_global = -1
    best_position_global = []
    swarmm = []

    # Appending all particles to the swarm list
    for i in range(Np):
        swarmm.append(particle(bounds, n))

    # Set iteration to 0
    k=0           
    parts = np.zeros((k_max, Np, n))        

    # Initialize variable used to calculate accuracy
    diff=100
    while k < k_max and diff > acc:
        
        # Evaluate all particles and update global bests
        for i in range(Np):
            swarmm[i].evaluate_particle(costFunc)
            if swarmm[i].costvalue < best_val_global or best_val_global==-1:
                best_val_global=float(swarmm[i].costvalue)
                best_position_global=list(swarmm[i].position)
        
        # Update particle velocity and position
        sum=0
        for i in range(Np):
            swarmm[i].update_particle_velocity(n, best_position_global, c1, c2, w)
            swarmm[i].update_particle_position(n, bounds)
            sum+= swarmm[i].best_costvalue
            parts[k, i] = np.array(swarmm[i].position)

        # Calculate accuracy
        diff=abs(sum/Np-best_val_global)
        
        # Next iteration
        k += 1
    return best_position_global, best_val_global, k, parts

def main():
    # Testing function
    function = func.arora_431
    n = func.num_vars(function)
    pos, val, k, parts = pso(function, n, 20, acc=0.01)
    print('Minimum = {}; Optimum_point = {}; Iter = {}'.format(val, pos, k))

if __name__ == '__main__':
    main()
