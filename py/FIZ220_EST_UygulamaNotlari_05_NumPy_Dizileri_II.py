#!/usr/bin/env python
# coding: utf-8

# # Uygulama Notları: 5
# ## FİZ220 - Bilgisayar Programlama II | 16/04/2020
# 
# **Matrisler II (NumPy Dizi (_numpy.ndarray_) Nesneleri)**
# 
# * Matrislerin Özellikleri
#   * size
#   * shape
#   * reshape
#   * ndim
#   * dtype
# * Tipik Matrisler
#   * zeros
#   * ones
#   * fill ile matrisi doldurmak
#   * birim matris
#   * rastgele matrisler
#   * arange ile aralıklar
#   * linspace
# * Matris işlemleri
#   * Dört temel işlem (eleman bazında)
#   * Skaler ve Vektörel Çarpımlar
#     * Skaler Çarpım
#     * Vektörel Çarpım
#   * Matrisin transpozesi, tersi ve determinantı
#     * Transpozesi
#     * Tersi
#     * 'Tersimsisi'
#     * Determinantı
#   
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# ## Matrislerin Özellikleri
# Sıklıkla, elimize geçirdiğimiz bir NumPy dizisinin özelliklerini bilmek isteriz: boyu nedir, boyutu nedir, kimlerdendir, içinde sevdiceğimiz var mıdır vs. Bu bölümde temel bilgi komut ve metotlarını işleyeceğiz.
# 
# O halde, bir tane 2 boyutlu $(4\times5)$ matris tanımlayıp, işimize bakalım:

# In[1]:


import numpy as np
mat1 = np.array([[0,1,2,3,4],[10,11,12,13,14],[20,21,22,23,24],[30,31,32,33,34]])
print(mat1)


# Fark ettiyseniz, değerler aynı zamanda satır ve sütun indislerini veriyor (ilk satırın (0 satırı) misal 2 indisli elemanını `02` yazamadığımdan, `2` ile yetiniyoruz ama artık _o kadar kusur kadı kudu_ (©Yiğit Özgür 8).

# ### size: Matrisin eleman sayısı
# `size` metodu bize matrisin toplam eleman sayısını verir. Örneğimizdeki matrisimizin 20 elemanı var, o halde, "size" diye sorunce, "20" demesini bekliyoruz, bakalım:

# In[2]:


print("Matrisimizin eleman sayısı: ",mat1.size)


# ## shape: Matrisimizin boyutları _(90-60-90)_
# `shape` metodu matrisimizin "şeklini" yani boyutlarını bir demet (_tuple_) olarak döndürür:

# In[3]:


print("Matrisimizin boyutları: ",mat1.shape)
print("Matrisimizin ",len(mat1.shape)," adet boyutu var.")
print("Asıl (0 - satırlar) eksendeki 'kat' sayısı: ",mat1.shape[0])
print("İkincil (1 - sütunlar) eksendeki 'daire sayısı: ",mat1.shape[1])


# Burada dikkatinizi çektiyse, boyutların döndürüldüğü mat1.shape demetinin boyunu bulurken `size` metodunu değil, `len` komutunu kullandık. Bunun sebebi, `size`ın bir ndarray metodu olup, demetlere uygulanabilir olmaması. `len` komutu epey evrensel bir komut olup, hemen her değişkene sorulabilir. O halde niye `len` dururken, matrislerde `size` ile uğraşıyoruz? Hemen bakalım:

# In[4]:


print(len(mat1))


# Gördüğünüz üzere, sadece ilk eksenin (satırların) sayısını veriyor, gayet de mantıklı zira Python bunu -teknik olarak- her birinde 5 elemanlı 1 boyutlu dizi olan, 4 elemanlı bir derleme olarak görüyor (matrisi nasıl tanımladığımızı hatırlayın: [ [1. eleman: 1. dizi], [2. eleman: 2. dizi], ...]). Bu yüzden, n-boyutlu matrislerin eleman sayısını `len` ile değil, `size` ile öğreniyoruz (bu konu sanırım bölüm sonlarında olan "bunları bilmeseniz de olur ama işte..." kısmına daha uygundu!.. 8)

# ![play-it-sam.jpg](attachment:play-it-sam.jpg)
# (Casablanca, "Play it -again- Sam" (tamam, Bogart hiç _again_ lafını söylemiyor aslında ama olsun))

# ## reshape: yeniden şekillendir, Sam..
# Matrisin şekli çok önemlidir zira o şekli yeniden ("re-") biçimlendirebiliriz ("shape") => `reshape`!
# 
# Elimizdeki matris (4x5)'ti, 20 elemanı vardı. Elemanları düzgünce dağıtabileceğimiz (yani bütün boyutlarının çarpımı 20 olduğu sürece) her boyuta çıkabiliriz. Çarpımı 20 olan sayılardan bazılarını sıralayalım:
# 
# * 1x20
# * 2x10
# * 2x2x5
# * 20x1
# 
# Gördüğünüz üzere, yukarıdakilerden 1. ve 4. örnekler bir boyutlu matrisler (ilki satır, ikincisi sütun vektörü); 2. örnek 2 satırlı, 10 sütunlu iki boyutlu bir matris; 3. ilginç çünkü 3 boyut var. Tek tek deneyelim:
# 
# 

# In[5]:


print(mat1.reshape(1,20))


# In[6]:


print(mat1.reshape(2,10))


# In[7]:


print(mat1.reshape(2,2,5))
print(mat1.reshape(2,2,5)[1,1,3])


# In[8]:


print(mat1.reshape(20,1))


# (2x2x5) üç boyutlu matrisimizde [1,1,3] indisli elemanı istediğimizde, önce 1. eksende ilerleyip, 1 indisli diziye gittik:
# 
# `[[20 21 22 23 24]
#   [30 31 32 33 34]]`
#  
# dizisi. Sonra bu dizinin 1 indisli dizisine gittik:
# 
# ` [30 31 32 33 34]`
# 
# dizisi. Sonra da, bu dizinin 3 indisli elemanına (yani 4. elemanına) gittik: 33
# 
# Bu vesileyle, çaktırmadan, 3 boyutlu bir diziyi nasıl oluşturabileceğimize dair bir yolu da keşfetmiş olduk: `reshape` metodu ile.

# ## ndim: kısa yoldan kaç boyutlu bir matrisimiz olduğuna dair...
# Elimizdeki matrisimizin kaç boyutlu olduğunu şeklinin kaç elemanı olduğunu sorarak öğrenebilmiştik:

# In[9]:


print("Matrisimizin ",len(mat1.shape)," adet boyutu var.")


# Bunu tek bir metotla da yapmak mümkün, bu iş için `ndim` metotu yardımımıza koşuyor:

# In[10]:


print("Matrisimizin ",mat1.ndim," adet boyutu var.")


# ## dtype: elemanlarının cinsi
# Aşağıdaki üç diziye bir bakın -- sizce aralarında çok fark var mı?
# 1. `dizi_1 = np.array([0,1,2])`
# 2. `dizi_2 = np.array([0,1,2.0])`
# 3. `dizi_3 = np.array([0,1.0,"iki"])`
# 
# ...
# 
# Herhalde, 3.yü listeye koymasaydık, "fark yok" cevabı normal karşılanacaktı ama 3. işi bozduğundan, bu sefer 1. ile 2. arasında da bir bit yeniği çıkmasını bekliyoruz. Python'a verelim, bakalım o ne diyecek:
# 

# In[11]:


dizi_1 = np.array([0,1,2])
dizi_2 = np.array([0,1,2.0])
dizi_3 = np.array([0,1.0,"iki"])

print("dizi_1:\n",dizi_1,"\n")
print("dizi_2:\n",dizi_2,"\n")
print("dizi_3:\n",dizi_3,"\n")


# Hemen fark edenler kendilerine bir 10 puan yazsınlar bakalım! Detaylıca incelediğimizde, ilkinde sayılarımızın ondalık noktalarının olmadığını, ikincisinde diziyi girerken sadece 2'yi ondalıklı girdiğimiz halde (o da hani "2.3" gibi değil, bildiğiniz "2.0" masumane şekliyleydi!) 0 ve 1'in kuyruklarına da ondalık noktasının takılmış olduğunu, üçüncü dizide ise hepsinin (0'ın ve 1.0'ın bile!) bir kelimeymişçesine kesme (') işaretleri arasına alınmış olduğunu görüyoruz. Bunun sebebi şu:
# 
# NumPy dizileri sadece tek bir eleman cinsini tutarlar. İlk dizimizde bütün elemanlarımız tam sayı, o yüzden tam sayı olarak tutulabiliyorlar; ikinci dizimizde iki tam sayı, bir tane ondalıklı sayı girdiğimizde, ondalıklı sayının varlığı (değerinden bağımsız olarak), dizinin elemanları tuttuğu cins olarak tam sayıyı değil, hepsini içerebilecek ondalıklı sayı cinsini seçmesini gerektiriyor (genel olarak: tam sayıları bilgi kaybı olmadan ondalıklı olarak tutabilsek de, tersi mümkün değil); üçüncüsünde ise, tam sayı olsun, ondalıklı sayı olsun, bunları string olarak tutabiliyoruz ama string değişkenlerini -genel olarak- sayı olarak ifade edemediğimizden, elemanların cinsi "en küçük ortak cins" olan string olarak tanımlanıyor.
# 
# Bir dizinin tuttuğu eleman cinsini de `dtype` metodu ile öğreniyoruz:

# In[12]:


print("dizi_1'in elemanlarının cinsi :",dizi_1.dtype,"\n")
print("dizi_2'nin elemanlarının cinsi:",dizi_2.dtype,"\n")
print("dizi_3'ün elemanlarının cinsi :",dizi_3.dtype,"\n")


# Tipte yazılı kısım cinsi (integer: tam sayı; float: ondalıklı sayı; U: Unicode string) verirken, peşinden gelen sayı her bir eleman için hafızada ayrılan yer miktarını (bit cinsinden) verir.

# Bir dizinin elemanlarının cinsini **zorla** bir başka cinse dönüştürmek mümkündür: bunu `astype` metotu ile yaparız:

# In[13]:


print(dizi_2.astype(int))


# Ama bunun mümkün olmadığı yerde de zorlamanın pek bir alemi yok:

# In[14]:


print(dizi_3.astype(float))


# 150 tane tam sayı elemanı olan bir diziye, 151. eleman olarak ondalıklı sayı eklediğimizde bütün elemanlarının tipi nasıl da tümden ondalıklı sayılara dönüşüyorsa, iki sayıyı topladığımızda da bu kural otomatikman uygulanır:

# In[15]:


# Tam sayı + tam sayı = tam sayı:
5 + 7


# In[16]:


# Tam sayı + ondalıklı sayı = ondalıklı sayı:
5 + 7.5


# In[17]:


# Çok mu barizdi? Öyleyse bir de şuna bakalım:
5 + 7.0


# ## Tipik Matrisler
# Şimdi eğri oturup, doğru konuşalım: NumPy'da matris elemanlarını tanımlamak çoğu kez epey sıkıcı. Bu yüzden hayatı kolaylaştırıcı birkaç tipik hazır matris türü var.

# ### zeros : sıfır sıfır sıfır...
# Adı üzerinde, istediğimiz boyutta, tüm elemanları sıfır olan bir matris döndürür - yapmamız gereken, istediğimiz matris boyutunu belirlemekten ibaret:

# In[18]:


mat_0 = np.zeros([2,3,4])
print (mat_0)


# ### ones : bir bir bir... (nereye kadar gideceğiz böyle, haydi bakalım...)

# Bu da, bütün elemanları 1 olan bir matris döndürür:

# In[19]:


mat_1 = np.ones([2,5,2])
print(mat_1)


# ### fill ile matrisi doldurmak
# Bütün elemanları sıfır veya bir olan bir matrisi nasıl tanımlayacağımızı artık biliyoruz, peki bütün elemanlarının 2.7 olmasını istiyorsak? Bu durumda, iki-üç(-çok?) yolumuz var: 
# 
# 1. 0-matrisi oluşturup, bütün elemanlarına 2.7 ekleriz:

# In[20]:


mat_0 + 2.7


# 2. 1-matrisi oluşturup, bütün elemanlarını 2.7 ile çarparız:

# In[21]:


mat_1 * 2.7


# 3. Herhangi bir matris oluşturup (ya da hazır alıp), bütün elemanlarını 2.7 ile _doldururuz_:

# In[22]:


mat_n = np.array([[1,2,3.],[4,5,6]])
print(mat_n)
print("----------")
mat_n.fill(2.3)
print(mat_n)


# `fill` metodunu kullanırken dikkat etmeniz gereken iki şey var: 
# * Metodu kullandığınızda doğrudan ilgili matrise etki eder, yeni bir matris döndürmez.
# * Elinizdeki matrisin cinsi ne ise, doldururken kullandığınız değerin cinsini matrisin cinsine döndürür.
# 
# İkinci noktanın nasıl çalıştığını görmek için üstteki örneği bir kez daha, bu kez "hilesiz, el çabukluğu kerametsiz", ağır çekimde izleyelim:

# In[23]:


mat_n = np.array([[1,2,3],[4,5,6]])
print(mat_n)
print("----------")
mat_n.fill(2.3)
print(mat_n)


# Hoppala! Yukarıdakinin _aynısını_ yazdık ama bu sefer 2.3 yerine, 2 ile doldurdu... nereyi farklı girdik ki?.. (haydi bulun bakalım, size 1 dakika süre...)

# ....

# Buldunuz mu? İki girişte de ilk satırdaki "3"e bakın. Evet, tam orası işte! İlk kodda "3." diyerek, çaktırmadan bütün diziyi ondalıklı tipine dönüştürmüşüz, ikincisinde hepsi tam sayı. Bu yüzden ikincisinde "2.3" ondalıklı sayısı ile doldur deyince matrisimize, "hiç kusura bakma, ben tam sayı matrisiyim, çok istiyorsa tam sayı kılığına girsin, 2 olarak eklerim" diyor, olayımız bundan ibaret. 8P 8)

# ### birim matris
# 
# Birim matris, tanım itibarı ile -ve tabii ki boyutları ile uyumlu olmak şartıyla- bir matrisle çarpıldığı zaman, o matrisi değiştirmeyen matristir. Bunu da sağlamanın tek yolu, köşegeni boyunca "1" değerini almasıdır. "Identity" (birim, etkisiz) olarak isimlendirilip "I" harfi ile temsil edildiğinden, okunuşundan yola çıkıp, ufak bir kelime oyunu ile `eye` olarak tanımlanır:

# In[24]:


mat_birim_5x5 = np.eye(5,5)
print(mat_birim_5x5)


# In[25]:


# Kare matris olması zorunluluğu yoktur:
mat_birim_3x5 = np.eye(3,5)
print(mat_birim_3x5)


# ### rastgele matrisler
# Bazen uğraşmak istemeyiz, "sen kafana göre doldur, ben sonra bakarım" deriz. Bu durumlarda numpy.random kütüphanesinin rand ve randint'i epey yardımcı olur:

# In[26]:


mat_rastgele_tamsayilar = np.random.randint(5,10,[2,3,4])
print(mat_rastgele_tamsayilar)


# In[27]:


mat_rastgele_ondaliklar = np.random.rand(2,3,4)
print(mat_rastgele_ondaliklar)


# Parametreler anlaşılıyor mu çağrıştan? randint'e ilk parametre olarak alt limiti (dahil), ikinci parametre olarak üst limiti (hariç), üçüncü parametre olarak da matrisimizin arzu ettiğimiz boyutunu belirtiyoruz (Bu arada, Python'da harikulade bir parametre sıralama opsiyonu var, birkaç haftaya göreceğiz inşallah 8)
# 
# rand'da ise parametre olarak sadece boyutu verebiliyoruz, o da bize, alışık olduğumuz üzere 0 ile 1 arasında (0 dahil, 1 hariç) sayılar üretiyor (teknik not: düzgün dağılımdan).

# ### arange ile aralıklar
# `arange` komutu bize bir boyutlu diziler verir ama elemanlarını istediğimiz adımla türetebildiğimiz için, peşine bir de `reshape` çekersek tadından yenmez olur. İlk parametre başlayacağı sayı (dahil), ikinci parametre biteceği sayı (hariç), üçüncü parametre de adım boyu olur:

# In[28]:


mat_aralik = np.arange(4,10.1,2.3)
print(mat_aralik)


# Gördüğünüz üzere, ne başlangıcın, ne bitişin, ne de adım boyunun tam sayı olmak gibi bir zorunluluğu yok. İleriye doğru gidebildiğimiz gibi, geriye doğru da gidebiliriz (Nasıl?.. Adım boyumuzu negatif alarak tabii ki!):

# In[29]:


mat_aralik_gerigeri = np.arange(10,2,-2)
print(mat_aralik_gerigeri)


# In[30]:


# Bir de arange + reshape kombosu yapalım, tam olsun:
mat_kombo_3x3 = np.arange(1,10).reshape(3,3)
print(mat_kombo_3x3)


# Yukarıdaki örnekte nokta ardından nokta birleşik yazımı (metodun dönüşüne metot) kafanızı karıştırıyorsa, parantez içinde de güzel güzel belirtebilirsiniz:

# In[31]:


mat_kombo_3x3 = (np.arange(1,10)).reshape(3,3)
print(mat_kombo_3x3)


# ![SelcukErdem_AkilliEfendiKopek.png](attachment:SelcukErdem_AkilliEfendiKopek.png)
# (Selçuk Erdem, Karikatürler 1, s.72)
# 
# ### linspace: düzenli, disiplinli
# Sayısal örneklerle haşır neşir olacağımız için bir fonksiyonun belli -ve hemen her zaman düzenl aralıklı- noktalarda değerini hesaplatmak istediğimizde arange yardıma koşar. Ama mesela doğrudan "23 ile 30 arasındaki değerleri hesaplayalım, 100 tane değer alalım" dersek, o zaman biraz zorlanıyoruz (ben zorlanıyorum en azından... `adım_boyu = (30 - 23) / 100`?.. 
# 
# Bu gibi durumlarda, bu işi yapan hazır linspace komutumuz var:

# In[32]:


mat_duzenli_guzel_aralik = np.linspace(23,30,100)
print(mat_duzenli_guzel_aralik)
print("---------------------")
print("Bu güzel, düzenli dizinin eleman sayısı: ",mat_duzenli_guzel_aralik.size)


# Yani, linspace ile tek yapmamız gereken başlangıcı (dahil), bitişi (**o da dahil**, aman dikkat!) ve toplamda kaç tane nokta istediğimiz belirtip, arkamıza yaslanmak!

# ## Matris işlemleri (dört işlem + bir ters, bir düz)
# ### Dört temel işlem (eleman bazında)
# Matrislerimizi -birbirleriyle boyutları uyumlu olduğu sürece- dört temel işlemi kullanarak <u>eleman bazında</u> toplayabilir, çıkarabilir, çarpabilir ve hatta bölebiliriz.

# In[33]:


np.random.seed(220)
mat_a_3x2 = np.random.randint(1,10,[3,2])
print("mat_a_3x2:\n",mat_a_3x2)
print("-"*50)

mat_b_3x2 = np.random.randint(1,10,[3,2])
print("mat_b_3x2:\n",mat_b_3x2)
print("-"*50)

mat_c_2x4 = np.random.randint(1,10,[2,4])
print("mat_c_2x4:\n",mat_c_2x4)
print("-"*50)


# In[34]:


print("mat_a_3x2 + mat_b_3x2")
print(mat_a_3x2 + mat_b_3x2)


# In[35]:


print("mat_a_3x2 * mat_b_3x2")
print(mat_a_3x2 * mat_b_3x2)


# In[36]:


print("mat_a_3x2 / mat_b_3x2")
print(mat_a_3x2 / mat_b_3x2)


# ### Skaler ve Vektörel Çarpımlar
# **Skaler Çarpım**  
# Matrislerin skaler çarpımını ise `dot` fonksiyonu ile sağlarız:

# In[37]:


skaler_carpim_3x4 = np.dot(mat_a_3x2,mat_c_2x4)
print("skaler_carpim_3x4 = np.dot(mat_a_3x2,mat_c_2x4):")
print(skaler_carpim_3x4)


# **Vektörel Çarpım**  
# Vektörel çarpım ise `cross` fonksiyonu ile yapılmakta:
# $$\hat{i}\times \hat{j} = \hat{k}$$

# In[38]:


i_hat = np.array([1,0,0])
j_hat = np.array([0,1,0])
k_hat = np.array([0,0,1])

print("i_hat x j_hat = ",np.cross(i_hat,j_hat))
print("-"*50)
print("mat_a_3x2 x mat_b_3x2 =",np.cross(mat_a_3x2,mat_b_3x2))


# ### Matrisin transpozesi, tersi ve determinantı

# **Transpozesi**
# Matrislerimizin transpozesini `T` metodu ile alırız (Uzun uzadıya yazmak isterseniz transpose() komutunu kullanabilirsiniz)

# In[39]:


print(mat_a_3x2)
print("-"*50)
print(mat_a_3x2.T)
print()
print(np.transpose(mat_a_3x2))
mat_d_2x3x4 = np.random.randint(1,10,[2,3,4])
print("="*50)

print(mat_d_2x3x4)
print("-"*50)
print(mat_d_2x3x4.T)


# **Tersi**  
# Kare bir matrisin tersini `linalg` (_linear algebra_) kütüphanesinin `inv` (_inverse_) komutu ile alabiliriz:

# In[40]:


np.random.seed(220)
mat_e_3x3 = np.random.randint(1,10,[3,3])
mat_e_3x3_tersi = np.linalg.inv(mat_e_3x3)
print(mat_e_3x3)
print(mat_e_3x3_tersi)


# Bildiğiniz üzere, bir matrisin tersi, o matrisle çarpıldığında, birim matrisini veren matristir, yani:
# $$A\cdot A^{-1} = \mathbb{1}$$
# 
# Yukarıdaki hesabımızı kontrol edelim:

# In[41]:


print(np.dot(mat_e_3x3,mat_e_3x3_tersi))


# $10^{-16}$ küçüklüğünü pratik olarak 0 alabileceğimiz için, çarpımın gayet güzel bir birim matris vermiş olduğunu görüyoruz! 8)

# **'Tersimsisi'**  
# Bir matrisin tersi hesaplanırken, analitik olarak determinantından da faydalanır. Determinant ise sadece kare matrislerin bir özelliği olduğundan, bu nedenle kare olmayan matrislerin analitik olarak tersleri yoktur. Fakat, nümerik olarak kare olmayan (nxm)'lik bir matris ile çarpılıp, (nxn)'lik bir birim matrisi verebilecek (mxn)'lik bir matris bulunabilir. Kare olmayan bu ters matrisler de sanki-ters, 'tersimsi' (_pseudo-inverse_) olarak adlandırılıp, buradan kısaltmayla, yine `linalg` kütüphanesinin `pinv` komutu ile bulunur (yalnız tabii her matrisin tersi olacak diye bir garanti yoktur).

# In[42]:


np.random.seed(220)
mat_a_3x5 = np.random.randint(1,10,[3,5])
print("mat_a_3x5:")
print(mat_a_3x5)
print("-"*50)

print("mat_a_3x5_tersimsi:")
mat_a_3x5_tersimsi = np.linalg.pinv(mat_a_3x5)
print(mat_a_3x5_tersimsi)
print("-"*50)

print("mat_a_3x5 x mat_a_3x5_tersimsi =")
print(np.dot(mat_a_3x5,mat_a_3x5_tersimsi))


# **Determinantı**  
# Kare bir matrisin determinantını da şaşırtıcı olmayan bir biçimde, `linalg` kütüphanesinin `det` komutu ile elde ederiz:

# In[43]:


print("mat_e_3x3")
print(mat_e_3x3)
print("-"*50)
print("det(mat_e_3x3):")
print(np.linalg.det(mat_e_3x3))

