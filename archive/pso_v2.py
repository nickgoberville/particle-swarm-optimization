#! /usr/bin/env python3
import random
import cost_functions as func
import numpy as np
import time

class Particle:
    def __init__(self, bounds):
        self.position=[]
        self.velocity=[]
        self.position_best=[]
        self.part_val=-1
        self.part_val_best=-1
        self.initial_position=[]

        for i in range(n):
            r = random.random()
            x_l = bounds[i][0]
            x_u = bounds[i][-1]
            initial_val=x_l+r*(x_u-x_l)
            self.initial_position.append(initial_val)

        for i in range(n):
            self.position.append(self.initial_position[i])
            self.velocity.append(0)

    def evaluate(self, costFunc):
        self.part_val=costFunc(self.position)

        if self.part_val<self.part_val_best or self.part_val_best==-1:
            self.part_val_best=self.part_val
            self.position_best=self.position
        elif self.part_val>self.part_val_best and self.part_val_best!=-1:
            self.position=self.position_best

    def update_velocity(self, position_global_best, c1, c2, w):
        #c1, c2, w = 2, 2, 0.5
        for i in range(n):
            r1 = random.random()
            r2 = random.random()
            vel_cognitive=c1*r1*(self.position_best[i]-self.position[i])
            vel_social=c2*r2*(position_global_best[i]-self.position[i])
            self.velocity[i]=w*self.velocity[i]+vel_cognitive+vel_social

    def update_position(self, bounds):
        for i in range(n):
            self.position[i]=self.position[i]+self.velocity[i]

            if self.position[i]<bounds[i][0]:
                self.position[i]=bounds[i][0]

            if self.position[i]>bounds[i][1]:
                self.position[i]=bounds[i][1]

   # def max_particle_error(self): average-global best < acc




def pso(costFunc, x0, bounds, Np=50, k_max=100, acc=0.001, c1=2, c2=2, w=0.5):
    global n
    n=len(x0)

    best_val_global=-1
    position_global_best=[]
    #max_error=1
    
    parts=np.zeros((k_max,Np,n))

    swarm=[]
    for i in range(Np):
        swarm.append(Particle(bounds))
        #print(swarm[i].position)
    diff = 100
    k=0
    while k < k_max and diff > acc:
        for i in range(Np):
            swarm[i].evaluate(costFunc)
            
            


            if swarm[i].part_val<best_val_global or best_val_global==-1:
                best_val_global=float(swarm[i].part_val)
                position_global_best=list(swarm[i].position)
                #print('new_global_best: {}'.format(position_global_best))
        sum=0
        for i in range(Np):
            swarm[i].update_velocity(position_global_best, c1, c2, w)
            swarm[i].update_position(bounds)
            
            parts[k,i]=np.array(swarm[i].position)

            sum += swarm[i].part_val_best 
        #print('Iter: {} Position: {} Velocity: {}'.format(k,swarm[0].position,swarm[0].velocity))
        #time.sleep(1)
        #print(swarm[i].position)
        #print(swarm[i].velocity)
        #print(k)
        diff=abs(sum/Np-best_val_global)
        #print(diff) 
        k+=1
    #print('inter: {}'.format(k))
    #print('x_G = {}'.format(position_global_best))
    #print('minimum = ' + str(best_val_global))
    return best_val_global, parts, position_global_best, k

def main():
    start_time = time.time()
    #inf = float('inf')
    bounds = [(-300000,300000), (-300000,300000),]# (-30,30),(-10,10)]
    initial = [6, 6]# 6, 6]
    val, parts, soln, k = pso(func.arora_424, initial, bounds)
    print("Soln = {}; Val = {}; iterations = {}".format(soln, val, k))
    print("Runtime: {}".format(time.time() - start_time))

if __name__ == '__main__':
    main()

