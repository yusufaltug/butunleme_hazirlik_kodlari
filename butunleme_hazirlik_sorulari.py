def asal(a):
   if a>0:
       if a==1:
           return "asal değil"
       elif a>1:
           durum=False
           for i in range(2,a):
               if a%i==0:
                   durum=True
                   break
       if durum:
           return "asal değil"
       else:
           return "asal"
#print(asal(2))
#**********15
def aralik_asal(a,b):
    liste=[]
    for i in range(a,b+1):
        if i>1:
            for a in range(2,i):
                if i%a==0:
                    break
                else:
                    liste.append(i)
                    break
    return liste
# print(aralik_asal(2,8))
#**********16
def faktöriyel(n):
    if n==1 or n==0:
        return 1
    else:
        return n*faktöriyel(n-1)
# print(faktöriyel(5))
#**********17
# for i in range(1,10):
#     for j in range(1,11):
#         print("{}*{}={}".format(i,j,i*j))
#     print()
#**********18
#**********19
def amstorng(a):
    deger=0
    if a>0:
        deger+=(a//100)**3
        deger+=(a//10%10)**3
        deger+=(a%10)**3
    if a==deger:
        return "sayi amstrong"
    else:
        return "sayi amstrong değil"
    return deger
# print(amstorng(523))
def topla(n):
    if n<0:
        return "lütfen pozitif sayi girin!!"
    else:
        deger =0
        while n>0:
            deger+=n
            n-=1
        return deger
# print(topla(16))
def  çarpım():
    for i in range(1,11):
        for j in range(1,101):
            print("{}*{}={}".format(i,j,i*j))
        print()
# print(çarpım())

def ascii(n):
    return  ord(n)
# print(ascii("P"))

def çarpan(n):
    Liste=[]
    for i in range(1,n+1):
        if n%i==0:
            Liste.append(i)
    return Liste
# print(çarpan(320))
# def compress(plainText):

    # sözlük oluşturma.
#     dictionary_size = 256
#     dictionary = dict((chr(i), i) for i in range(dictionary_size))

#     word = ""
#     result = []
#     for char in plainText:
#         wordchar = word + char
#         if wordchar in dictionary:
#             word = wordchar
#         else:
#             result.append(dictionary[word])
#             # wordchar sözlüğe ekle
#             dictionary[wordchar] = dictionary_size
#             dictionary_size += 1
#             word = char

#     if word:
#         result.append(dictionary[word])
#     return result


# def decompress(compressedText):
#     from io import StringIO

#     # sözlüğü oluştur
#     dictionary_size = 256
#     dictionary = dict((i, chr(i)) for i in range(dictionary_size))
#     result = StringIO()
#     word = chr(compressedText.pop(0))
#     result.write(word)
#     for k in compressedText:
#         if k in dictionary:
#             entry = dictionary[k]
#         elif k == dictionary_size:
#             entry = word + word[0]
#         else:
#             raise ValueError('Bad compression k: %s' % k)
#         result.write(entry)
#         dictionary[dictionary_size] = word + entry[0]
#         dictionary_size += 1
#         word = entry
#     return result.getvalue()
# # Derste verilen örneği test edelim
# compressedText = compress('ABABBABCABABBA')
# print (compressedText)
# decompressedText = decompress(compressedText)
# print (decompressedText)
    




def sesli_harf_bul(n):
    sesli_harf="e,u,ı,o,ü,a,i,ö"
    top=0
    for i in n:
        for j in sesli_harf:
            if i==j:
                top+=1
    return top
# print(sesli_harf_bul("yusufalaaa"))


def sessiz_harf_bul(n):
    sesli_harf="a,e,u,ü,ı,i,o,ö"
    top=0
    for i in n:
        for j in sesli_harf:
            if i==j:
                top+=1
    return len(n)- top
# print(sessiz_harf_bul("yusufaltug"))

import random
def tahmin_oyunu():
    print("3 tahmin hakkınız var")
 
    hak=3
    while hak>0:
        a=random.randint(1,10)
      
        b=int(input("1 ile 10 arasında bir sayi tahmin edin: "))
        if a==b:
            print("tahmin doğru")
            break
        else:
            hak-=1
            print("hatalı tahmin")
    return a
# print(tahmin_oyunu())


# from random import randint
 
# rand=randint(1, 100)
# sayac=0
 
# while True:
#     sayac+=1
#     sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
#     if(sayi==0):
#         print("Oyunu İptal Ettiniz")
#         break
#     elif sayi < rand:
#         print("Daha Yüksek Bir Sayı Girin.")
#         continue
#     elif sayi > rand:
#         print("Daha Düşük Bir Sayı Girin.")
#         continue
#     else:
#         print("Rastele seçilen sayı {0}!".format(rand))
#         print("Tahmin sayınız {0}".format(sayac))


import random
def sayi_tahmin():
    print("10 tahmin hakkiniz var!")
    a=random.randint(1,100)
    hak=15
    sayac=0
    while hak>0:
        b=int(input("tahmin: "))
        if a==b:
            print("tahmin doğru program kapatiliyor ")
            sayac+=1
            break
        elif a>b:
            print("daha büyük bir sayi")
            hak-=1
            sayac+=1
            continue
        elif b>a:
            print("daha küçük bir sayi")
            hak-=1
            sayac+=1
            continue
        else:
            print("hakkiniz bitti")
            break
    print("deneme sayisi: ",sayac)
    return b
# print(sayi_tahmin())

def karakter(cumle,x):
    sayac=0
    for i in cumle:
        for j in x:
            if i==j:
                sayac+=1
    return sayac
# print(karakter("yusufaltuggg","g"))

# from tkinter import *
# from tkinter import messagebox
# pencere = Tk()
# pencere.title("neden bukadar ciddisin")
# pencere.geometry("400x300")
# uygulama = Frame(pencere)
# uygulama.grid()
# L1 = Label(uygulama, text="AdınızıGirin")
# L1.grid(padx=110, pady=10)
# E1 = Entry(uygulama, bd =2)
# E1.grid(padx=110, pady=3)
# pencere.mainloop()


def buyukharf(cumle,s=0):
    if len(cumle)>0:
        ilk=cumle[0]
        if 65<=ord(ilk)<=90:
            return buyukharf(cumle[1:],s+1)
        else:
            return buyukharf(cumle[1:],s)
    else:
        return s
# print(buyukharf("BüyükHarfLerQQQA"))

def Tr2Eng(cumle):
    ncumle=""
    List=["ı","ö","ü","ş","ç"]
    Dict={"ı":"i","ö":"o","ü":"u","ş":"s","ç":"c"}
    for i in cumle:
        if i in List:
            ncumle=ncumle+Dict[i]
        else:
            ncumle=ncumle+i
    return ncumle
# print(Tr2Eng("ıöüşç"))

def MatrisiKucult(M):
    nM=[]
    for i in range(0,len(M)-1,2):
        satir=[]
        for j in range(0,len(M[0])-1,2):
            satir.append((M[i][j]+M[i+1][j]+M[i][j+1]+M[i+1][j+1])/4)
        nM.append(satir)
    return nM
# print(MatrisiKucult(3))

# def fak(n):
#     if n==1 or n==0:
#         return 1
#     for i in range(1,n+1):
#         a*=fak(i+1)
#         if a==n:


def poldirom(n):
    if n==n[::-1]:
        return "sayi polidrom"
    else:
        return "sayi polidrom değil"
# print(poldirom("neden"))

def mükemmel(n):
    top=0
    for i in range(1,n):
        if n%i==0:
            top+=i
        elif top==n:
            return "sayi mükemmel"
        else:
            return " sayi mükemmel değil"





def basamak(n):
    sayac=0
    while n>0:
        n=n//10
        sayac+=1
    return sayac





def fibonacci(n):
    Liste=[1,1]
    while len(Liste)<n:
        Liste.append(Liste[-1]+Liste[-2])
    return Liste




def basamak(n):
    sayac=0
    while n>0:
        n=int(n/10)
        sayac+=1
    return sayac




def asal(n):
    if n>0:    
        if n==1:
            return "sayi asal değil"
        sayac=0
        for i in range(2,n):
            if n%i==0:
                sayac+=1
        if sayac==0:
            return "sayi asal"
        else:
            return "sayi asal değil"
    else:
        return "negatif sayi girmeyin"




def tek_cift(n):
    tek=0
    çift=1
    for i in range(1,n+1):
        if i%2==0:
            çift*=i
        else:
            tek+=i
    return tek,çift




def daire(n):
    cevre=2*3*n
    alan=3*(n**2)
    return cevre,alan




def ortalama(a,b):
    toplam=0
    sayac=0
    for i in range(a,b+1):
        if i%2==0:
            toplam+=i
            sayac+=1
    return toplam//sayac





def rakam_roplam(n):
    toplam=0
    while n>=10:
        k=n%10
        toplam+=k
        n=n//10
    return toplam



def bölüm_kontrol(n):
    if n%2==0 and n%3==0:
        return "sayi hem 2 hem 3ün katı"
    elif n%2==0:
        return "sayi 2nin katı"
    elif n%3==0:
        return "sayi 3ün katı"
    else:
        return "sayi 2 veye 3ün katıı değil"    



import random
def matris(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]

    matris2=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    toplam=[[0 for i in range(boyut)]for j in range(boyut)]
    for i in range(boyut):
        for j in range(boyut):
            toplam[i][j]=matris1[i][j]+matris2[i][j]
    return toplam




import random
def matris_çarpım(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    matris2=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris1)
    print(matris2)
    toplam=[[0 for i in range(boyut)]for j in range(boyut)]

    for i in range(boyut):
        for j in range(boyut):
            toplam[i][j]=matris1[i][j]*matris2[i][j]
    return toplam



import random
def diyagonal_toplam(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    diyagonaltop=0
    for i in range(boyut):
        for j in range(boyut):
            if i==j:
                diyagonaltop+=matris[i][j]
    return diyagonaltop




def bosluk_bul(n):
    bosluk=" "
    sayac=0
    for i in n:
        if i==bosluk:
            sayac+=1
    return sayac



def karşilaştir(n,m):
    if n==m:
        return "kelimeler ayni"
    else:
        return "kelimeler aynı değil"
    


def büyükmü(n):
    sayac=0
    for i in n:
        if 65<=ord(i)<=90:
            sayac+=1
    print(len(n))
    if len(n)==sayac:
        return  "harfler büyük"
    else:
        return "harfler hepsi büyük değil"
    




def kaçfak(n):
    geçici = int(n**0.5)
    fak = 1
    k = 1
    kontrol = 0
    while(k < geçici+4):
        fak *= k
        if (fak == n):
            kontrol = 1
            break
        k += 1
    
    if (kontrol == 1):
        return k
    else:
        return "Sayı Faktöriyel değil"

def yazı_tura(a,b):
    olasılıklar=["yazı","tura"]
    c=olasılıklar[random.randint(0,len(olasılıklar)-1)]
    print("oyuncu",a)
    print("oyuncu",b)
    
    if a==c:
        return "1.oyuncu kazandı"
    elif b==c:
        return "2.oyuncu kazandı"
# print(yazı_tura("yazı","tura"))



def üsal(a,b):   
    if b==1:
        return a
    elif b==0:
        return 1
    else:
        return  a*üsal(a,b-1)
# print(üsal(2,5))

def  dizi_topla(Liste,toplam=0,n=0):
    if n<len(Liste):
        toplam+=Liste[n]
        return dizi_topla(Liste,toplam,n+1)
    return toplam
# print(dizi_topla([1,2,3,4,5,6,7,8]))


def özpolidrom(cumle,ters_cumle="",indeks=-1):
    if  len(cumle)!=len(ters_cumle):
        ters_cumle+=cumle[indeks]
        return özpolidrom(cumle,ters_cumle,indeks-1)
    else:
        if cumle==ters_cumle:
            return "polidrom"
        else:
            return "polidrom değildir"
        
# print(özpolidrom("neewween"))
        
def özliste_elemenı(Liste,sayac=0):
    if sayac!=len(Liste):
        return özliste_elemenı(Liste,sayac+1)
    return sayac
# print(özliste_elemenı())



def özçevir(Liste,yeniliste=[],indeks=-1):
    if len(Liste)!=len(yeniliste):
        yeniliste.append(Liste[indeks])
        return özçevir(Liste,yeniliste,indeks-1)
    print(Liste)
    return yeniliste
# print(özçevir([1,2,3,4,5,6,7,8,9]))

import random
def matris_yerdeğiş(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    for i in range(boyut//2):
        for j in range(boyut//2):
            depo=matris[i][j]
            matris[i][j]=matris[i+3][j+3]
            matris[i+3][j+3]=depo
    return matris
#print(matris_yerdeğiş(5))
def matris_yerdeğiş2(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    for i in range(boyut):
        for j in range(boyut):
            depo=matris[0][0]
            depo2=matris[4][0]
            matris[0][0]=matris[0][4]
            matris[0][4]=depo
            matris[4][0]=matris[4][4]
            matris[4][4]=depo2
    return matris
# print(matris_yerdeğiş2(5))


#Matrisin ilk İki Satırını Değiştirme

def iki_satirdegis(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    for i in range(1):
        for j in range(boyut):
            depo=matris[i][j]
            matris[i][j]=matris[i+1][j]
            matris[i+1][j]=depo
    return matris
#print(iki_satirdegis(5))


#istenilen satır ile sütunu yer değiştir
def yerdegis(boyut,satir1,satir2):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    for i in range(boyut):
        for j in range(boyut):
            depo=matris[satir1-1][j]
            matris[satir1-1][j]=matris[satir2-1][j]
            matris[satir2-1][j]=depo
        return matris
# print(yerdegis(5,2,3))

def matris_topla(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    matris2=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris1)
    print(matris2)
    toplam=[[0 for i in range(boyut)]for j in range(boyut)]
    for i in range(boyut):
        for j in range(boyut):
            toplam[i][j]=matris1[i][j]+matris2[i][j]
    return toplam
# print(matris_topla(2))

def diyagonal_toplam(boyut):
    toplam=0
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris1)
    for i in range(boyut):
        for j in range(boyut):
            if i==j:
                toplam+=matris1[i][j]
    return toplam

# print(diyagonal_toplam(3))


#matrisin satırları toplamı

def satir_toplam(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris1)
    print()
    for i in range(boyut):
        satirtoplam=0
        for j in range(boyut):
            satirtoplam+=matris1[i][j]
        print(i+1,".saatir toplami",satirtoplam)
# print(satir_toplam(3))

def sütun_toplam(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris1)
    print()
    for i in range(boyut):
        sütuntoplam=0
        for j in range(boyut):
            sütuntoplam+=matris1[j][i]
        print(i+1,".sütun toplamı",sütuntoplam)
# print(sütun_toplam(3))
import random        
def final_matris_sorusu(boyut):
    matris1=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    yeni_matris=[[0 for i in range(2)]for j in range(2)]
    print(matris1)
    a00=0
    a01=0
    a10=0
    a11=0
    for i in range(boyut//2):
        for j in range(boyut//2):
            a00+=matris1[i][j]
    yeni_matris[0][0]=round(a00/(boyut/2)**2)
    for i in range(boyut//2):
        for j in range(boyut//2,boyut):
            a01+=matris1[i][j]
    yeni_matris[0][1]=round(a01/(boyut/2)**2)
    for i in range(boyut//2,boyut):
        for j in range(boyut//2):
            a10+=matris1[i][j]
    yeni_matris[1][0]=round(a10/(boyut/2)**2)
    for i in range(boyut//2,boyut):
        for j in range(boyut//2,boyut):
            a11+=matris1[i][j]
    yeni_matris[1][1]=round(a11/(boyut/2)**2)
    print(round(a00/(boyut/2)**2))
    print(round(a01/(boyut/2)**2))
    print(round(a10/(boyut/2)**2))
    print(round(a11/(boyut/2)**2))
    return(yeni_matris)
# print(final_matris_sorusu(6))


def istenilen_satır_toplamı(boyut,satir):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    for i in range(satir-1,satir):
        satirtoplam=0
        for j in range(boyut):
            satirtoplam+=matris[i][j]
    return satirtoplam
# print(istenilen_satır_toplamı(3,2))

def yerdeğiş5(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    x=len(matris)-1
    for i in range(boyut):
            depo=matris[i][i]
            matris[i][i]=matris[i][x]
            matris[i][x]=depo
            x-=1
    return matris
# print(yerdeğiş5(4))


# matrisin belirli bit satirını ters çevirme

def matristersçevir(boyut,satir):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    matris[satir-1] = [i for i in matris[satir-1][::-1]]
    return matris
# print(matristersçevir(5,1))


#matris alanhespalama
def alan_hesapma(boyut):
    matris=[[random.randint(0,1)for i in range(boyut)]for j in range(boyut)] 
    sayac=0
    print(matris)
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j]==1:
                sayac+=1
    return sayac
# print(alan_hesapma(4))
#evrilen listede 1ve2 , 3ve4 sayıları yer değiştiren program


def YerDegis4(Liste):
    for i in range(1,len(Liste),2):
        depo =Liste[i]
        Liste[i]=Liste[i-1]
        Liste[i-1]=depo
    return Liste
# print(YerDegis4([1,2,3,4,5,6,7,8,9,0]))


#verilen listedeki her kelimenin baş ve son harfini büyük harf yap


def elemen_sayiyi(liste,sayac=0):
    
    if sayac!=len(liste):
        return elemen_sayiyi(liste,sayac+1)

    return sayac
# print(elemen_sayiyi([1,2,3,4,4,5]))

#dizi elemanlarını ters çevirme programı rekürsif
def ters_çevir(liste,Yeniliste=[],indeks=-1):
    if(liste == len(Yeniliste)):
        return Yeniliste
    else:
        liste!=len(Yeniliste)
        Yeniliste.append(liste[indeks])
        return ters_çevir(liste,Yeniliste,indeks-1)
        
    
#print(ters_çevir([1,2,3,4,5,6,7,8,9,0]))
def matris_çarp(boyut,satir,k):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    for i in range(satir-1,satir):
        for j in range(boyut):
            matris[i][j]=matris[i][j]*k
    return matris

def yer_değiş(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    liste1=[i for i in range(boyut)]
    satir1=random.choice(liste1)
    satir2=random.choice(liste1)
    for i in range(1):
        for j in range(boyut):
            depo=matris[satir1][j]
            matris[satir1][j]=matris[satir2][j]
            matris[satir2][j]=depo
    return matris
# print(yer_değiş(5))


def maxibul(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    maximum=matris[0][0]
    makyer=(0,0)
    print()
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j]>maximum:
                maximum=matris[i][j]
                makyer=(i,j)
                break      
    return maximum,makyer
# print(maxibul(5))


def büyük_bul(liste,max=0,indeks=0):
    if indeks<=len(liste):
            return büyük_bul(liste,max=liste[indeks+1])
    else:
        return "enbüyük sayi",max
# print(büyük_bul([1,2,3,4,5,6,7]))

def diyagonal_toplam(boyut,diyagonaltop=0):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    for i in range(boyut):
        for j in range(boyut):
            if i==j:
                diyagonaltop+=matris[i][j]
    return diyagonaltop
# print(diyagonal_toplam(5))
# boyut=[1,2,3,4,5,6,7,8]
# a=int(len(boyut))
# for i in range(len(boyut)//2):
#     print("a")



# final 2.sortu
def Topla(Liste):
    n = len(Liste)
    yListe = []
    for i in range(n//2):
        yListe.append(Liste[i] + Liste[n-i-1])
    
    if n%2==1:
        yListe.append(Liste[n//2])
    return yListe

# print(Topla([1,2,3,4,5,6,7,8]))

#Verilen bir cümledeki büyük harf sayısını özyinelemeli bulan algoritmayı yazınız?
def büyük_bul(n):
    sayac=0
    for i in n:
        if 65<=ord(i)<=90:
            sayac+=1
    return sayac
# print(büyük_bul("nedenNbuLDSADLAadar"))


def büyük_bul(n,sayac=0):
    if len(n)>0:
        ilk=n[0]
        if 65<=ord(ilk)<=90:
            return büyük_bul(n[1:],sayac+1)
        else:
            return büyük_bul(n[1:],sayac)
    return sayac
# print(büyük_bul("nerdenDASDADW"))


# Başlangıç Saat, Dakika ve Saniye bilgileri verildiğinde ilk5 saniyelik saat bilgisini listeye ekleyen fonsiyonu yazınız?

def DigitalSaat(saat,dakika,saniye):
    liste1=[]
    for i in range(5):
        liste1.append(str(saat)+"."+ str(dakika)+"."+str(saniye))
        saniye+=1
        if saniye==60:
            dakika+=1
            saniye=0
        if dakika==60:
            saat+=1
            dakika=0
        if saat==24:
            saat=0
    return liste1

# print(DigitalSaat(23,59,57))


def BozanElamanİndeksi(liste):
    c=0
    b=liste[0]-liste[1]

    for i in range(len(liste)):
        if liste[i]-liste[i+1]==b:

           c+=1
        else:
            c+=2

            break

    return c
#print(BozanElamanİndeksi([1,2,5,6,7,8]))
def basamakbul(a):
    liste = []
    while(a > 0):
        bas = a % 10

        liste.append(bas)
        a //= 10
    return liste

# print(basamakbul(123))
def sayidaki_tekleribul(n):
    sayac=0
    while n>0:
        bas=n%10
        if bas%2==1:
            sayac+=1
        n//=10
    return sayac
# print(sayidaki_tekleribul(132753222222))

def basamak_değeri_kadar(n):
    while n>0:
        bas=n%10
        liste=[]
        liste.append(bas*"*")
        bas//10
    return liste
print(basamak_değeri_kadar(124))
a=(4*"*")
print(a)
def sesli_harf(cumle):
    yeni=" "
    sesli_harf="a,e,u,ı,o,ü,i,ö"
    for i in cumle:
        if i in sesli_harf:
            yeni+=i
    return yeni
# print(sesli_harf("nedenbukadarciddisin"))


def sesli_harf(cumle):
    sayac=0
    sesli_harf="ci"
    for i in cumle:
        if i in sesli_harf:
            sayac+=1
    return sayac
# print(sesli_harf("nedenbukadarciddisin"))



def sansür(n,kelime,indeks=0):
    
    for i in n:
        if i!=kelime:
            indeks+=1
        else:
            break
    if kelime in n:
        depo=kelime
        n[indeks]=len(kelime)*"*"
    return n
# print(sansür(["neden","bu","kadar","ciddisin"],"ciddisin"))


def sessiz_harf_bul(n):
    liste=[]
    sesli_harf="a,e,u,ı,o,ü,i,ö"
    for i in n:
        if i not in sesli_harf:
            liste.append("-"+i+"-")
    return liste
# print(sessiz_harf_bul("nedenbukadarciddisin"))
def buyuk_harf_kucult_ve_alt_cizgi_ekle_alg(metin):
    duzeltilmis_metin = ""
    for karakter in metin:
        if 'A' <= karakter <= 'Z':  
            duzeltilmis_metin += chr(ord(karakter) + 32)  
        elif karakter == ' ':   
            duzeltilmis_metin += '_'  
        else:
            duzeltilmis_metin += karakter  
    return duzeltilmis_metin
verilen_metin = "Bu Bir Örnek METİNDİR."
duzeltilmis_metin = buyuk_harf_kucult_ve_alt_cizgi_ekle_alg(verilen_metin)
# print(duzeltilmis_metin)



def kelime_sayisi_bul_alg(metin, aranan_kelime):
    kelime_uzunlugu = len(aranan_kelime)
    metin_uzunlugu = len(metin)
    sayac = 0
    
    i = 0
    while i < metin_uzunlugu:
        j = 0
        while j < kelime_uzunlugu and i + j < metin_uzunlugu:
            if metin[i + j] != aranan_kelime[j]:
                break
            j += 1
        
        if j == kelime_uzunlugu:
            sayac += 1
            i += kelime_uzunlugu
        else:
            i += 1
    
    return sayac

# verilen_metin = "Bu bir örnek metindir. Bu metin içinde b harfi geçen kelimeleri bulacağız. Bu"
# aranan_kelime = "Bu"
# sayac = kelime_sayisi_bul_alg(verilen_metin, aranan_kelime)
# print(f"'{aranan_kelime}' kelimesi metin içinde {sayac} kez geçiyor.")

def diyagonalikilitoplam(boyut):
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    sol=0
    sağ=0
    
    for i in range(boyut):
        for j in range(boyut):
            if i==j:
                sol+=matris[i][j]
            if i+j== len(matris) -1:
                
                sağ+=matris[i][j]
                
    return sol-sağ
# print(diyagonalikilitoplam(5))
#1111
# liste=[846, 9311, 641, 9721]
# liste2=[]
# for i in liste:
#     liste2.append(liste[::-1])
# print(liste2)


def ter_çevir(liste,liste2=[],indeks=0):
    liste2=[]
    if len(liste)!=len(liste2):
        liste2.append(liste[indeks])
        return ters_çevir(liste,liste2,indeks-1)
    else:
        return liste2
# print(ter_çevir(9311, 641, 9721))


#verilen matris içinde en çok tekrar eden sayıyı bulun
def matris_tekrar(boyut):
    sayac=0
    matris=[[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
    print(matris)
    print()
    liste=[]
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] not in liste: 
                liste.append(matris[i][j])
    maximum=liste[0]
    a=1
    for i in range(len(liste)//2):
        if liste[a]>maximum:
            maximum=liste[a]
            a+=1
    return liste,maximum
# print(matris_tekrar(5))
# Verilen iki dizide ortak olmayan harfleri bulunuz.
def ortakolmayanharf(dizi1,dizi2):
    liste=[]
    for i in dizi1:
        if i not in dizi2:
            liste.append(i)
    return liste
# print(ortakolmayanharf("nedenkadarciddisin","nedenbukadarciddisin"))

 
 
 
def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# insertion_sort(liste)
# print("Sıralanmış Liste:", liste)


def sırala(liste):
    for i in range(1,len(liste)):
        depo=liste[i]
        j=i-1
        while j>=0 and depo <liste[j]:
            liste[j+1]=liste[j]
            j-=1
        liste[j+1]=depo
    return liste
# print(sırala([1,3,5,2,4,8,6,7,9]))


def bosluk(n):
    bosluk=" "
    temiz_liste=""
    for i in n:
        if i not in bosluk:
            temiz_liste+=i
    return temiz_liste
# print(bosluk("neden bu kadar ciddisin"))


def sayibul(n,b):
    sayac=0
    for i in n:
        if i==b:
            sayac+=1
    return sayac
# print(sayibul("nedenb ukada r ciddi  sin a"," ")) 