import sympy as sym
from sympy import Symbol, Limit, Integral, exp, sqrt, pi
from sympy import pprint

p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) # Faktöriyel alma işlemleri yapılarak formülün ilk parçası hesaplanıyor
pprint(my_f_3_part_0)

my_f_3_part_1=p**x # Formülün ikinci parçası
pprint(my_f_3_part_1)

my_f_3_part_2=(1-p)**(n-x) # Formülün üçüncü parçası
pprint(my_f_3_part_2)

my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2 # Binomial distribution formülü bulunuyor
pprint(my_f_3) # Formülün matematiksel gösterimi

sym.plot(my_f_3.subs({p:0.5,n:50}),(x,0,50),title='binomial distribution plot for n=50') # Grafik arayüzde gösteriliyor
########################################################################################
t = Symbol('t') # Symbol t tanımlanıyor
St = 5*t**2 + 2*t + 8 # Türevi alınacak ifade yazılıyor
t1 = Symbol('t1')
delta_t = Symbol('delta_t')
St1 = St.subs({t: t1}) # Subs ile t1 değeri aktarılıyor
St1_delta = St.subs({t: t1 + delta_t})
Limit((St1_delta-St1)/delta_t,delta_t,0).doit() # İfadenin türevi alınıyor

x = Symbol('x')
p = exp(-(x - 10)**2/2)/sqrt(2*pi) # Integral formülü yazılıyor
Integral(p,(x,11,12)).doit().evalf() # Integral sonucu hesaplanıyor