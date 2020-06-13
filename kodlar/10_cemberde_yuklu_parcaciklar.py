#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 00:05:45 2020

@author: sururi
"""

# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

aa = 0

def E_dt(theta):
    # aa'nın dışarıda tanımlandığına güveniyoruz
    E_dt = (np.cos(theta) - aa)/(1+aa**2-2*aa*np.cos(theta))**1.5
    return E_dt

def E_I(r,l):
    global aa
    # r: konum vektörü
    aa = np.linalg.norm(r)
    E_I_n,hassasiyet = integrate.quad(E_dt,0,2*np.pi)
    E_I_n *= k*l
    E_I_aci = np.arctan2(r[1],r[0])
    E_I = np.array([E_I_n*np.cos(E_I_aci),E_I_n*np.sin(E_I_aci)])
    return E_I


N = 50 # Simülasyonun toplam adım sayısı

k = 1 # Nm^2/C^2 
l = 1 # yük yoğunluğu (C/m)
m = 1 # kg (kütleleri 1 alalım)
Delta_t = 0.2 # zaman aralığı (s)

# Konum hesabında her seferinde karesini hesaplamamak için
# ayrı bir değişken olarak tanımlıyoruz
Delta_t_kare = Delta_t**2 # s^2
Delta_t_kare_yarim = Delta_t**2*0.5 # s^2

q = np.array([3,2,1,-4]) # Yükleri burada tutuyoruz (C)

r = np.array([[1,5],[7,1],[3,3],[0,0]])*0.1 # Konumlar da burada (m)

r = np.random.rand(6,2)*2-1
"""
# Altıgen
r= np.array([[-0.69692259, -0.02724232],
        [-0.33840058,  0.56061384],
        [ 0.28843479,  0.3626893 ],
        [-0.15758969, -0.51850352],
        [ 0.44098836,  0.20023462],
        [ 0.58547754, -0.3282882 ]]])
            
# Yıldız
r = np.array([[ 0.23521891,  0.17173761],
        [ 0.54690823, -0.0215273 ],
        [-0.37706119, -0.80255193],
        [-0.08277804, -0.69548606],
        [ 0.42817634,  0.47258186],
        [-0.35387868,  0.25307498]])
"""



P = r.shape[0] # Parçacık sayısı -- satır sayısından buluyoruz
q = np.ones((P,1)) # Bütün yükler 1 C olsun



# Her adımda parçacıkların konumlarını 
# konumlar değişkeninde tutacağız.
# konumlar[adım#,parçacık#,{x,y}]
# Örneğin: konumlar(5,1,0) : 2. parçacağın 5. adımdaki x konumu
konumlar = np.zeros((N+1,P,2))
konumlar[0,:] = r
ivmeler_toplam = np.zeros(N)

for adim in range(N):
    ivmeler = np.zeros((P,2))
    for i in range(P):
        for j in range(i+1,P):
            r_ij = r[j,:]-r[i,:]
            r_n = np.linalg.norm(r_ij) # m
            
            F_n = (k*q[i]*q[j]/r_n**2) # N
            aci = np.arctan2(r_ij[1],r_ij[0]) # radyan
            F_x = F_n*np.cos(aci)
            F_y = F_n*np.sin(aci)
            F = np.array([F_x[0],F_y[0]])

            a = F/m # m/s^2
            # ilgili parçacığın `ivmeler` matrisine ivmesini yazalım
            ivmeler[j,:] += a
            
            # Diğer parçacık da nasibini zıt yönde alacak
            ivmeler[i,:] -= a

        # Şimdi de çemberin i. parçacık üzerinde oluşturduğu kuvvet var:
        a_cember = E_I(r[i,:], l)
        ivmeler[i,:] -= a_cember 

    # Bu adımdaki her bir parçacığın üzerine binen kuvvetleri/ivmeleri 
    # hesapladığımıza göre, şimdi aldıkları yolları bulalım:
    
    # (sonuçta bütün ivme değerlerini 0.5*t^2 ile çarpıyoruz)
    Deltalar = ivmeler*Delta_t_kare_yarim
    
    # Deltalar'ı doğrudan r'lere ekleyebiliriz:
    r += Deltalar
    
    # Çemberin dışına kaçanları rastgele olarak içeriye koyalım
    r[np.abs(r)>1]=np.random.rand(np.sum(np.abs(r)>1))
    
    konumlar[adim+1,:] = r
    ivmeler_toplam[adim] = np.sum(np.linalg.norm(ivmeler,axis=1))
    
    # ileri seviye ------------------------------------------0---#
    if(np.linalg.norm(konumlar[adim+1,:]-konumlar[adim,:])<1E-5):
        N = adim
        break
    # ileri seviye ------------------------------------------1---#

#print(konumlar)

x_min = np.min(konumlar[:,:,0])
x_max = np.max(konumlar[:,:,0])
y_min = np.min(konumlar[:,:,1])
y_max = np.max(konumlar[:,:,1])

x_min = y_min = -1
x_max = y_max = 1


for adim in range(N+1):
    fig,ax = plt.subplots()
    plt.plot(konumlar[adim,:,0],konumlar[adim,:,1],"ok")

    plt.xlim(x_min-0.1,x_max+0.1)
    plt.ylim(y_min-0.1,y_max+0.1)
    plt.title("Adim: {:d}".format(adim))
    circle=plt.Circle((0,0), radius=1,fill=False,linewidth=3)
    ax.add_artist(circle)
    plt.show()