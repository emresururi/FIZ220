#!/usr/bin/env python
# coding: utf-8

# # Uygulama Notları: 1
# ## FİZ220 - Bilgisayar Programlama II | 06/03/2020
# **Python'la 'Merhaba Dünya!'**
# 
# * Python'a Giriş
#  * Python hakkında çok kısa bilgi
#  * Python'ın popülerliği
#  * Hangi Python IDE'sini kullanmalıyız?
# * Jupyter ortamı
#  * Hücreler
# * Python kütüphaneleri
# * Jupyter sayfanızı aktarma
#  
# Dr. Emre S. Taşcı, emre.tasci@hacettepe.edu.tr  
# Fizik Mühendisliği Bölümü  
# Hacettepe Üniversitesi

# # Python'a Giriş
# ## Python hakkında çok kısa bilgi
# Python dili 1990 yılında, Guido van Rossum tarafından geliştirilmiştir. Yüksek seviye bir dil olup, işlemci tarafında pek çok zahmetli işlem (örn. _hafıza ayarlamaları, çöp toplama_) sistem tarafından otomatik olarak halledilmektedir. Ayrıca nesne tabanlı bir yapıya sahiptir (daha da ileri gidersek: Python'da hemen hemen **her şey** bir nesnedir).
# 
# Dil, ismini İngiliz anarşist komedi topluluğu [Monty Python](https://en.wikipedia.org/wiki/Monty_Python)'dan almaktadır (hatta, bizzat van Rossum'un örneklerde kullanılacak değişken ve durumların da grubun skeçlerinden seçilmesi konusunda ricası vardır).

# ## Python'ın popülerliği
# 
# Yaygın kütüphane desteği ve internetin doğrudan işletim sistemlerinde kaynak olarak kullanımının önünün açılması sonucu 2000'li yıllardan itibaren "en çok kullanılan diller" listelerinde hep üst sıraya yerleşmiştir. Bu listelerde kriter sayılan [TIOBE endeksinde](https://www.tiobe.com/tiobe-index/) Python, Java (%17.8) ve C'den (%16.3) sonra %10.1'lik kullanımla 3. sırada yer almaktadır ve [yükselişini kararlı bir biçimde sürdürmektedir](https://www.tiobe.com/tiobe-index/python/). GitHub ve Stack Overflow istatistiklerinden yola çıkılarak hazırlanan bir diğer endeks olan [RedMonk sıralamasında](https://redmonk.com/sogrady/2020/02/28/language-rankings-1-20/) ise Ocak 2020 itibarı ile JavaScript ile birinciliğe başabaş oynamaktadır. İnternette en çok başlangıç ve tanıtımları ziyaret edilen diller üzerinden sıralama yapan PYPL endeksinde ise açık ara ile (Python: %30.1; Java: %18.8) birinci sıradadır. _(Bütün istatistikler 2020 Mart ayı açıklamalarına dairdir)_

# ## Hangi Python IDE'sini kullanmalıyız?
# Temel olarak Python yorumlanarak çalışan ("interpreted") bir dil olduğundan, bir yorumcuya ("interpreter") ihtiyaç duyar. Python'ın kendisi ile gelen _IDLE_ IDE'si temelde iş görse de, yaşamı kolaylaştırıcı pek çok özellikten mahrumdur. Bu nedenle, zorunlu durumlar dışında pek kullanılmaz.
# 
# Python'da program geliştirmek için yoğun olarak [PyCharm](https://www.jetbrains.com/pycharm/) ve [IPython](https://ipython.org/) IDE'lerini kullanmaktadırlar. [Anaconda](https://www.anaconda.com/) ise, IPython IDE'sini (Jupyter üzerinden) ve pek çok popüler sayısal analiz kütüphanesini içinde barındıran bir yazılım paketi olup, kullanım kolaylığı açısından benim de tavsiye ettiğim IDE'dir.
# 
# Jupyter yoluyla bir web tarayıcısında yazılan Jupyter defterleri (_ipynb - IPython Notebooks_) gerek görsel, gerekse kullanım açısından gerçekten de akıcı bir geliştirmeye olanak tanır (bu uygulama notları da bizzat Jupyter ile hazırlanmaktadır 8).

# # Jupyter ortamı
# ## Hücreler
# Jupyter'ı bir kelime işlemci (örn: MS Word) belgesi olarak düşünebilirsiniz: bu dökümanın bazı yerlerine açıklamalar yazıp, aralara da resimler eklediğiniz gibi, bir Jupyter defterinin istediğiniz kısımlarına yazı yazıp, istediğiniz kısımlarında da programınızı yazıp çalıştırabilirsiniz -- tıpkı şu anda yapmakta olduğum gibi. Python'da basit bir işlem yapalım:

# In[1]:


5 + 7


# Yukarıdaki işlemin olduğu kısım, şu anda bu satırların olduğu kısım gibi, çalışmamızın bir parçası olup, "hücre" (_cell_) adıyla anılırlar. Bir hücre şu üç çeşitten biri olabilir:
# 1. **Kod Hücresi:** Bu hücre -doğal olarak- en temel hücre tipimiz olacaktır. Buraya yazılan kodlar çalıştırılıp, çıktıları da aynı hücrenin altında monte şekilde gösterilecektir. (Kısayol tuşu: **Y**)
# 2. **Metin Hücresi:** Metin hücreleri de şu anda okumakta olduğunuz hücreler gibi, bilgi paylaşımı amacıyla oluşturulan hücrelerdir. Bu kısımları programlarda açıklamaları yazdığımız yorum satırlarının gelişmiş versiyonları olarak düşünebiliriz. **Kalın**, _italik_ vs. şeklindeki basit biçimlendirmelere de izin verirler (bu biçimlendirmeler için kullanılan notasyona **MarkDown** notasyonu adı verilmekte olup, detaylı açıklamalar ve örnekler için [Adam Pritchard'ın kapsamlı sayfasına bakabilirsiniz](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). Metin hücreleri, MathJax motoru sayesinde, karmaşık formülleri $\LaTeX$ yoluyla yazmanıza da izin vermektedir, örneğin: $\oint E \cdot \text{d}A = \frac{\rho}{\epsilon_0}$. (Kısayol tuşu: **M**)
# 3. **Çiğ Hücre:** Çiğ hücreler bir kodu (veya _şiiri_ ;) şeklini bozmadan, normalde çeşitli anlamlara gelen sembolleri olduğu gibi girmenize yarar. Şimdilik pek kullanacağımız bir hücre tipi değil. (Kısayol tuşu: **R**)
# 
# Hücrelerle ilgili çok kullanacağınız birkaç diğer kısayol tuşu ise şunlardır:
# * &lt;Enter> : Seçili hücreyi değiştirme moduna alır.
# * &lt;CTRL>+&lt;Enter> : Seçili olan hücreyi _çalıştırır_ (kod hücresi ise yazılı kodu çalıştırıp, çıktısını döndürür; metin hücresi ise markdown ve LateX sembollerini işler)
# * b (below/aşağı) ve a (above/yukarı) : Seçili olan hücrenin aşağısına (veya yukarısına) yeni bir hücre ekler.
# * &lt;CTRL>+&lt;Shift>+&lt;s> (split) : Seçili olan hücreyi o anda imleçin olduğu satırdan iki ayrı hücreye böler.
# * h (help) : Kısayol tuşlarının karşılıklarını gösterir.
# 
# Bütün defteri çalıştırmak için ise **Kernel** menüsünden "Restart & Run All" diyebilirsiniz - bu durumda, defteri yeni açmışsınız gibi çekirdek (_kernel_) baştan yüklenir ve her şey sıfırdan çalıştırılır; **Cell** menüsünden "Run All" seçeneği ise, hücreleri en tepeden aşağıya doğru sırayla çalıştırır fakat daha önce çalıştırdığınızda edinilen (değişken değerleri gibi) bilgileri de kullanır. Kod hücrelerinin sol başlarındaki sayılar hücrelerin hangi sırayla çalıştırıldıklarını işaret eder (beklemediğiniz bir çıktı almanız halinde gidişatı kolayca takip edip, durumu anlayabilmeniz için).

# # Python kütüphaneleri
# Python, çeşitli işlere özgü (örn: matris hesabı, grafik çizimi, veritabanı, konumsal işlemler, görüntüleme, ses işleme, yapay zeka vs.) metotları barındıran pek çok kütüphane ile desteklenir; zaten bu kadar geniş kullanıcı sayısına ulaşmasında da bu çeşitliliğin büyük katkısı vardır. Python'da kütüphaneler _modül_ (_module_) olarak adlandırılır.
# 
# Sayısal hesap işlemlerinde yoğun olarak kullanacağımız üç adet kütüphane:
# 1. NumPy : Temel matematiksel fonksiyonları ve gelişmiş dizi & matris tiplerini, işlemlerini içerir. GNU Octave'da yaptığımız hemen her şeyi bu kütüphanedeki tanımlar çerçevesinde yapabiliriz.
# 2. SciPy : NumPy'ın bir üst kütüphanesi olarak düşünebiliriz. İleri fonksiyonlar ve metotlar bu kütüphanede bulunur, hayli kapsamlıdır.
# 3. MatPlotLib : Grafik çizmek için GNU Octave / MATLAB benzeri komutlarla işimizi kolaylaştırır.
# 
# Python'da istediğimiz kütüphaneyi:  
# `import <kütüphane-adı> as <kütüphane-adı-kısaltması>`  
# veya  
# `from <kütüphane-adı> import <istenilen-metotlar>`  
# biçimiyle çağırabiliriz. İki kullanım biçimi birbirinden farklıdır: İlkinde kütüphane elemanlarını çağırırken kütüphanenin kısa adıyla işaret ederiz (bu tür aidiyete "isimuzayı" (_namespace_) denir); ikinci türde ise kütüphane elemanları doğrudan ana isimuzayına eklenir, ilgili kütüphaneyi işaret etmemiz gerekmez. İkinci yaklaşım daha pratik gelse de birden fazla kütüphanenin aktarıldığı durumlarda karışıklığa yol açabilir, bu nedenle mümkün mertebe ilk yaklaşımı kullanmak gerekir. 
# 
# **Not:** ikinci yaklaşımla sadece bir tek metot eklense bile, Python yine de bütün kütüphaneyi yükleyecektir. `import numpy as np` ile `from numpy import pi` arasında performans bakımından hiçbir fark yoktur: iki durumda da bütün NumPy modülü yüklenir - ikinci durumda sadece _pi_'nin kullanımı mümkün olsa bile!

# In[2]:


# Örnek:
print(pi) # tanımlı olmadığından hata gelecektir


# In[3]:


# Kütüphaneyi 'np' kısaltmasıyla aktaralım:
import numpy as np
print(np.pi) # pi de tanımlı,
print(np.e) # e de...


# In[4]:


# Kütüphaneden sadece pi'yi aktarıp, öyle çağıralım:
from numpy import pi
print(pi) # pi tanımlı,
print(e) # fakat e değil...


# # Jupyter sayfanızı aktarma
# Jupyter'da hazırladığınız sayfalar otomatik olarak sıklıkla kaydedilir (bunun yanısıra, siz de sol üstteki ikondan veya &lt;CTRL>+s kestirmesinden dilediğiniz zaman kaydedebilirsiniz).
# 
# Dosyanızı bir başkasına doğrudan veya farklı bir biçimde göndermek içinse **File** menüsünden "Download as..." seçeneğini kullanabilirsiniz. Bu menüde çıkan seçeneklerden başlıcaları:
# 
# * Notebook (.ipynb) : Oluşturmuş olduğunuz defterin tam olarak bir kopyasını verir.
# * Python (.py) : İlgili kod kısımlarını tutar, yazı kısımlarını ise yorum olarak işleyip verir.
# * HTML (.html) : Grafikler de dahil olmak üzere, bütün içeriği web tarayıcınızda gördüğünüz şekilde _statik olarak_ kaydeder fakat kod doğrudan çalıştırılamaz ya da siz defterdekine benzer şekilde işlemler yapamazsınız.
# * PDF (.pdf)
