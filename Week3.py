from sympy import FiniteSet

liste_1 = [0,5,25,100,5,5,0,100] # Liste içerisinde eleman sayısını bulan fonksiyon
def my_h(liste_1):
    my_d = {}
    for i in liste_1:
        if i in my_d:
            my_d[i]=my_d[i] + 1
        else:
            my_d[i] = 1
    return my_d
print(my_h(liste_1))

liste_1 = [0,5,25,100,5,5,0,100] # Liste içerisinde eleman sayısını bulan fonksiyon
def my_h(liste_1):
    my_d = {}
    for i  in liste_1:
        if i not in my_d:
           my_d[i] = 1
        else:
            my_d[i] +=1
    return my_d
print(my_h(liste_1))


known={0:0,1:1} # Fibonacci hesaplayan fonksiyon
def fibo_rec(n):
    if n in known:
        return known[n]
    else:
        result = fibo_rec(n-1) + fibo_rec(n-2)
        known[n]=result
        return result
x=fibo_rec(10)
print(x)



# Parametre olarak aldığı sayının listede olup olmadığını kontrol eden fonksiyon
def lookup(d,v):
    for key in range(0,len(liste_1)):
        if d[key]==v:
            return 1
    else:
        return 0

liste_1= [0,5,25,100,5,5,0,100]
print(lookup(liste_1,5100))


# Asal sayı kontrol fonksiyonu

def check_prime(number):
    if number!=1:
        for i in range(2,number):
            if number%i==0:
                return False
    else:
        return False
    return True

def probability(space,event):
    return len(event)/len(space)

space =FiniteSet(*range(1,21))
primes =[]
for num in space:
    if check_prime(num):
        primes.append(num)
event=FiniteSet(*primes)
p=probability(space,event)
print(p)