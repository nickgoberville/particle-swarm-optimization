#! /usr/bin/env python3
import random
import cost_functions as func
import numpy as np
import time

class Particle:
    def __init__(self, x0):
        self.position=[]
        self.velocity=[]
        self.pos_best=[]
        self.err_best=-1
        self.err=-1

        for i in range(n):
            self.position.append(x0[i])
            self.velocity.append(random.uniform(-1,1))

    def evaluate(self, costFunc):
        self.err=costFunc(self.position)
        #print(self.part_val)

        if self.err<self.err_best or self.err_best==-1:
            self.pos_best=self.position
            self.err_best=self.err


    def update_velocity(self, pos_best_g):
        c1, c2, w = 1, 2, 0.5
        for i in range(n):
            r1 = random.random()
            r2 = random.random()
            vel_cognitive=c1*r1*(self.pos_best[i]-self.position[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position[i])
            self.velocity[i]=w*self.velocity[i]+vel_cognitive+vel_social

    def update_position(self, bounds):
        for i in range(n):
            self.position[i]=self.position[i]+self.velocity[i]

            if self.position[i]<bounds[i][0]:
                self.position[i]=bounds[i][0]

            if self.position[i]>bounds[i][1]:
                self.position[i]=bounds[i][1]

def pso(costFunc, x0, bounds, Np=50, k_max=100, c1=2, c2=2, w=0.5):
    global n
    n=len(x0)

    err_best_g=-1
    pos_best_g=[]
    
    parts=np.zeros((k_max,Np,n))

    swarm=[]
    for i in range(Np):
        swarm.append(Particle(x0))

    k=0
    while k < k_max:
        for i in range(Np):
            swarm[i].evaluate(costFunc)

            if swarm[i].err<err_best_g or err_best_g==-1:
                pos_best_g=list(swarm[i].position)
                print('swarm: {} pos_best_g: {}'.format(swarm[i].position,pos_best_g))
                err_best_g=float(swarm[i].err)

        for i in range(Np):
            swarm[i].update_velocity(pos_best_g)
            swarm[i].update_position(bounds)
            parts[k,i]=np.array(swarm[i].position)
        #print(swarm[i].position)
        #print(swarm[i].velocity)
        #print('Iter: {} Position: {} Velocity: {}'.format(k,swarm[0].position,swarm[0].velocity))
        #time.sleep(1) 
        k+=1

    print('x_G = ' + str(pos_best_g))
    print('minimum = ' + str(err_best_g))
    return err_best_g, parts

def main():
    inf = float('inf')
    bounds = [(-inf,inf),(-inf,inf)]
    initial = [6,5]
    pso(func.random_1, initial, bounds)


if __name__ == '__main__':
    main()

