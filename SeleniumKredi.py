from selenium import webdriver
import time
browser= webdriver.Chrome()

url ="https://www.imubank.com"

browser.get(url) #the site link

time.sleep(10)
#--------------------------------Ekran 1--------------------------------------


tutar1 = browser.find_element_by_name("tutar1")
#vade1 = browser.find_element_by_name("vade1")

tutar1.send_keys("475")
basvur1 = browser.find_element_by_xpath("")
basvur1.click()
# 1. Hata Mesajı
time.sleep(5)

tutar1.send_keys("1000001")
basvur1 = browser.find_element_by_xpath("")
basvur1.click()
# 2. Hata Mesajı
time.sleep(5)


tutar2 = browser.find_element_by_name("tutar2")
#vade2 = browser.find_element_by_name("vade2")

tutar2.send_keys("475")
basvur2 = browser.find_element_by_xpath("")
basvur2.click()
# 1. Hata Mesajı
time.sleep(5)

tutar2.send_keys("1000001")
basvur2 = browser.find_element_by_xpath("")
basvur2.click()
# 2. Hata Mesajı
time.sleep(5)


tutar3 = browser.find_element_by_name("tutar3")
#vade3 = browser.find_element_by_name("vade3")

tutar3.send_keys("475")
basvur3 = browser.find_element_by_xpath("")
basvur3.click()
# 1. Hata Mesajı
time.sleep(5)

tutar3.send_keys("1000001")
basvur3 = browser.find_element_by_xpath("")
basvur3.click()
# 2. Hata Mesajı
time.sleep(5)

# Hatasız Devam
tutar3.send_keys("55555")
basvur3 = browser.find_element_by_xpath("")
basvur3.click()

time.sleep(5)

#--------------------------------Ekran 2--------------------------------------

#tchatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("987654321012")
ad.send_keys("Ali")
soyad.send_keys("Candan")
eposta.send_keys("acandan@outlook.com")
telno.send_keys("5551552535")
tutarb.send_keys("555")
gelirb.send_keys("5")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#ad hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432101")
ad.send_keys("55555")
soyad.send_keys("Karahanli")
eposta.send_keys("karahnli@gmail.com")
telno.send_keys("5551552535")
tutarb.send_keys("555")
gelirb.send_keys("5")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#soyad hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432102")
ad.send_keys("Polat")
soyad.send_keys("55555")
eposta.send_keys("cimbom_polat@hotmail.com")
telno.send_keys("5551552535")
tutarb.send_keys("555")
gelirb.send_keys("5")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#eposta hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432104")
ad.send_keys("Eysan")
soyad.send_keys("Tezcan")
eposta.send_keys("teyzcanhotmail")
telno.send_keys("5551552535")
tutarb.send_keys("555")
gelirb.send_keys("5")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#telno hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432105")
ad.send_keys("Ali")
soyad.send_keys("Kirgiz")
eposta.send_keys("kerpeten@gmail.com")
telno.send_keys("02125552552")
tutarb.send_keys("555")
gelirb.send_keys("5")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#tutar bilgisi hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432109")
ad.send_keys("Poyraz")
soyad.send_keys("Karayel")
eposta.send_keys("paragel34@gmail.com")
telno.send_keys("5551552535")
tutarb.send_keys("55")
gelirb.send_keys("7")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

#gelir bilgisi hatası
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432121")
ad.send_keys("Mecnun")
soyad.send_keys("Cinar")
eposta.send_keys("leyla@hotmail.com")
telno.send_keys("5551552535")
tutarb.send_keys("656")
gelirb.send_keys("0")

#fotograf islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(3)

# Hatasız Devam
tcno = browser.find_element_by_name("tcno")
ad = browser.find_element_by_name("ad")
soyad = browser.find_element_by_name("soyad")
eposta = browser.find_element_by_name("eposta")
telno = browser.find_element_by_name("telno")
tutarb = browser.find_element_by_name("tutarb")
gelirb = browser.find_element_by_name("gelirb")

tcno.send_keys("98765432141")
ad.send_keys("kemal")
soyad.send_keys("hacioglu")
eposta.send_keys("akhaciog@gmail.com")
telno.send_keys("5572526128")
tutarb.send_keys("7755")
gelirb.send_keys("100")

#fotograf yükleme islemi
dg = browser.find_element_by_xpath("")
dg.click()
#...
ktype = browser.find_element_by_xpath("")
ktype.click()
#...
meslek = browser.find_element_by_xpath("")
meslek.click()
#...
kvkk = browser.find_element_by_xpath("")
kvkk.click()
kaydet = browser.find_element_by_xpath("")
kaydet.click()

time.sleep(5)

#--------------------------------Ekran 3--------------------------------------

bekle = browser.find_element_by_xpath("")
bekle.click()
#Belge Hatası


ktype = browser.find_element_by_xpath("")
ktype.click()
#...kredi tipi seçme

#belge yükleme islemi

btype = browser.find_element_by_xpath("")
btype.click()
#...belge tipi seçme


browser.close()