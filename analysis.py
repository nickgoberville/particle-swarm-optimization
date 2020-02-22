#! /usr/bin/env python3

import ackley_solver as ack
import matplotlib.pyplot as plt
import numpy as np
import my_pso_v2 as pso
import cost_functions as func
import time

fig, ax = plt.subplots(2)
plt.xlabel('Accuracy', fontsize=25)
Nps = range(10,101,10)
for l in Nps:
    points = []
    costvalues = []
    iters = []
    run_times = []
    acc_varies = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]
    runs = 5
    for i in acc_varies:
        #sum_pnt = 0
        sum_val = 0
        sum_k = 0
        sum_rt = 0
        for j in range(runs):
            start_time = time.time()
            pnt, val, k, parts = pso.pso(func.arora_431, 2, l, acc=i)
            stop_time = time.time()
            run_time = stop_time - start_time
            #sum_pnt += pnt
            sum_val += val
            sum_k += k
            sum_rt += run_time
        #new_pnt = sum_pnt/runs
        new_val = sum_val/runs
        new_k = sum_k/runs
        new_rt = sum_rt/runs
        #points.append(new_pnt)
        costvalues.append(new_val)
        iters.append(new_k)
        run_times.append(new_rt)

    ax[0].plot(acc_varies, iters, label='Np = {}'.format(l))
    ax[1].plot(acc_varies, run_times, label='Np = {}'.format(l))
    
ax[0].legend()
ax[0].set_xscale('log')
ax[0].set_ylabel('Iterations', fontsize=25)

#ax[1].legend()
ax[1].set_xscale('log')
ax[1].set_ylabel('Run Time (s)', fontsize=25)
plt.show()


print('Minimum = {}; Point = {}; Iterations = {}'.format(val, pnt, k))
print('PSO Runtime = {}'.format(run_time))
    