import sqlite3 as sql
from ui import UI
con = sql.connect("mydb.db")
cursor = con.cursor()
menu = UI(["Kitap_Ekle","Kitap_Ara","Kitap_Sil","Kitap_Listele"])
def Kitap_Ekle():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplar (kitap_adi TEXT, yazar_adi TEXT, yayin_evi TEXT, sayfa_sayisi INT)")
    ad = input("Kitap adı:")
    yazar = input("Yazar adı:")
    yayin = input("Yayınevi:")
    sayfa = int(input("Sayfa sayısı:"))
    cursor.execute("INSERT INTO kitaplar VALUES(?,?,?,?)",(ad,yazar,yayin,sayfa))
    con.commit()
def Kitap_Ara():
    ad = input("Kitap adı:")
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_adi = ?",(ad,))
    for i in cursor.fetchall():
        print(i)
def Kitap_Sil():
    ad = input("Silinecek kitabın adı:")
    cursor.execute("DELETE FROM kitaplar WHERE kitap_adi = ?",(ad,))
    con.commit()
def Kitap_Listele():
    cursor.execute("SELECT * FROM kitaplar")
    for i in cursor.fetchall():
        print(i)

def odunc_al():
    ad = input("Kitap adı:")
    yazar = input("Yazar adı:")
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_adi = ? AND yazar_adi = ?",(ad,yazar))
    for i in cursor.fetchall():
        print(i)
    odunc = input("Kitabı ödünç alacak kişinin adı:")
    cursor.execute("INSERT INTO odunc VALUES(?,?,?)",(ad,yazar,odunc))
    con.commit()

def odunc_ver():
    ad = input("Kitap adı:")
    yazar = input("Yazar adı:")
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_adi = ? AND yazar_adi = ?",(ad,yazar))
    for i in cursor.fetchall():
        print(i)
    odunc = input("Kitabı ödünç veren kişinin adı:")
    cursor.execute("DELETE FROM odunc WHERE kitap_adi = ? AND yazar_adi = ?",(ad,yazar))
    con.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS odunc (kitap_adi TEXT, yazar_adi TEXT, odunc_alan TEXT)")

while True:
    secim = input("Seçiminizi yapınız:")
    if secim == "1":
        menu.show_menu()
        Kitap_Ekle()
    elif secim == "2":
        menu.show_menu()
        Kitap_Ara()
    elif secim == "3":
        menu.show_menu()
        Kitap_Sil()
    elif secim == "4":
        menu.show_menu()
        Kitap_Listele()
    elif secim == "5":
        menu.show_menu()
        x = input("ödünç al/ver")
        if x == "ödünç al":
            odunc_al()
        elif x == "ödünç ver":
            odunc_ver()
    else:
        break