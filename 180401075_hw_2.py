# Shell için -> python 180401075_hw_2.py input_dir_name\input_hw_2.csv output_dir_name\

import sys # Sys argümanlarını okumak için import edilen kütüphane
import csv # Csv üzerinde okuma işlemi için import edilen kütüphane

def histCreate(freqList): # Histogram oluşturma fonksiyonu
    monthD = {}
    for item in freqList:
        if (item in monthD):
            monthD[item] = monthD[item] + 1
        else:
            monthD[item] = 1
    return monthD

def mAverage(monthD):
    mAverageList = list(monthD.values()) # Dict içindeki value kısmı listeye dönüştürülüyor
    return sum(mAverageList) / len(mAverageList) # Liste toplamı eleman sayısına bölünerek ortalama elde ediliyor

def mMedian(monthD): # Listeye dönüştürmeden sonra tek ve çift eleman sayısına bağlı olarak medyan bulma işlemi
    mMedianList = list(monthD.values())
    mMedianList.sort()
    mCount = len(mMedianList)
    if mCount % 2 == 1:
        middle = int(mCount/2) + 1
        median = mMedianList[middle - 1]
    else:
        middle_1 = int(mCount / 2)-1
        middle_2 = middle_1 + 1
        median = mMedianList[middle_1] + mMedianList[middle_2]

    return median

freqList = []

with open(sys.argv[1], "r") as csvFile: # Shell üzerinden alınan dizin bilgisiyle csv dosyası okunuyor
    readCSV = csv.reader(csvFile, delimiter=';') # ; ayracına göre split etme işlemi
    for row in readCSV:
        freqList.append(row[3].split("-")[1]) # 3. kolondaki ayrılış tarihi bilgisinin ay kısmını alıp freqList listesine ekliyor

histogram = histCreate(freqList) # Histogram oluşturuluyor
fWr = open(sys.argv[2]+"180401075_hw_2_output.txt", "w") # Shell'den alınan dizin bilgisiyle txt dosyası oluşturuluyor
fWr.write("Medyan "+ str(mMedian(histogram)) + "\n") # Medyan bilgisi yazdırılıyor
fWr.write("Ortalama "+ str(mAverage(histogram))) # Ortalama bilgisi yazdırılıyor
fWr.close() # Dosya işleme kapatılıyor