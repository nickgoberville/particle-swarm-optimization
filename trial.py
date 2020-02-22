#! /usr/bin/env python3

import my_pso_v2 as pso
import cost_functions as func

function = func.arora_431
n = func.num_vars(function)

pos, val, k, parts = pso.pso(function, n, 50)
print(pos)
print(function(pos))
x = pos
print(3*x[0]**2 - 2*x[0]*x[1] + 5*x[1]**2 + 8*x[0])