print("Bir işlem seçin: \n\n 1) Toplama \n 2) Çıkarma \n 3) Çarpma \n 4) Bölme \n 5) Kuvvet Hesapmala \n 6) Karekök Hesaplama ")

sayı1 = int(input())

#kullanıcıdan bir sayı alıcam ve o sayının değerine göre if döngüsüne koyacagım.

if (sayı1 == 1):
    try:
        Tsayı1 =int(input("toplamak istediğiniz ilk sayıyı giriniz: \t"))
        Tsayı2 =int(input("toplamak istediğiniz ikinci sayıyı giriniz: \t"))
        Sonuç= Tsayı1+Tsayı2
    except ValueError:
            print("Lütfen sadece sayı giriniz! ")
    print("toplamınız: "+str(Sonuç))
#The script gets through the calculations but fails when we try to combine our result with the text in result_string. This failure occurs because the concatenate operator (+) for strings in Python doesn't know how to comvert convert numeric types to strings implicitly.
#Bu yaptıklarımız diğer işlemler içinde benzer olacak. sadece ismini ve işlemi değiştiricez.

elif (sayı1 == 2):
    try:
        Çı_sayı1 =int(input("eksilen sayıyı yazınız: \t"))
        Çı_sayı2 =int(input("çıkan sayıyı yazınız: \t"))
        Sonuç= Çı_sayı1-Çı_sayı2
    except ValueError:
            print("Lütfen sadece sayı giriniz! ")
    
    print("Sonucunuz: "+str(Sonuç)) 
     
elif (sayı1 == 3):
    try:
        Ça_sayı1 =int(input("Çarpmak istediğiniz ilk sayıyı yazınız: \t"))
        Ça_sayı2 =int(input("Çarpmak istediğiniz ikinci sayıyı yazınız: \t"))
        Sonuç= Ça_sayı1*Ça_sayı2
    except ValueError:
            print("Lütfen sadece sayı giriniz! ")
    
    print("Sonucunuz: "+str(Sonuç))
    
elif (sayı1 == 4):
    try:
        Bö_sayı1 =float(input("Bölünen sayıyı giriniz: \t"))
        Bö_sayı2 =float(input("Bölen sayıyı giriniz: \t"))
        Sonuç= Bö_sayı1/Bö_sayı2
    except ValueError:
        print("Lütfen sadece sayı giriniz! ")
    except(ZeroDivisionError):
        print("Bölen sayı 0 olamaz! ") 
    
    print("Sonucunuz: "+str(Sonuç))
   

elif (sayı1 == 5):
        k1=input("Hesaplanılacak sayıyı giriniz:\t")
        k2=input("Hesaplanacak kuvveti giriniz:\t")
        try:
            k_1=int(k1)
            k_2=int(k2)
            print(k_1**k_2)
        except ValueError:
            print("Lütfen sadece sayı giriniz! ")
elif (sayı1 == 6):
        r1=input("Hesaplanacak sayıyı giriniz:\t")
        try:
            r_1=int(r1)
            print(r_1**0.5)
        except ValueError:
            print("Lütfen sadece sayı giriniz! ")
            
else:
    print("Lütfen tekrar deneyin. ")