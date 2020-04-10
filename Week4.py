import os

os.getcwd()

def get_words(my_file=u"C:\\Users\\sncrh\\Desktop\\FilePy\\dataTx.txt"):
      my_list = []
      f = open(my_file, "r+")
      contents = f.readlines()

      for line in contents:
          words=line.split("")
          for word in words:
             my_list.append(word)
      f.close()
      return my_list

# Histogram oluşturma
def get_hist(my_list):
    my_hist={}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist=1
    return my_hist

def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(file)]
    return file_s

    lst_1=get_words()
    get_hist(lst_1)

import os
my_list=os.listdir()

for item in my_list:
    if os.path.isdir(item):
        print(item)
    if os.path.isfile(item):
        print(item)

dir_s =[dir for dir in my_list if os.path.isdir(dir)]    # Bulunan dizinde ki aktif klasörleri yazdirma
file_s=[file for file in my_list if os.path.isfile(file)]  # Bulunan dizinde ki aktif dosyaları yazdirma

dir_s,file_s