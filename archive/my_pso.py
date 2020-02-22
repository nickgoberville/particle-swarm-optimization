#! /usr/bin/env python3

import cost_functions as func
import random
import time

class particle:
    # Initialize Particles
    def __init__(self, bounds, n):
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
            self.position.append(pos)       # Initial Position
            self.velocity.append(0)         # Initial Velocity

    # Evaluate a particle
    def evaluate_particle(self, costFunc):
        self.costvalue = costFunc(self.position)
        try:
            if self.costvalue < self.best_costvalue:
                print('\n...Updating Best Position from {}'.format(self.best_position))
                self.best_costvalue = self.costvalue
                self.best_position = self.position
                print('To {}...'.format(self.best_position))
            elif self.costvalue > self.best_costvalue:
                self.position = self.best_position
        except:
            print('Here')
            self.best_costvalue = self.costvalue
            self.best_position = self.position
        self.costvalue = costFunc(self.position)

    def update_particle_velocity(self, n, global_best_position, c1, c2, w):
        for i in range(n):
            r1 = random.random()
            r2 = random.random()
            cognitive = c1*r1*(self.best_position[i] - self.position[i])
            social = c2*r2*(global_best_position[i] - self.position[i])
            self.velocity[i] = w*self.velocity[i] + cognitive + social

    def update_particle_position(self, n, bounds):
        for i in range(n):
            self.position[i] = self.position[i] + self.velocity[i]

            try:
                if self.position[i] < bounds[i][0]:
                    self.position[i] = bounds[i][0]
                elif self.position[i] > bounds[i][1]:
                    self.position[i] = bounds[i][1]
            except:
                continue


class swarm:
    def __init__(self, Np, bounds, n):
        self.design_point = []
        for i in range(Np):
            self.design_point.append(particle(bounds, n))
            #print("i= {}; point = {}".format(i, self.design_point[i].position))

    def evaluate_swarm(self, costFunc, Np):
        for i in range(Np):
            self.design_point[i].evaluate_particle(costFunc)
            #print("i: {} Point: {} Costvalue: {} Best_Costvalue: {}".format(i, self.design_point[i].position, self.design_point[i].costvalue, self.design_point[i].best_costvalue))
            try:
                if design_point[i].costvalue < global_best_costvalue:
                    self.global_best_costvalue = float(self.design_point[i].costvalue)
                    self.global_best_position = list(self.design_point[i].position)
            except:
                self.global_best_costvalue = float(self.design_point[i].costvalue)
                self.global_best_position = list(self.design_point[i].position)
            #print("NEW i: {} Point: {} Costvalue: {} Best_Costvalue: {}\n\n".format(i, self.design_point[i].position, self.design_point[i].costvalue, self.design_point[i].best_costvalue)) 
            #if i >= 0 and i < 10:
            #    time.sleep(5)
            

    def update_swarm(self, Np, c1, c2, w, bounds, n):
        sum = 0
        for i in range(Np):
            ###### DELETE ######
            #stop = 0
            #if i == stop:
            #    print("i = {}; point = {}; best_point = {}; cost_value = {}".format(i, self.design_point[i].position, self.design_point[i].best_position, self.design_point[i].best_costvalue))            
            ###### DELETE ######
            
            self.design_point[i].update_particle_velocity(n, self.global_best_position, c1, c2, w)
            self.design_point[i].update_particle_position(n, bounds)
            
            ###### DELETE ######
            #if i == stop:
            #    print("i = {}; NEW_point = {}; best_point = {}; cost_value = {}\n\n".format(i, self.design_point[i].position, self.design_point[i].best_position, self.design_point[i].best_costvalue))        
            #    time.sleep(5)
            ###### DELETE ######

            sum += self.design_point[i].best_costvalue
        diff = abs(sum/Np - self.global_best_costvalue)
        print('diff: {}\n'.format(diff))
        return diff

def pso(costFunc, n, Np, x0=None, bounds=None, k_max=100, acc=0.1, c1=1, c2=2, w=0.5):
    points = swarm(Np, bounds, n)
    #print(points)
    k = 0
    diff = 100
    while k < k_max and diff > acc:
        print('====================  k = {}  ==================='.format(k)) 
        points.evaluate_swarm(costFunc, Np)
        ######
        print("\npoint = {}; best_point = {}; cost_value = {}; best_cost_value = {}".format(points.design_point[0].position, points.design_point[0].best_position, points.design_point[0].costvalue, points.design_point[0].best_costvalue))            
        print('Best_point_global = {}; Best_costval_global = {}; velocity = {}'.format(points.global_best_position, points.global_best_costvalue, points.design_point[0].velocity))
        ######
        diff = points.update_swarm(Np, c1, c2, w, bounds, n)
        time.sleep(2)
        k += 1
    return points.global_best_position, points.global_best_costvalue, k

def main():
    function = func.arora_422
    n = func.num_vars(function)
    print(pso(function, n, 10))#, bounds=[(-30,30)]))

if __name__ == '__main__':
    main()
