import sqlite3 as sql
from ui import UI
con = sql.connect("emlak.db")
cursor = con.cursor()
menu = UI(["Ev_islem","isletme_islem","Arsa_islem","kiralik_islem"])
class Ev_islem():
    cursor.execute("create table if not exists ev (id integer primary key autoincrement,ev text,fiyat int,adres text,metrekare int)")
    def __init__(self):
        self.menu = UI(["Ev Ekle","Ev Sil","Ev Listele","Ev Güncelle/adres degisikligi"])
    def Ev_Ekle(self):
        try:
            ev = input("Ev Adı: ")
            fiyat = int(input("Fiyat: "))
            adres = input("Adres: ")
            metrekare = int(input("Metrekare: "))
            cursor.execute("insert into ev (ev,fiyat,adres,metrekare) values (?,?,?,?)",(ev,fiyat,adres,metrekare))
            con.commit()
            print("Ev eklendi")
        except:
            print("Hatalı giriş")
    def Ev_Sil(self):
        try:
            cursor.execute("select * from ev")
            evler = cursor.fetchall()
            for ev in evler:
                print(ev)
            ev_id = int(input("Silmek istediğiniz evin id'sini giriniz: "))
            cursor.execute("delete from ev where id = ?",(ev_id,))
            con.commit()
            print("Ev silindi")
        except:
            print("Hatalı giriş")
    def Ev_Listele(self):
        cursor.execute("select * from ev")
        evler = cursor.fetchall()
        for ev in evler:
            print(ev)
    def Ev_Guncelle(self):
        try:
            cursor.execute("select * from ev")
            evler = cursor.fetchall()
            for ev in evler:
                print(ev)
            ev_id = int(input("Güncellemek istediğiniz evin id'sini giriniz: "))
            ev = input("Ev Adı: ")
            fiyat = int(input("Fiyat: "))
            adres = input("Adres: ")
            metrekare = int(input("Metrekare: "))
            cursor.execute("update ev set ev = ?,fiyat = ?,adres = ?,metrekare = ? where id = ?",(ev,fiyat,adres,metrekare,ev_id))
            con.commit()
            print("Ev güncellendi")
        except:
            print("Hatalı giriş")
class isletme_islem():
    cursor.execute("create table if not exists isletme (id integer primary key autoincrement,isletme text,fiyat int,tip text)")
    def __init__(self):
        self.menu = UI(["İşletme Ekle","İşletme Sil","İşletme Listele","İşletme Güncelle"])
    def İşletme_Ekle(self):
        try:
            isletme = input("İşletme Adı: ")
            fiyat = int(input("Fiyat: "))
            tip = input("İşletme tipi: ")
            cursor.execute("insert into isletme (isletme,fiyat,tip) values (?,?,?)",(isletme,fiyat,tip))
            con.commit()
            print("İşletme eklendi")
        except:
            print("Hatalı giriş")
    def İşletme_Sil(self):
        try:
            cursor.execute("select * from isletme")
            isletmeler = cursor.fetchall()
            for isletme in isletmeler:
                print(isletme)
            isletme_id = int(input("Silmek istediğiniz işletmenin id'sini giriniz: "))
            cursor.execute("delete from isletme where id = ?",(isletme_id,))
            con.commit()
            print("İşletme silindi")
        except:
            print("Hatalı giriş")
    def İşletme_Listele(self):
        cursor.execute("select * from isletme")
        isletmeler = cursor.fetchall()
        for isletme in isletmeler:
            print(isletme)
    def İşletme_Güncelle(self):
        try:
            cursor.execute("select * from isletme")
            isletmeler = cursor.fetchall()
            for isletme in isletmeler:
                print(isletme)
            isletme_id = int(input("Güncellemek istediğiniz işletmenin id'sini giriniz: "))
            isletme = input("İşletme Adı: ")
            fiyat = int(input("Fiyat: "))
            tip = input("İşletme tipi: ")
            cursor.execute("update isletme set isletme = ?,fiyat = ?,tip = ? where id = ?",(isletme,fiyat,tip,isletme_id))
            con.commit()
            print("İşletme güncellendi")
        except:
            print("Hatalı giriş")
class Arsa_islem():
    cursor.execute("create table if not exists arsa (id integer primary key autoincrement,arsa text,fiyat int,yer text,donum int)")
    def __init__(self):
        self.menu = UI(["Arsa Ekle","Arsa Sil","Arsa Listele","Arsa Güncelle"])
    def Arsa_Ekle(self):
        try:
            arsa = input("Arsa Adı: ")
            fiyat = int(input("Fiyat: "))
            yer = input("arsanın bulunduğu yer: ")
            donum = int(input("Donum: "))
            cursor.execute("insert into arsa (arsa,fiyat,yer,donum) values (?,?,?,?)",(arsa,fiyat,yer,donum))
            con.commit()
            print("Arsa eklendi")
        except:
            print("Hatalı giriş")
    def Arsa_Sil(self):
        try:
            cursor.execute("select * from arsa")
            arsalar = cursor.fetchall()
            for arsa in arsalar:
                print(arsa)
            arsa_id = int(input("Silmek istediğiniz arsanın id'sini giriniz: "))
            cursor.execute("delete from arsa where id = ?",(arsa_id,))
            con.commit()
            print("Arsa silindi")
        except:
            print("Hatalı giriş")
    def Arsa_Listele(self):
        cursor.execute("select * from arsa")
        arsalar = cursor.fetchall()
        for arsa in arsalar:
            print(arsa)
    def Arsa_Güncelle(self):
        try:
            cursor.execute("select * from arsa")
            arsalar = cursor.fetchall()
            for arsa in arsalar:
                print(arsa)
            arsa_id = int(input("Güncellemek istediğiniz arsanın id'sini giriniz: "))
            arsa = input("Arsa Adı: ")
            fiyat = int(input("Fiyat: "))
            yer = input("arsanın bulunduğu yer")
            donum = int(input("Donum: "))
            cursor.execute("update arsa set arsa = ?,fiyat = ?,yer = ?,donum = ? where id = ?",(arsa,fiyat,yer,donum,arsa_id))
            con.commit()
            print("Arsa güncellendi")
        except:
            print("Hatalı giriş")
class kiralik_islem():
    cursor.execute("create table if not exists kiralik (id integer primary key autoincrement,kiralik text,fiyat int,sure int)")
    def __init__(self):
        self.menu = UI(["Kiralık Ekle","Kiralık Sil","Kiralık Listele","Kiralık Güncelle"])
    def Kiralık_Ekle(self):
        try:
            kiralik = input("Kiraladigin şey: ")
            fiyat = int(input("Fiyat: "))
            sure = int(input("Kiralama süresi/gün: "))
            cursor.execute("insert into kiralik (kiralik,fiyat,sure) values (?,?,?)",(kiralik,fiyat,sure))
            con.commit()
            print("Kiralık eklendi")
        except:
            print("Hatalı giriş")
    def Kiralık_Sil(self):
        try:
            cursor.execute("select * from kiralik")
            kiralikler = cursor.fetchall()
            for kiralik in kiralikler:
                print(kiralik)
            kiralik_id = int(input("Silmek istediğiniz kiralığın id'sini giriniz: "))
            cursor.execute("delete from kiralik where id = ?",(kiralik_id,))
            con.commit()
            print("Kiralık silindi")
        except:
            print("Hatalı giriş")
    def Kiralık_Listele(self):
        cursor.execute("select * from kiralik")
        kiralikler = cursor.fetchall()
        for kiralik in kiralikler:
            print(kiralik)
    def Kiralık_Güncelle(self):
        try:
            cursor.execute("select * from kiralik")
            kiralikler = cursor.fetchall()
            for kiralik in kiralikler:
                print(kiralik)
            kiralik_id = int(input("Güncellemek istediğiniz kiralığın id'sini giriniz: "))
            kiralik = input("Kiralık Adı: ")
            fiyat = int(input("Fiyat: "))
            sure = int(input("Kiralama süresi/gün: "))
            cursor.execute("update kiralik set kiralik = ?,fiyat = ?,sure = ? where id = ?",(kiralik,fiyat,sure,kiralik_id))
            con.commit()
            print("Kiralık güncellendi")
        except:
            print("Hatalı giriş")
while True:
    menu.show_menu()
    choice = menu.getChoice()
    if choice == 1:
        ev = Ev_islem()
        ev.menu.show_menu()
        choice = ev.menu.getChoice()
        if choice == 1:
            ev.Ev_Ekle()
        elif choice == 2:
            ev.Ev_Sil()
        elif choice == 3:
            ev.Ev_Listele()
        elif choice == 4:
            ev.Ev_Guncelle()
    elif choice == 2:
        isletme = isletme_islem()
        isletme.menu.show_menu()
        choice = isletme.menu.getChoice()
        if choice == 1:
            isletme.İşletme_Ekle()
        elif choice == 2:
            isletme.İşletme_Sil()
        elif choice == 3:
            isletme.İşletme_Listele()
        elif choice == 4:
            isletme.İşletme_Güncelle()
    elif choice == 3:
        arsa = Arsa_islem()
        arsa.menu.show_menu()
        choice = arsa.menu.getChoice()
        if choice == 1:
            arsa.Arsa_Ekle()
        elif choice == 2:
            arsa.Arsa_Sil()
        elif choice == 3:
            arsa.Arsa_Listele()
        elif choice == 4:
            arsa.Arsa_Güncelle()
    elif choice == 4:
        kiralik = kiralik_islem()
        kiralik.menu.show_menu()
        choice = kiralik.menu.getChoice()
        if choice == 1:
            kiralik.Kiralık_Ekle()
        elif choice == 2:
            kiralik.Kiralık_Sil()
        elif choice == 3:
            kiralik.Kiralık_Listele()
        elif choice == 4:
            kiralik.Kiralık_Güncelle()
    else:
        break

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Emlak"
ws.append(["Ev","Fiyat","Adres","Metrekare"])
cursor.execute("select * from ev")
evler = cursor.fetchall()
for ev in evler:
    ws.append(ev)
ws.append([])
ws.append(["İşletme","Fiyat","Tip"])
cursor.execute("select * from isletme")
isletmeler = cursor.fetchall()
for isletme in isletmeler:
    ws.append(isletme)
ws.append([])
ws.append(["Arsa","Fiyat","Yer","Donum"])
cursor.execute("select * from arsa")
arsalar = cursor.fetchall()
for arsa in arsalar:
    ws.append(arsa)
ws.append([])
ws.append(["Kiralık","Fiyat","Süre"])
cursor.execute("select * from kiralik")
kiralikler = cursor.fetchall()
for kiralik in kiralikler:
    ws.append(kiralik)
wb.save("Emlak.xlsx")