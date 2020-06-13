#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 00:42:30 2020
Simulation of two masses connected via springs
FIZ220 - https://emresururi.github.io/FIZ220/

@author: sururi
"""

import numpy as np
import matplotlib.pyplot as plt

k=50 # N/m
K=1 # N/m

m = 1 # kg

x1_0 = -1 # m
x2_0 = 3 # m
v1_0 = 0 # m/s
v2_0 = 0 # m/s

x2_rel_to_x1 = 5

w_s = np.sqrt(k/m)
w_f = np.sqrt(k+2*K/m)

Omega = (w_f+w_s)/2
Epsilon = (w_f-w_s)/2

N = 30
t=np.linspace(0,100,N)

M_ac = np.array([[1, 1],[1,-1]])
x1x2_0 = np.array([[x1_0],[x2_0]])
a,c = np.linalg.solve(M_ac,x1x2_0).flatten()
print("a,c: ",a,c)

M_bd = np.array([[w_s, w_f],[w_s,-w_f]])
v1v2_0 = np.array([[v1_0],[v2_0]])
b,d = np.linalg.solve(M_bd,v1v2_0).flatten()
print("b,d: ",b,d)

x1 = a*np.cos(w_s*t) + b*np.sin(w_s*t) + c*np.cos(w_f*t) + d*np.sin(w_f*t)
x2 = x2_rel_to_x1+a*np.cos(w_s*t) + b*np.sin(w_s*t) - c*np.cos(w_f*t) - d*np.sin(w_f*t)

fig,(ax1,ax2) = plt.subplots(2,1)
ax1.plot(t,x1,t,np.max(x1)*np.sin(Epsilon*t))
ax2.plot(t,x2,t,x2_rel_to_x1+(np.max(x2)-x2_rel_to_x1)*np.cos(Epsilon*t))
plt.show()
input("devam?..")

minmin = np.min(x1)-1
maxmax = np.max(x2)+1
for step in np.arange(N):
    plt.clf()
    plt.plot([x1[step],x2[step]],[0,0],"k-")
    plt.plot([minmin,x1[step]],[0,0],"g--")
    plt.plot([x2[step],maxmax],[0,0],"g--")
    plt.plot([minmin+0.1,minmin+0.1],[-0.2,0.2],"k-")
    plt.plot([maxmax,maxmax],[-0.2,0.2],"k-")
    plt.plot(x1[step],0,"ob",x2[step],0,"or")
    plt.xlim(minmin,maxmax)
    plt.ylim(-1,1)
    plt.title("t: %.3fs"%(t[step]))
    plt.show()
    