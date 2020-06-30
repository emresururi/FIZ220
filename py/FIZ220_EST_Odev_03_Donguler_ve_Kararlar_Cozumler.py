#!/usr/bin/env python
# coding: utf-8

# # Ödev: 3 - Çözümler
# ## FİZ220 - Bilgisayar Programlama II | 08/05/2020
# 
# **Döngüler ve Kararlar**
# 
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# ## NumPy Dizileri (ndarray) matrisler şeklinde olacak.

# ### 1. Soru: Asal sayılar (hani hesaplanamıyordu?..)
# Tanımlanan bir _n_ sayısından büyük ilk asal sayıyı bulan program yazınız.

# In[1]:


import numpy as np

n = 113
print("Tanımlanmış olan n değeri: ",n)

# Asal sayılar için sihirli bir formülümüz olmadığından,
# "en baştan", 3'den başlıyoruz

simdiye_kadarki_asallar = np.array([2])

# Once n'e kadar/dahil olan asal sayıları bulalım:
for i in np.arange(3,n+1,2):
    # Şu anda elimizdeki i sayısının asal olduğunu varsayalım
    i_asal_mi = True
    
    # Şimdi de birer birer "simdiye_kadarki_asallar" kumesinin
    # elemanlarına bölelim -- tâ ki bir tanesine kalansız bölününceye
    # kadar -- o zaman asal değil demektir!
    for j in simdiye_kadarki_asallar:
        if(i%j == 0): 
            # Kalansız bölündü - demek ki asal değil!
            i_asal_mi = False
            
            # Diğer sayılara bölünüyor mu diye bakmaya gerek yok
            break
    
    # Buraya gelindiğinde iki şey olmuş olabilir:
    # * ya bir sayıya kalansız bölündü (i_asal_mi = False)
    # * ya da, hiçbirine kalansız bölünmedi de, j'nin döngüsü bitti
    #     (yani gerçekten asalmış -- i_asal_mi = True kaldı)
    if(i_asal_mi == True):
        simdiye_kadarki_asallar = np.append(simdiye_kadarki_asallar,i)
print("Şimdiye kadarki asallar: \n",simdiye_kadarki_asallar)

# Artık tek yapmamız gereken bunu takiben bir tane daha asal bulmak
while True:
    # Bu şekilde sonsuz bir döngüye girdik, sonumuz hayır olsun
    # (hemen korkmayın, istediğimiz an break ile kırar çıkarız 8)
    n = n + 1
    n_asal_mi = True
    for j in simdiye_kadarki_asallar:
        if(n%j == 0):
            n_asal_mi = False
            # print(j tarafindan tam bolundu")
            break
    if(n_asal_mi == True):
        print("Bulunan asal: ",n)
        break  


# Kendinizi geliştirmek isterseniz, ikinci döngüde (n=n+1 olan) n'in değerini birer birer değil de, ikişer ikişer arttıralım, ne de olsa çift sayılar asal olamayacağından, boşu boşuna kontrol etmekle CPU'yu yormuş olmayız --- ama bir saniye, ya bize başta verilen n çift sayı ise? o zaman bütün tekleri atlamış oluruz!!! O halde koda öyle bir ekleme yapın ki, eğer verilen n tek ise, öyle kabul edin ama eğer çift ise, ondan küçük en büyük tek sayıya eşitleyin (yani, halk tabiriyle: _1 çıkarın_ 8)

# ### 2. Soru: Kuvvet hesabı
# 
# İki boyutta, konumları $(x_i\hat{i} + y_i\hat{j})\,\text{m}$ şeklinde, yükleri de Coulomb cinsinden verilen 5 adet parçacığın her birinin üzerine diğerlerinden binen kuvvetleri (vektörel olarak) hesaplayan program yazın.

# In[2]:


import numpy as np

np.random.seed(220)

n = 5 # Parcacik sayisi

k = 8.99E9 # Nm^2/C^2

# Rastgele konumlar ve yükler için:
# konumlar = 10*np.random.rand(n,2)-5 # orijine göre (m)
# yukler = 500*(np.random.rand(n,1)-0.5)*1E-6 # (C)

# Biz yüklerimizi merkezi orijinde olan,
# kenar uzunluğu 2m'lik bir karenin köşelerine 
# ve merkezine koyalım

konumlar = np.zeros((n,2)) # (m)
konumlar[0,:] = [0,0]   # Merkez
konumlar[1,:] = [1,1]   # Sağ üst
konumlar[2,:] = [-1,1]  # Sol üst
konumlar[3,:] = [-1,-1] # Sol alt
konumlar[4,:] = [1,-1]  # Sağ alt


yukler = np.array([5,1,1,1,1])*1E-6 # (C)

print("konumlar (m):\n",konumlar)
print("-"*45)

print("yükler (C):\n",yukler)
print("-"*45)

kuvvetler = np.zeros((5,2))

print("\n"+"2 --- 1\n"+" \   /\n"+"|  0  |\n"+" /   \ \n"+"3 --- 4\n")



for i in np.arange(n-1):
    for j in np.arange(i+1,n):
        r_vec = konumlar[i,:] - konumlar[j,:]
        r_buyukluk = np.sqrt(r_vec[0]**2 + r_vec[1]**2)
        F = k*yukler[i]*yukler[j]*r_vec/r_buyukluk**3
        print("F_"+str(i)+str(j),": ",j," -> ",i," kuvveti: ",F,"N")
        kuvvetler[i] = kuvvetler[i] + F
        # j, i'ye F kuvveti uyguluyorsa,
        # i de j'ye -F kuvveti uygular:
        kuvvetler[j] = kuvvetler[j] - F
print("-"*45)
print("kuvvetler (N):\n",kuvvetler)
print("-"*45)


# Parçacıklar üzerinden döngüyü alırken, nasıl saydığımıza dikkat edin: $i\rightarrow j$ etkileşimi ile $j\rightarrow i$ etkileşimi zıt yönlerde fakat aynı büyüklükte olduğundan, ayrı ayrı bir $i\rightarrow j$, bir de $j\rightarrow i$ etkileşimi hesaplamamak için $i$'leri 0,1,2,3'e kadar/dahil sayarken, $j$'leri de $i$'lerin başlangıcından 4'e kadar/dahil sayıyoruz. Böylelikle hesap sayısını en aza indirgemiş oluyoruz. İleride, bilimsel makalelerde şöyle toplamlar göreceksiniz:
# 
# $$\frac{1}{2}\sum_{i\ne j}{E_{ij}}$$
# işte o başındaki $\frac{1}{2}$'nin hikayesi bu çifte sayım mevzuu. Anlaşılsın diye o şekilde yazılır, koda uyarlanırken de:
# 
# $$\sum_{i=0}^{N-1}\sum_{j=i}^{N}{E_{ij}}$$
# olarak uyarlanır. ;)
