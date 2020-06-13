#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:26:58 2020

@author: sururi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 50 # Simülasyonun toplam adım sayısı

k = 9E9 # Nm^2/C^2 

m = 1 # kg (kütleleri 1 alalım)
Delta_t = 1 # zaman aralığı (s)

# Konum hesabında her seferinde karesini hesaplamamak için
# ayrı bir değişken olarak tanımlıyoruz
Delta_t_kare = Delta_t**2 # s^2
Delta_t_kare_yarim = Delta_t**2*0.5 # s^2

q = np.array([3,2,1,-4,-2])*1E-6 # Yükleri burada tutuyoruz (C)
r = np.array([[1,5],[7,1],[3,3],[0,0],[1,4]])*0.1 # Konumlar da burada (m)

P = q.shape[0] # Parçacık sayısı -- satır sayısından buluyoruz

# Her adımda parçacıkların konumlarını 
# konumlar değişkeninde tutacağız.
# konumlar[adım#,parçacık#,{x,y}]
# Örneğin: konumlar(5,1,0) : 2. parçacağın 5. adımdaki x konumu
konumlar = np.zeros((N+1,P,2))
konumlar[0,:] = r

for adim in range(N):
    ivmeler = np.zeros((P,2))
    for i in range(P):
        for j in range(i+1,P):
            r_ij = r[j,:]-r[i,:]
            r_n = np.linalg.norm(r_ij) # m
            
            F_n = k*q[i]*q[j]/r_n**2 # N
            aci = np.arctan2(r_ij[1],r_ij[0]) # radyan
            F_x = F_n*np.cos(aci)
            F_y = F_n*np.sin(aci)
            F = np.array([F_x,F_y])

            a = F/m # m/s^2
            # ilgili parçacığın `ivmeler` matrisine ivmesini yazalım
            ivmeler[j,:] += a
            
            # Diğer parçacık da nasibini zıt yönde alacak
            ivmeler[i,:] -= a

    # Bu adımdaki her bir parçacığın üzerine binen kuvvetleri/ivmeleri 
    # hesapladığımıza göre, şimdi aldıkları yolları bulalım:
    
    # 2'nin üzerine binen kuvvet sonucu kazandığı bu ivme ile 
    # Delta_t süre sonra ne kadar yol kat etmiş olacağını hesaplayalım:
    
    # Bu eski usülde nasıl yaptığımızdı:
    ## Delta_x = 0.5*a[0]*Delta_t_kare
    ## Delta_y = 0.5*a[1]*Delta_t_kare
    ## Delta_xy = np.array([Delta_x,Delta_y])
    
    # ama artık, doğrudan yapabiliriz 
    # (sonuçta bütün ivme değerlerini 0.5*t^2 ile çarpıyoruz)
    Deltalar = ivmeler*Delta_t_kare_yarim
    
    # Deltalar'ı doğrudan r'lere ekleyebiliriz:
    r += Deltalar
    konumlar[adim+1,:] = r

print(konumlar)

x_min = np.min(konumlar[:,:,0])
x_max = np.max(konumlar[:,:,0])
y_min = np.min(konumlar[:,:,1])
y_max = np.max(konumlar[:,:,1])

for adim in range(N+1):
    plt.plot(konumlar[adim,:,0],konumlar[adim,:,1],"ok")

    plt.xlim(x_min-0.1,x_max+0.1)
    plt.ylim(y_min-0.1,y_max+0.1)
    plt.title("Adim: {:d}".format(adim))
    plt.show()