import random

random.random()
s = random.randint(1, 100) # Random sayı üreterek değişkene atama

# Belirtilen aralıklarda n tane sayı üretip liste olarak dönderme işlemi
def get_n_random_numbers(n=10, min_=-5, max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_, max_))
    return numbers

get_n_random_numbers()
get_n_random_numbers(15, -4, 4)

# Bu liste için [0, -4, 8, -1, 0, -3, 6, 3, 0, 1] listenin her elemanının tekrarlanma sayısını alma
histgram_1 = [(-4,1),(-3,1),(-1,1),(0,2),(1,1),(3,1),(6,1),(8,1)]

my_list = get_n_random_numbers(15, -4, 4)
my_list
sorted(my_list)

# Parametre olarak aldığı dizide ki her elemanın tekrar sayısını dict olarak döndüren fonksiyon
def my_frequency_with_dict(list):
    frequency_dict = {}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item] = frequency_dict[item] + 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

my_frequency_with_dict(my_list)

# Parametre olarak aldığı dizide ki her elemanın tekrar sayısını tuple formatında dizi olarak dönderen fonksiyon
def my_frequency_with_list_of_tuples(list_1):
    frequency_list = []
    for i in range(len(list_1)):
        s = False
        for j in range(len(frequency_list)):
            if(list_1[i] == frequency_list[j][0]):
                frequency_list[j][1] = frequency_list[j][1] + 1
                s = True
        if(s == False):
            frequency_list.append([list_1[i],1])
    return frequency_list

my_list = [2, 3, 2, 5, 8, 2, 4, 3, 3, 2, 8, 5, 2, 4, 4, 4, 4, 4]
result_1 = my_frequency_with_dict(my_list)
result_2 = my_frequency_with_list_of_tuples(my_list)
result_1,result_2

# Parametre olarak aldığı dict içinde ki en çok tekrar eden elemanı ve tekrar sayısını döndüren fonksiyon
def my_mode_with_dict(my_hist_d):
    frequency_max = 1
    mode = -1
    for key in my_hist_d.keys():
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode, frequency_max

my_list_100 = get_n_random_numbers(100, -40, 40)
my_hist_1 = my_frequency_with_dict(my_list_100)
my_mode_with_dict(my_hist_1)

# Parametre olarak aldığı dizi içinde ki en çok tekrar eden elemanı ve tekrar sayısını döndüren fonksiyon
def my_mode_with_list(my_hist_list):
    frequency_max = -1
    mode = -1
    for item, frequency in my_hist_list:
        print(item, frequency)
        if frequency > frequency_max:
            frequency_max = frequency
            mode = item
    return mode,frequency_max

# Parametre olarak aldığı item dizi içerisinde var ise tuple formatında item'ı ve indisini döndüren fonksiyon
def my_linear_search(my_list, item_search):
    found = (-1, -1)
    n = len(my_list)
    for indis in range(n):
        if my_list[indis] == item_search:
            found = (my_list[indis], indis)
    return found

# Listenin ortalamasını döndüren fonksiyon
def my_mean(my_list):
    s, t = 0, 0
    for item  in my_list:
        s = s+1
        t = t+item
    mean_ = t/s
    return mean_

# Dizide ki elemanları bubble sort yöntemiyle sıralayan fonksiyon
def my_bubble_sort(my_list):
    n = len(my_list)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if not(my_list[j] < my_list[j+1]):
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

# Parametre olarak aldığı elemanı ikili arama methoduyla listede arayarak var ise tuple formatında döndüren fonksiyon
def my_binary_search(my_list, item_search):
    found = (-1,-1)
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if my_list[mid] == item_search:
            return my_list[mid],mid
        elif my_list[mid] > item_search:
            high = mid - 1
        else:
            low = mid + 1
    return found

my_list_1 = get_n_random_numbers(10)
print("liste ",my_list_1)
my_list_2 = my_bubble_sort(my_list_1)
print("sıralı liste",my_list_2)
my_binary_search(my_list_2,3)

# Listede ki tek ve çift eleman sayısına bağlı olarak medyan bulan fonksiyon
def my_median(my_list):
    my_list_2 = my_bubble_sort(my_list_1)
    n = len(my_list_2)
    if n % 2 == 1:
        middle = int(n/2) + 1
        median = my_list_2[middle]
    else:
        middle_1 = my_list_2[int(n/2)]
        middle_2 = my_list_2[int(n/2)+1]
        median = (middle_1 + middle_2) / 2

    return median

my_list_2 = get_n_random_numbers(5, -10, 10)
print(my_median(my_list_2))