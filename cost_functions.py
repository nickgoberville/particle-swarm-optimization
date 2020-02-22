#! /usr/bin/env python3

def random_1(x):
    out = 0
    for i in range(len(x)):
        out += x[i]**2
    return out - 20

def random_2(x):
    return 42*x[0]**3 - 32*x[1]**2 + x[0]*x[1]*99 - 1000

def random_3(x):
    return 10000+5*x[0]+(1/9)*x[0]**2

def arora_422(x):
    return 3*x[0]**2 + 2*x[0]*x[1] + 2*x[1]**2 + 7

def arora_423(x):
    return x[0]**2 + 4*x[0]*x[1] + x[1]**2 + 3

def arora_442(x):
    return (x[0]-10*x[1])**2 + 5*(x[2]-x[3])**2 + (x[1]-2*x[2])**4 + 10*(x[0]-x[3])**4

def arora_424(x):
    return x[0]**3 + 12*x[0]*x[1]**2+2*x[1]**2+5*x[0]**2+3*x[1]

def arora_427(x):
    return x[0]**2 + x[0]*x[1] + x[1]**2

def arora_429(x):
    return x[0] - 10/(x[0]*x[1]) + 5*x[1]

def arora_430(x):
    return x[0]**2 - 2*x[0] + 4*x[1]**2 - 8*x[1] + 6

def arora_431(x):
    x1 = x[0]
    x2 = x[1]
    return 3*x1**2 - 2*x1*x2 + 5*x2**2 + 8*x1

def num_vars(costFunc):
    '''
    Determine the number of variables in a function.
    '''
    x = [0]
    while True:
        try:
            costFunc(x)
            return len(x)
        except:
            x.append(0)
