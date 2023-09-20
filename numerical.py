from scipy.stats import qmc
import matplotlib.pyplot as plt
import numpy as np
import random
# Q1
# def LGC(a,c, m:int, z):
#     output = []
#     for i in range(m):
#         mod = (a*z+c)%m
#         output.append(mod/m)
#         z = mod
#     return output
# a=6.5
# c=0.7
# m=60
# z=2.23
# output = LGC(a,c,m,z)
#
# plt.scatter(np.arange(1,21,1), output[0:20], color='r')
# plt.scatter(np.arange(21,41,1), output[20:40], color='b')
# plt.scatter(np.arange(41,61,1), output[40:60], color='g')
# plt.show()
#
# # Q2
# sampler = qmc.Sobol(d=2, scramble=True)
# sample = sampler.random(200)
# sample_builtin = []
# for i in range(200):
#     sample_builtin +=[[random.uniform(0, 1),random.uniform(0, 1)]]
# sample = np.array(sample)
# sample_builtin = np.array(sample_builtin)
# plt.scatter(sample[:,0], sample[:,1], color='r')
# plt.scatter(sample_builtin[:,0],sample_builtin[:,1], color='b')
# plt.show()

#Q3
# Uniform
def uniform(a,b,N):
    u = np.random.uniform(0,1,N)
    x= a +(b-a)*u
    return x
#exponential
def exponential(lamada,N):
    u = np.random.uniform(0, 1, N)
    x = -1*lamada*np.log(u)
    return x
# Bernouli
def Bernouli(p,N):
    u = np.random.uniform(0, 1, N)
    x = []
    for a in u:
        if a<p:
            x.append(1)
        else:
            x.append(0)
    return x
# discrete distribution
def discrete(p1,p2,p3,p4,N):
    u = np.random.uniform(0, 1, N)
    x = []
    for a in u:
        if a <p1[1]:
            x.append(p1[0])
        elif a <p1[1]+p2[1]:
            x.append(p2[0])
        elif a <p1[1]+p2[1]+p3[1]:
            x.append(p3[0])
        else:
            x.append(p4[0])
    return x
# print(discrete([-1,0.1],[2,0.3],[3,0.4],[-4,0.2],10))
#Possion
def possion(lamda,N):
    x=[]
    for i in range(N):
        t = 0
        count = 0
        while t<=1:
            tao = exponential(lamda,1)
            t+=tao
            count+=1
        x.append(count-1)
    return x
#Binomial
def binomial(n,p,N):
    x=[]

    for a in range(N):
        x.append(sum(Bernouli(p,n)))
    return x
#Gamma
def Gamma(a,b,N):
    x=[]
    for i in range(N):
        x.append(sum(exponential(1/b,a)))
    return x
