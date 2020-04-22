from sympy import *
import sympy as sym
import matplotlib.pyplot as plt

number = 180401075
mod = sym.Mod(number, 4) # mod = 3 = Exponential Distribution

l = Symbol('lambda') # İki durumun gözlenmesi için gereken ortalama süre
x = Symbol('x') # İki durum arasında veya ilk durumun orta çıkması için gereken süre

# Exponential Distribution = Bir Poisson sürecindeki olaylar arasındaki süreyi tanımlayan olasılık dağılımını temsil eder.
# Bir öğrenci sınav sorunu 2 dk ortalama süre ile üstel dağılım olarak çözsün.
# Örnek olarak öğrencinin soruyu 5 dk da çözme olasılığını üstel dağılım olarak bulalım.

exponential = (l * (sym.exp(-l*x))) # Exponential dağılım formülü bulunuyor. sym.exp fonksiyonu e ifadesinin üssünü alıyor
pprint(exponential) # Formülün matematiksel gösterimi

# sympy kütüphanesi ile grafik çizdirme işlemleri
def sympyGraph():
    sym.plot(exponential.subs({l:2}), (x, 0, 5), title = 'Exponential Distribution') # Subs ile değerler aktarılıyor

# matplotlib kütüphanesi ile grafik çizdirme işlemleri
def matplotGraph():
    x__values = []
    y__values = []

    for i in range(6):
        y = exponential.subs({x:i, l:2}).evalf() # x'e karşılık gelen y değerleri bulunuyor
        x__values.append(i)
        y__values.append(y)

    plt.plot(x__values, y__values) # x ve y listelerinin değerleri aktarılıyor
    plt.show()# grafik arayüzde gösteriliyor

sympyGraph()
print("\n")
matplotGraph()