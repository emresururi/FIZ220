#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:27:12 2020

@author: sururi
"""

import numpy as np
import matplotlib.pyplot as plt

N = 10 # Simülasyonun toplam adım sayısı

k = 9E9 # Nm^2/C^2 
m = 1 # kg (kütleleri 1 alalım)
Delta_t = 1 # zaman aralığı (s)
# Konum hesabında her seferinde karesini hesaplamamak için
# ayrı bir değişken olarak tanımlıyoruz
Delta_t_kare = Delta_t**2 # s^2

# Her adımda parçacıkların konumlarını 
# konumlar değişkeninde tutacağız.
# konumlar[adım#,parçacık#,{x,y}]
# Örneğin: konumlar(5,1,0) : 2. parçacağın 5. adımdaki x konumu
konumlar = np.zeros((N,2,2))

q1 = 3.0E-6 # C
r1 = np.array([1,5])*0.1 # m


q2 = 2.0E-6 # C
r2 = np.array([7,1])*0.1 # m

plt.plot([r1[0],r2[0]],[r1[1],r2[1]],"ok")
##plt.arrow(0,0,r1[0],r1[1],length_includes_head=True,head_width=.3, head_length=.5)
##plt.arrow(0,0,r2[0],r2[1],length_includes_head=True,head_width=.3, head_length=.5)
##plt.arrow(r1[0],r1[1],r2[0]-r1[0],r2[1]-r1[1],length_includes_head=True,head_width=.3, head_length=.5,color="purple")
##plt.xlim(0,0.1)
##plt.ylim(0,0.1)
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.show()



for adim in range(N):
    r = r2-r1
    r_n = np.linalg.norm(r) # aradaki mesafe (m)


    plt.plot([r1[0],r2[0]],[r1[1],r2[1]],"ok")
    plt.xlim(-1,1)
    plt.ylim(-1,1)
    plt.title("Adim: {:d}".format(adim))
    plt.show()



    # Kuvvetin büyüklüğü (1'in 2'ye yaptigi: F_21)
    F_n = k*q1*q2/r_n**2 # N
    ##print(F_n)

    # Kuvvetin bileşenleri
    aci = np.arctan2(r[1],r[0]) # r vektörünün x-ekseniyle yaptığı açı (radyan)
    ##print(np.rad2deg(aci))
    F_x = F_n*np.cos(aci)
    F_y = F_n*np.sin(aci)
    F = np.array([F_x,F_y])
    ##print(F)

    # İvmeyi de bulalım
    a = F/m # m/s^2
    ##print(a)

    # 2'nin üzerine binen kuvvet sonucu kazandığı bu ivme ile 
    # Delta_t süre sonra ne kadar yol kat etmiş olacağını hesaplayalım:
    Delta_x = 0.5*a[0]*Delta_t_kare
    Delta_y = 0.5*a[1]*Delta_t_kare
    Delta_xy = np.array([Delta_x,Delta_y])
    ##print("Delta_xy: ", Delta_xy)

    r2 = r2 + Delta_xy

    # 1'in kat edeceği yol da 2'ninkinin tam tersi yönde, aynı büyüklükte olacak:
    r1 = r1 - Delta_xy
    
    ##print(r1)
    ##print(r2)
    
    konumlar[adim,0,0] = r1[0]
    konumlar[adim,0,1] = r1[1]
    konumlar[adim,1,0] = r2[0]
    konumlar[adim,1,1] = r2[1]
print(konumlar)