#!/usr/bin/env python
# coding: utf-8

# # Uygulama Notları: 3
# ## FİZ220 - Bilgisayar Programlama II | 20/03/2020
# 
# **Matrisler (NumPy Matrix (_numpy.matrix_) Nesneleri)**
# 
# * NumPy Kütüphanesine Giriş
#   * NumPy ve SciPy kütüphaneleri
#   * Matrix değişken tipi
#   * Temel Matris İşlemleri
#     * Matris hakkında bilgi almak için kullanılan metotlar
#       * ndim
#       * shape
#       * size
#     * Matris elemanlarına erişim ve değiştirme
#     * Transpozesini (devriğini) almak
#     * Tersini (inverse) almak
#     * Matrislerin birbirleri ile toplanması ve çarpılması
#       * Toplama işlemi
#       * Çarpma işlemi
#       * Matrisin üssünü alma
#       * Matrisin 'şeklini değiştirme'
#   * Yolun sonu
#   * Kurtuluş: NumPy dizileri
#   * Aklınızdaki "o soru"
#  
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# # NumPy Kütüphanesine Giriş
# 

# ## NumPy ve SciPy kütüphaneleri
# Python'da matematiksel işlemler için iki adet temel kütüphane vardır: NumPy ve SciPy. NumPy, temel matematik ve asıl olarak sayısal hesaplamaların olmazsa olmazı matris işlemlerini içerirken, SciPy daha ileri özel fonksiyonlarını ve çözüm yöntemlerini bünyesinde barındırır. Dersimizde işlemlerimize NumPy ile başlayıp, daha ileri seviyedeki problemler için ileride SciPy'dan da yararlanacağız.
# 
# NumPy nesneleri ve işlemleri, GNU Octave ile büyük parallellik gösterir. Bu benzerliği daha ilk aşamada "matrix" değişkeni ile hemen görmek mümkündür.

# ### Matrix değişken tipi
# NumPy'da `matrix` türündeki matrisler tırnak içinde, -tıpkı Octave'da olduğu gibi- sütunlar virgül veya boşlukla; satırlar ise noktalı virgülle ayrılır (Octave'ın aksine, satır ayrımı yapmak için bir alt satıra geçmek hataya sebep olur). 
# 
# Tırnağın içerisinde köşeli parantez kullanmak opsiyoneldir.
# 
# 3x3'lük bir matris tanımlayalım:

# In[1]:


import numpy as np

# Koseli parantez kullanmadan tanimlayalim:
a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print(a)

print("---------------")

# Ayni matrisi bu sefer koseli parantez
# kullanarak tanimlayalim:
a_2 = np.matrix("[1 2, 3;4 5 6 ; 7 8 9]")
print(a_2)


# ### Temel Matris İşlemleri

# **Matris hakkında bilgi almak için kullanılan metotlar(*):**  
# * `ndim` ile matrisimizin kaç boyutlu olduğunu,
# * `shape` ile kaça kaçlık bir matris olduğunu,
# * `size` ile de matrisimizdeki eleman sayısını  
# öğreniriz:

# In[2]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print("Matrisimiz",a.ndim,"boyutlu bir matris olup,")
kaca_kac = a.shape
print(kaca_kac[0],"x",kaca_kac[1],"dağılımlı bir matristir.")
print("Matrisimizde toplam ",a.size,"adet eleman vardır.")


# _(\*) Her ne kadar "metot" terimini kullanmış olsam da, teknik olarak `matrix` nesnesinin özelliklerinden ("attribute") bahsetmekteyiz -- işleri fazla karıştırmamak için nesne özellikleri ve metotları geçişli olarak kullanılacaktır._

# **Matris elemanlarına erişim ve değiştirme**  
# Matris elemanlarına köşeli parantez içerisinde indisi belirterek erişebiliriz (indislerin 0'dan başladığına ve bütün indislerin aynı köşeli parantez içinde belirtildiğine dikkat edin!). 
# 
# Örneğin, matrisimizin 2. satırının 3. elemanına erişmek için:

# In[3]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print(a)
print("Matrisimizin 2. satırının 3. sütundaki elemanı:",a[1,2])
print("----------")
# Bu elemana yeni bir deger atayalim:
a[1,2] = 12
print("Matrisimizin 2. satırının 3. sütundaki elemanı:",a[1,2])
print(a)


# Matrisimizin bir kısmına erişmek için aralıkları kullanabiliriz:

# In[4]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print("Matrisimizin 2. ve 3. satırlarının, 1. ve 2. elemanları:")
print(a[1:3,0:2])


# Aralıkları belirtirken bitiş elemanının "kadar" anlamına geldiğini, onu **içermediğini** unutmayın!
# 
# Hazır aralıklardan söz açmışken, aralıklardaki artış miktarını 3. parametre olarak belirtiriz _(GNU Octave'da bu parametre başlangıç ve bitiş parametrelerinin ortasında yer almaktaydı)_.

# In[5]:


b = np.matrix("1 2, 3,9;4 5 6,9 ; 7 8 9 9")
print(b)
print("Matrisimizin 1. ve 3. satırlarının, 2. ve 4. sütunları")
print(b[0:4:2,:4:2])


# **Transpozesini (_devriğini_) almak:** 'T' metodu bu iş içindir:

# In[6]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print(a.T)


# Aynı işi uzun uzadıya `transpose()` fonksiyonu ile de yapabiliriz:

# In[7]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
print(np.transpose(a))


# Fonksiyon NumPy kütüphanesinde tanımlı olduğundan, çağırırken 'np' isim alanı (_namespace_) ile `np.transpose()` şeklinde çağırdığımıza dikkat edin.
# 
# (Matrisin kompleks eşlenik transpozesini almak içinse 'H' metodu kullanılır)

# **Tersini (_inverse_) almak: 'I' metodu kullanılır:**

# In[8]:


a = np.matrix("0 2 1;1 0 0;2, 0 1")
print(a.I)


# **Matrislerin birbirleri ile toplanması ve çarpılması**  
# İki matris (boyutları uyumlu olduğu sürece) birbirleri ile toplanabilir, çarpılabilir (bir matrisin üssü de alınabilir).

# * **Toplama işlemi:**

# In[9]:


a = np.matrix("1 2, 3;4 5 6 ; 7 8 9")
b = np.matrix("9 1 2; 3 2 5;1 2 0")
print("a matrisi:\n",a)
print("b matrisi:\n",b)
print("---------")
print("a+b matrisi:\n",a+b)


# * **Çarpma işlemi:**

# In[10]:


a = np.matrix("1 2, 3;4 5 6")
b = np.matrix("9 1; 3 2;1 2")
print("a matrisi:\n",a)
print("b matrisi:\n",b)
print("---------")
print("a*b matrisi:\n",a*b)


# * **Matrisin üssünü alma:**

# In[11]:


a = np.matrix("1 2;3 4")
print("a matrisi:\n",a)
print("a^2 matrisi:\n",a**2)
print("a^3 matrisi:\n",a**3)


# (Sadece tam sayı üsler alınabilir -- örneğin matrisin kökünü hesaplamak için 0.5 üssünü kullanamayız -- biraz sabır, bu sorunun da üstesinden geleceğiz! 8)

# **Matrisin 'şeklini değiştirme':**  
# Elimizde 3x4'lük bir matris olsun. Bu matrisin düzenini değiştirip, onu 6x2'lik bir matrise dönüştürmek istiyoruz. Bu durumda `shape()` metotu yardımımıza koşar:

# In[12]:


a = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(a)
kaca_kac = a.shape
print(kaca_kac[0],"x",kaca_kac[1],"dağılımlı bir matristir.")
print("-------------")
b = a.reshape(6,2)
print(b)
kaca_kac = b.shape
print(kaca_kac[0],"x",kaca_kac[1],"dağılımlı bir matristir.")


# Bazen de matrisimizi tamamıyla _düzleştirmek_ yani onu 1 boyutlu bir matrise indirmek ihtiyacını duyarız. Bu durumda `flat` metotunu kullanırız:

# In[13]:


a = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(a)
kaca_kac = a.shape
print(kaca_kac[0],"x",kaca_kac[1],"dağılımlı bir matristir.")
print("-------------")
b = np.matrix(a.flat)
print(b)
kaca_kac = b.shape
print(kaca_kac[0],"x",kaca_kac[1],"dağılımlı bir matristir.")


# `flat` metotu diğer metotların aksine bir `matrix` nesnesi değil, daha özel bir nesne (`flatiter`) döndürür (`matrix` nesnesi olmadığından ötürü de `matrix` nesnesinin sahip olduğu metotlara (örn. `shape`) sahip değildir). Bu nedenle yeni b matrisini tanımlarken `b = np.matrix(a.flat)` şeklinde, `flat`in sonucunu tekrardan `matrix` olarak atamaktayız.
# 
# Herhangi bir nesnenin cinsini `type()` fonksiyonu ile öğrenebiliriz:

# In[14]:


a = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print("a'nın cinsi:",type(a))
print("'a.flat'ın cinsi:",type(a.flat))
b = np.matrix(a.flat)
print("b'nin cinsi:",type(b))


# ## Yolun Sonu
# 
# NumPy'ın `matrix` nesnesi çok başta, dil ilk kurulurken çalışmalara hız kazandırsın diye oluşturulmuş bir nesne idi: sonrasında yeterli gelmediği için, daha gelişmiş olan _NumPy dizileri_ geliştirildi (bir sonraki dersimizin konusu).
# 
# Bu yetersizliği anlamak için, 1 boyutlu bir `matrix` nesnesi tanımlayalım:

# In[15]:


a1 = np.matrix([1,2,3])
print("1 boyutlu matrisimiz:\n",a1)


# buraya kadar bir sıkıntı yok. 
# 
# Şimdi de 2 boyutlu bir `matrix` nesnesi tanımlayalım:

# In[16]:


a2 = np.matrix("[1,2,3;4,5,6]")
print("2 boyutlu matrisimiz:\n",a2)

# veya, alternatif olarak:
a2_2 = np.matrix([[1,2,3],[4,5,6]])
print("2 boyutlu matrisimiz:\n",a2_2)


# Hâlâ iyi gidiyoruz. 
# 
# Daha da yüksek boyuta çıkalım:

# In[17]:


a3 = np.matrix([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])


# Hata mesajına ("ValueError: matrix must be 2-dimensional"), hatta daha da açık olarak, orijinal tanımın içine yerleştirilmiş kontrol mekanizmasına ("if (ndim > 2):") bakacak olursanız, `matrix` nesnelerinin en fazla 2 boyutlu olabileceğini, daha yüksek boyutlara izin verilmediğini göreceksiniz.

# Daha da dramatik olarak, [bizzat resmi NumPy matrix nesnesinin dökümanında](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html) kullanıcı bu nesneye karşı uyarılmakta:

# **Note:** 
# 
# It is no longer recommended to use this class, even for linear algebra. Instead use regular arrays. The class may be removed in the future.
# 
# _(Bu nesnenin lineer cebirde dahi kullanılması artık tavsiye edilmemektedir. Bunun yerine normal dizileri kullanın. Bu nesne gelecekte kaldırılabilir.)_

# ## Kurtuluş: NumPy dizileri
# Biz ne yapacağız? Tavsiyeyi dinleyip, çok daha esnek ve daha geniş desteklenen NumPy dizilerini kullanacağız (bkz. bir sonraki ders). Elimizdeki bir `matrix` nesnesini doğrudan ve kolaylıkla NumPy dizisine çevirmek için 'A' metotu tanımlıdır:

# In[18]:


a = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
print(a)
print("a nesnesinin cinsi:",type(a))
print("------------")
b = a.A
print(b)
print("b nesnesinin cinsi:",type(b))


# Paniğe mahal yok: şimdiye kadar gördüğümüz pek çok `matrix` metodu NumPy dizilerinde de geçerlidir (olmayanlar da numpy.linalg kütüphanesi ile gelecek -- bir sonraki derste 8)

# In[19]:


a = np.matrix("1,2,3,4;5,6,7,8;9,10,11,12")
b = a.A
print("a matrisinden cevirdigimiz b dizisi:\n",b)
print("2. satirin, 3. elemani:",b[1,2])
print("Cinsi:",type(b))
print("Boyut sayisi:",b.ndim)
print("Eleman sayisi:",b.size,"\n------------")
kaca_kac = b.shape
print("Kaca kaclik: (",kaca_kac[0],"x",kaca_kac[1],")")
print("Transpozesi:\n",b.T,"\n------------")
print("Toplama islemi\n",b+b,"\n------------")
print("Carpma islemi\n",b*b,"\n------------")
print("Us alma islemi\n",b**2,"\n------------")
print("Artik kok alma gibi tam sayi olmayan usler de desteklenmekte:")
print("Koku\n",b**(0.5),"\n------------")


# ## Aklınızdaki "o soru"##
# **_Madem ileride `matrix` nesnesini kullanmayıp dizileri (`ndarray`) kullanacaktık, ne demeye bu kadar şeyi gördük?_** 
# 
# Programlama dillerinde dizi kavramı çok geniş bir kavram. Baştan o kapıdan geçseydik, "dizi... dizi..." dedikçe kafanız karışacaktı (çünkü NumPy'da dizi dediğimiz şey pratikte matrisin ta kendisi). Kaldı ki -bir sonraki derste göreceğimiz üzere- dizi tanımında bizim Octave'dan alışageldiğimiz ve matrislerde kullandığımız satır/sütun - noktalı virgül/virgül tanımına izin verilmemekte. Bu nedenle yumuşak bir geçiş olsun istedim. 'A' metotu yardımıyla hiçbir kayıp vermeden elimizdeki matrisleri hop diye diziye çevirebildiğimiz için, bu dersi dizilere bir giriş olarak ele aldık.

# ### -Çok düşük ihtimalle de olsa- aklınızda olabilecek bir başka soru:###
# **Hocam, "nesne... nesne..." (_object... object... ;) deyip duruyorsunuz, ama sonra `type()` fonksiyonu ile cinsini sorduğumuzda bize "bir şey bir şey sınıfı (class)" diye yanıt geliyor. Nesne ile sınıf arasındaki fark nedir?**
# 
# (Öncelikle bu güzel soruyu sorduğunuz için teşekkür ederim... <kem küm...> 8) Sınıf dediğimiz şey, nesnenin ait olduğu yapıdır: nesne ise, bu yapıdan tanımladığımız bir elemandır, projeksiyon/anlık-gerçeklemedir (_instance_). Örneğin "araba" bir sınıftır: siz programınızda (hayatınızda) kullanmak üzere kendinize bu sınıftan bir eleman çektiğinizde (bir anlık-gerçekleme yaptığınızda) "Volkswagen", "Anadol", "Renault" gibi adı konulmuş bir nesne oluşturmuş olursunuz. Kafanız karıştıysa boşverin, teknik ve semantik bir ayrım var. Özetle: Sınıflar soyut (_abstract_) tanımlardır (üzerine binip bir yere gidemezsiniz), nesneler ise bu tanımlar doğrultusunda oluşturduğunuz, elle tutulur, üzerlerinde işlemler yapıp değerler atayabileceğiniz elemanlardır. Bu nedenle bir nesnenin cinsini sorduğumuzda cevap olarak onun sınıfı verilmektedir.
