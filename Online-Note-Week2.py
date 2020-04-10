from sympy import Symbol # Symbol kütüphanesi import ediliyor
x = Symbol('x') # x değişkeni oluşturuluyor
y = Symbol('y') # y değişkeni oluşturuluyor
p = x*(x + x)
print(p)

p = (x + 2)*(x + 3)
print(p)

from sympy import factor,expand # Factor, expand kütüphaneleri import ediliyor
expr = x**2 - y**2

factors = factor(expr) # Factor ile ifadeyi çarpanlarına ayırma işlemi
expand = expand(factors) # Expand ile çarpanlarına ayrılan ifadeyi çarpanlarına ayrılmadan önceki haline dönüştürme işlemi

print(factors,expand)

expr = x**3 + 3*x**2*y + 3*x*y**2 + y**3
factors = factor(expr)
print(factors)

from sympy import pprint
pprint(factors) # Matematiksel gösterim için pprint komutu kullanılıyor

x = Symbol('x') # Seri oluşturma işlemi
series = x
n = 5
for i in range(2, n+1):
    series = series + (x**i)/i
pprint(series)

expr = x*x + x*y + x*y + y*y
res = expr.subs({x:1, y:2}) # Subs komutu ile değişkenlere değer aktarma işlemi
print(res)
r = expr.subs({x:1-y})
print(r)

################################################################################
import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
sigma = Symbol('sigma') # Gauss hesaplaması için sigma,x ve mu değerleri tanımlanıyor
x = Symbol('x')
mu = Symbol('mu')
part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2)) # Gauss ifadesinin ilk kısmı hesaplanıyor
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2)) # İkinci kısmı hesaplanıyor
my_gauss_function = part_1*part_2 # Hesaplanan kısımlar çarpılarak gauss ifadesi elde ediliyor
pprint(my_gauss_function) # Matematiksel gösterimde gauss fonksiyonu gösteriliyor
# Subs komutu ile mu,sigma, x ifadelerine değerler atanarak plot ile grafik çizdiriliyor. Title ile grafiğe isimlendirme yapılıyor
syp.plot(my_gauss_function.subs({mu:10,sigma:30}), (x, -1000, 1000), title='gauss distribution')

# Yukarı da yapılan grafik for döngüsü ile farklı bir biçimde çizdiriliyor
x_values = []
y_values = []
for value in range(-50,50):
    y = my_gauss_function.subs({mu:0,sigma:10,x:value}).evalf() # Evalf ile ifade matematiksel hale getiriliyor
    y_values.append(y)
    x_values.append(value)
    print(value,y)

%matplotlib inline
import matplotlib.pyplot as plt
plt.plot(x_values,y_values) # Değerler aktarılarak grafik çizdiriliyor
plt.show() # Grafik gösteriliyor