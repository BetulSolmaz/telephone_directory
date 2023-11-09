import csv
import os
import shutil


def kayit_ekle():
  with open(FILE, "a", newline='', encoding="utf-8") as fa:
    writer = csv.DictWriter(
        fa,
        fieldnames=['names', 'phone_number'] # sütun adları(keys)
    )
    ad = input("Name.:").title() # ilk harfi büyük yap
    tel = int(input("Phone number..:"))
    writer.writerow({'names':ad, 'phone_number':tel})

def kayit_listele():
  with open(FILE, "r", newline='') as fr:
      csv_read = csv.DictReader(fr,fieldnames=['names', 'phone_number'])

      for i in csv_read:
         print(i['names'],":",i['phone_number'])

def kayit_ara():
  with open(FILE, "r", newline='') as fr:
    aranan = input("Arananın adı..:").title()
    csv_read = csv.DictReader(fr)
    for i in csv_read:
        if i['names']==aranan:
           print(i["names"],":",i['phone_number'])
           break
    else:
        print("Aranan kayıt rehberde yoktur")

def kayit_sil():
   YEDEK_FILE = "yedek_phone.csv"
   with open(FILE, mode="r") as fr, open(YEDEK_FILE, mode="w") as fw:
     writer = csv.DictWriter(
        fw,
        fieldnames=['names', 'phone_number'] # sütun adları(keys)
     )
     writer.writeheader()  #sütun başlıklarını yaz
     silinen = input("Silmek istediğimiz kaydın adı..:").title()
     for i in csv.DictReader(fr):
        # silinmek istenen haricindekileri yedek dosyaya yaz.
        if i['names'] != silinen:
            writer.writerow(i)
   os.remove(FILE) #asıl dosyayı sil
   os.rename(YEDEK_FILE, FILE)

def kayit_guncelle():
  with open(FILE, mode='r') as fr, open(YEDEK_FILE, mode='w') as fw:
    writer = csv.DictWriter(
        fw,
        fieldnames=['names', 'phone_number']
    )
    writer.writeheader()
    guncellenen = input("Güncellemek istediginiz kaydin adi: ").title()
    for i in csv.DictReader(fr):
      if i['names'] == guncellenen:
        print(i['names'], 'güncelleniyor...')
        ad = input("Name:").title()
        tel = int(input('phone number:'))
        i['names'], i['phone_number']= ad, tel
      writer.writerow(i)



  shutil.move(YEDEK_FILE, FILE)


def menu():
  print("1-Kayit ekle")
  print("2-Kayit Listele")
  print("3-Kayit Ara")
  print("4-Kayit Sil")
  print("5-Kayit Güncelle")
  print("6-Cikis\n")

# wallrus operatörü
  while (secim:= int(input("Seciminiz[1-6]..:"))):
    if secim==1:
      kayit_ekle()
    elif secim==2:
      kayit_listele()
    elif secim==3:
      kayit_ara()
    elif secim==4:
      kayit_sil()
    elif secim==5:
      kayit_guncelle()
    elif secim==6:
      print("Programdan ciktiniz.")
      break
    else:
      print("1 ile 6 arasinda bir rakam giriniz.")




  #ana program
if __name__== '__main__':
    FILE = "phone.csv"
    YEDEK_FILE = 'yedek_phone.csv'
    menu()