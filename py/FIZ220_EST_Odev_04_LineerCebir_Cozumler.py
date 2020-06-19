#!/usr/bin/env python
# coding: utf-8

# # Ödev: 4 - Çözümler
# ## FİZ220 - Bilgisayar Programlama II | 15/05/2020
# 
# **Lineer Cebir**
# 
# <strike>**Son gönderim tarihi:** 21 Mayıs Perşembe, 23:59  
# **Gönderim şekli:** FIZ220_Odev_04_Grup_#.ipynb isimli jupyter ipynb formatında dosyayı ödev sayfasından göndermek suretiyle  
# **Gönderecek kişi:** <u>Grup temsilcisi</u></strike>
# 
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# ### 1. Soru: Çevir, kısalt, göster, ispatla, edge of tomorrow
# $\require{cancel}$
# $$KR=\begin{bmatrix}0.75&0\\0&0.75\end{bmatrix}\begin{bmatrix}\cos{120^o} &-\sin{120^o}\\\sin{120^o}&\cos{120^o}\end{bmatrix}=\begin{bmatrix}-0.37500&-0.64952\\0.64952&-0.37500\end{bmatrix}$$
# 
# 
# 
# Şeklinde tanımlanan $KR$ operatörünün rastgele ürettiğiniz 10 vektörün hepsini $120^o$ döndürüp, boyunu da %75 kısalttığını teyit edin.
# 
# (300 puanlık) Bonus: KR operatörün verilen <u><span style="color:red;">her</span></u> vektörü $120^o$ döndürüp, boyunu da %75 kısalttığını <u><span style="color:red;">ispatlayın</span></u>..

# In[28]:


import numpy as np

K = np.array([[0.75,0],[0,0.75]])
aci_d = 120
aci = np.deg2rad(aci_d)
R = np.array([[np.cos(aci),-np.sin(aci)],[np.sin(aci),np.cos(aci)]])
KR = np.dot(K,R)
print(KR)
print("-"*40)

np.random.seed(220)
N = 10
v = np.random.rand(2,N)*20 - 10
print(v.T)
vp = np.dot(KR,v)
print(vp.T)

for i in range(N):
    v_i = v[:,i]
    vp_i = vp[:,i]
    v_i_boy = np.linalg.norm(v_i)
    vp_i_boy = np.linalg.norm(vp_i)
    print("Boylar: {:8.5f} /{:8.5f} = {:.2f}".format(v_i_boy,vp_i_boy,vp_i_boy/v_i_boy))
    v_i_aci = np.rad2deg(np.arctan2(v_i[1],v_i[0]))
    vp_i_aci = np.rad2deg(np.arctan2(vp_i[1],vp_i[0]))
    print("Açılar: {:5.2f} {:5.2f} :: {:5.2f}".format(v_i_aci,vp_i_aci,vp_i_aci - v_i_aci))
    print("-"*15)


# ## Gelelim Bonus'a... bonusa gel bonusa!..
# Kullandığımız koordinat sisteminde (Kartezyen), herhangi bir $\vec{a}$ vektörü, iki baz vektörün (${\hat\imath,\,\hat\jmath}$) skalerlerle ($\alpha,\,\beta$) çarpılıp toplanmış hali olarak yazılabilir:
# 
# $$\vec{a} = \alpha\,\hat{\imath}+\beta\,\hat{\jmath}$$
# 
# veya vektör-matris temsilinde açık olarak yazarsak:
# 
# $$\vec{a} =\begin{bmatrix}\alpha\\\beta\end{bmatrix} =\alpha\begin{bmatrix}1\\0\end{bmatrix}+\beta\begin{bmatrix}0\\1\end{bmatrix}$$
# 
# <u>Lineer</u> cebirde operatörlerin toplama üzerine dağılma özelliğini kullanırsak:
# 
# $$\begin{align*}\vec{a}'=KR\cdot\vec{a} &= \begin{bmatrix}-0.37500&-0.64952\\0.64952&-0.37500\end{bmatrix} \begin{bmatrix}\alpha\\\beta\end{bmatrix}\\
# &=\begin{bmatrix}-0.37500&-0.64952\\0.64952&-0.37500\end{bmatrix}\alpha\begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}-0.37500&-0.64952\\0.64952&-0.37500\end{bmatrix}\beta\begin{bmatrix}0\\1\end{bmatrix}
# \end{align*}$$

# In[32]:


i = np.array([[1],[0]])
j = np.array([[0],[1]])
KRi = np.dot(KR,i)
KRj = np.dot(KR,j)
print("KRi:\n",KRi)
print("-"*15)
print("KRj:\n",KRj)


# $$\begin{align*}\vec{a}' &=\alpha\begin{bmatrix}-0.37500\\0.64952\end{bmatrix}+\beta\begin{bmatrix}-0.64952\\-0.37500\end{bmatrix}
# \end{align*}$$
# 
# $\vec{a}'$nün büyüklüğü, bileşenlerinin karelerinin toplamına eşit:
# $$\begin{align*}|\vec{a}'|^2 &= \left(\alpha\left|\begin{bmatrix}-0.37500\\0.64952\end{bmatrix}\right|\right)^2+\left(\beta\left|\begin{bmatrix}-0.64952\\-0.37500\end{bmatrix}\right|\right)^2\\
# &=\alpha^2(0.5625) + \beta^2(0.5625)\\
# &=(0.5625)\left(\alpha^2 + \beta^2\right)
# \end{align*}$$
# 
# Bileşen vektörlerin boylarının karesini nasıl 0.5625 bulduğumuza gelirsek:

# In[43]:


print(np.dot(KRi.T,KRi))
print(np.dot(KRj.T,KRj))
print((-0.375)**2+0.64952**2)


# $\vec{a}$ vektörümüzün boyu da:
# $$|\vec{a}|^2=\left|\begin{bmatrix}\alpha\\\beta\end{bmatrix}\right|^2=\alpha^2 + \beta^2$$
# 
# ...buradan da boylarının oranını:
# $$\frac{|\vec{a}'|}{|\vec{a}|} = \sqrt{\frac{|\vec{a}'|^2}{|\vec{a}|^2}}=\sqrt{\frac{(0.5625)\cancel{\left(\alpha^2 + \beta^2\right)}}{\cancel{\alpha^2 + \beta^2}}}=\sqrt{0.5625}=\boxed{0.75}$$
# 
# olarak buluruz. Boyu gösterdik, sıra açıda.

# İki vektör arasındaki açıyı skaler çarpımın tanımından yola çıkarak buluruz, bu durumda $\vec{a}$ ile $\vec{a}'$ arasındaki açıya $\theta$ dersek:
# 
# $$\vec{a}\cdot\vec{a}' = |\vec{a}|| \vec{a}'|\cos\theta\Rightarrow \theta = \cos^{-1}\frac{\vec{a}\cdot\vec{a}'}{|\vec{a}|| \vec{a}'|}$$

# $$\begin{align*}
# \vec{a}\cdot\vec{a}' &=\begin{bmatrix}\alpha&&\beta\end{bmatrix} \cdot \left(\alpha\begin{bmatrix}-0.37500\\0.64952\end{bmatrix}+\beta\begin{bmatrix}-0.64952\\-0.37500\end{bmatrix}\right)\\
# &=\alpha^2(-0.375)+\beta\alpha(0.64952)+\alpha\beta(-0.64952)+\beta^2(-0.375)\\
# &=(-0.375)\left(\alpha^2+\beta^2\right)
# \end{align*}$$
# 
# Boylarının çarpımlarını da biliyoruz:
# 
# $$|\vec{a}| = \sqrt{\alpha^2+\beta^2},\quad |\vec{a}'|=0.75\sqrt{\alpha^2+\beta^2}$$
# $$\rightarrow |\vec{a}||\vec{a}'| = 0.75\left(\alpha^2+\beta^2\right)$$
# 
# Buradan da, açı denkleminde yerlerine yerleştirirsek:
# 
# $$\theta = \cos^{-1}\frac{\vec{a}\cdot\vec{a}'}{|\vec{a}|| \vec{a}'|}=\cos^{-1}\frac{(-0.375)\cancel{\left(\alpha^2+\beta^2\right)}}{0.75\cancel{\left(\alpha^2+\beta^2\right)}}=\cos^{-1}\frac{-0.375}{0.75}=\cos^{-1}{(-0.5)}=\boxed{120^o}$$

# In[51]:


theta = np.rad2deg(np.arccos(-0.375/0.75))
print("theta: {:5.2f} derece".format(theta))


# ### 2. Soru: Özvektör, özdeğer, 🎵eski dostlar, eski dostlar... 🎶
# 
# $A=\begin{bmatrix}2&3\\4&5\end{bmatrix}$ operatörü için:
#   * $\left( \begin{matrix}-0.49437\\-0.86925\end{matrix} \right)$,
#   * $\left( \begin{matrix}-0.79681\\0.60423\end{matrix} \right)$  
#   
# vektörlerini inceleyin. Bunlar özvektör ise, özdeğerlerini hesaplayıp, derste bulduğumuz $\left( \begin{matrix}1\\1.7583\end{matrix} \right)$ özvektörü ile karşılaştırın.

# In[61]:


import numpy as np
A = np.array([[2,3],[4,5]])
v1 = np.array([[-0.49437],[-0.86925]])
v2 = np.array([[-0.79681],[0.60423]])

v1_boy = np.linalg.norm(v1)
v2_boy = np.linalg.norm(v2)

A_v1 = np.dot(A,v1)
A_v2 = np.dot(A,v2)

A_v1_boy = np.linalg.norm(A_v1)
A_v2_boy = np.linalg.norm(A_v2)

print("boylar:\n",v1_boy,v2_boy,A_v1_boy,A_v2_boy)
print("A.v1:\n",A_v1)
print("A.v1/|A_v1|:\n",A_v1/A_v1_boy)
print("-"*20)
print("A.v2:\n",A_v2)
print("A.v2/|A_v2|:\n",A_v2/A_v2_boy)


# Yukarıda şu eşitlikleri çıkarmış olduk:
# $$\vec{v}_1 = \left( \begin{matrix}-0.49437\\-0.86925\end{matrix} \right),\quad \vec{v}_2=\left( \begin{matrix}-0.79681\\0.60423\end{matrix} \right),\quad A=\begin{bmatrix}2&3\\4&5\end{bmatrix}$$
# 
# olmak üzere:
# 
# $$\begin{gather*}A\cdot \vec{v}_1 = 7.2749\,\vec{v}_1\\
# A\cdot \vec{v}_2 = 0.2749\,\vec{v}_2\end{gather*}$$
# 
# yani $A$'nın özdeğerleri $\lambda_{1,2} = \{7.2749, 0.2749\}$ imiş. Derste $\vec{u}=\left( \begin{matrix}1\\1.7583\end{matrix} \right)$ özvektörünün özdeğeri olarak 7.2749'u bulmuştuk, demek ki $\vec{u}$ vektörü, $\vec{v}_1$'in bir skalerle çarpılmış hali. O skaleri de bulalım:

# In[63]:


u = np.array([[1],[1.7583]])
v1 = np.array([[-0.49437],[-0.86925]])
print(u/v1)


# $$ \vec{u} = -2.023\,\vec{v}_1$$

# ### 3. Soru: $R_{\pi/2}$
#  $90^0$ dönüş operatörünün özvektörünü ve özdeğerini bulun (bulamazsanız da yorumlayın (50 puan); bulursanız da (100 puan!))

# In[64]:


import numpy as np

theta = np.deg2rad(90)
R = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])

[l,u] = np.linalg.eig(R)
print(l)
print(u)


# Özdeğerler de özvektörler de kompleks çıktı!!! (Nasıl yani?...)
# 
# E sonuçta "2 boyutlu bir düzlemde, saat yönünde 90 derece döndürüldüğünde yönünü değiştirmeyen bir vektör" aradık, o da bize "yok öyle bir dünya!" diyerek, kendi dünyamızın dışından, kompleks düzlemden cevabı yapıştırdı. 8)
