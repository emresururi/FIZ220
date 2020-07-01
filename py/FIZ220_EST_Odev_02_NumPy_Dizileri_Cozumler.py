#!/usr/bin/env python
# coding: utf-8

# # Ödev: 2 - Çözümler
# ## FİZ220 - Bilgisayar Programlama II | 17/04/2020
# 
# **NumPy Dizileri**
# 
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# ## NumPy Dizileri (ndarray) matrisler şeklinde olacak.

# ### 1. Soru: 3 boyutlu, rastgele ([5,10) aralığında) değerleri olan bir garip  (2x3x4)'lük matris...
# (Hepsi başlıkta geçiyor, yine de bir daha yazalım bakalım 8)  
# (2x3x4) boyutlarında, değerleri 5 veya 5'ten büyük, 10'dan küçük rastgele ondalıklı sayılar olan bir ndarray matrisi üretin.

# In[4]:


import numpy as np

matris = np.random.rand(2,3,4) 
# bu matrisin değerleri 0 ile 1 arasında: [0,1)

matris = matris*5 + 5 # bu şekilde değerleri [5,10) aralığına taşıdık
# [0,1) * 5 = [0,5)
# [0,5) + 5 = [5,10)

print(matris)


# ### 2. Soru: Matris işlemleri, özdeğerler, özvektörler, aslında hepsi öteleme ve döndürmeden ibaret...
# 
# Elimizde iki boyutlu bir düzlem olsun. Bu düzlemde, (1,0) noktasını alalım (yani x=1, y=0 noktası). Bu noktayı öyle bir (2x2)'lik matrisle çarpalım ki, bize sonuç olarak (0,1) noktasını versin (yani noktamızı saat yönünün tersine, orijin etrafında 90 derece çevirsin). 
# 
# Aynı matrisi (0,1) ile çarptığımızda da, bu sefer onu (-1,0) noktasına taşısın (yaptığımız işlem aynı aslında: orijin etrafında, saat yönünün tersine 90 derece çevirmek).
# 
# Sorunun başlığı hakkında detaylı bilgi:
# * [The Applications of Matrices | What I wish my teachers told me way earlier](https://www.youtube.com/watch?v=rowWM-MijXU)
# * [Eigenvectors and eigenvalues | Essence of linear algebra, chapter 14](https://www.youtube.com/watch?v=PFDu9oVAE-g)

# **Çözüm**
# 
# İki boyutta olduğumuzdan ötürü, pozisyon vektörlerimiz de iki boyutlu olacak, tıpkı $\begin{pmatrix}1\\0\end{pmatrix}$ ve $\begin{pmatrix}0\\1\end{pmatrix}$ gibi.
# 
# $A$ matrisi aradığımız dönüş matrisimiz olsun. Bize verilen denklemler şunlar:
# 
# $$A\cdot \begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$$
# 
# $$A\cdot \begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}-1\\0\end{pmatrix}$$
# 
# $(2\times 1)$'lik bir vektöre etki edip, sonuçta yine $(2\times 1)$'lik bir vektör elde ettirecek matrisin boyutu $(2\times 2)$ olmak zorundadır. Bu durumda, bilinmeyen $A$ matrisimizi şu şekilde yazalım:
# 
# $$A=\begin{pmatrix}a&&b\\c&&d\end{pmatrix}$$
# 
# $a,b,c,d$ olmak üzere, 4 bilinmeyenimiz var. Bunları verilen vektörlere etki ettirirsek:
# 
# $$A\cdot \begin{pmatrix}1\\0\end{pmatrix} =  \begin{pmatrix}a&&b\\c&&d\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix} $$
# 
# $$A\cdot \begin{pmatrix}0\\1\end{pmatrix} =  \begin{pmatrix}a&&b\\c&&d\end{pmatrix}\begin{pmatrix}0\\1\end{pmatrix} = \begin{pmatrix}-1\\0\end{pmatrix} $$
# 
# çarpımları yapınca şu denklemleri buluruz:
# 
# $$\begin{gather*}a = 0,\\c = 1,\\b=-1,\\d=0\end{gather*}$$
# 
# $a$ ile $c$ ilk çarpımdan, $b$ ile $d$ de ikinci çarpımdan bulunuyor. Tanımda yerlerine koyunca:
# 
# $$A=\begin{pmatrix}0&&-1\\1&&0\end{pmatrix}$$
# 
# olarak buluruz. Haydi teyit edelim:

# In[7]:


A = np.array([[0,-1],[1,0]])
x1 = np.array([[1],[0]])
x2 = np.array([[0],[1]])
print("A:\n",A,"\n")
print("x1:\n",x1,"\n")
print("x2:\n",x2,"\n")

print("-"*45)

x1_ussu = np.dot(A,x1)
x2_ussu = np.dot(A,x2)

print("A.x1:\n",x1_ussu)
print("-"*45)
print("A.x2:\n",x2_ussu)


# [Bir sonraki dersimizde](https://emresururi.github.io/FIZ220/FIZ220_EST_UygulamaNotlari_06_Matris_Uygulamalari.html) bu matrisin aslında $\theta = 90^o$'ye karşılık gelen dönüş matrisi olduğunu göreceğiz -- en genel haliyle de:
# 
# $$R_{\theta}=\begin{bmatrix}\cos{\theta}&-\sin{\theta}\\\sin{\theta}&\cos{\theta}\end{bmatrix}$$
# 
# olarak temsil edilmekte...
