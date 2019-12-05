#SQLite ve sistem kütüphanemizi çekiyoruz.
import os
import sqlite3 as sql

#Veritabanı dosyamızın ismimizi tanımlayıcıya ekliyoruz.
veriad='kisiler.sqlite'
#Veritabanı dosyamızı sistemde aratıyoruz.
dosya_mevcut=os.path.exists(veriad)
#Bulduğumuz veritabanı dosyamıza bağlanıyoruz.
vt=sql.connect(veriad)
imlec=vt.cursor()
#Veritabanımızısilmek için gerekli olan SQL kodlarımızı giriyoruz.
imlec.execute("DELETE FROM kisi_bilgisi WHERE telefon='05307035076'")
vt.commit()
#Veritabanımızı seçiyoruz.
imlec.execute("SELECT * FROM kisi_bilgisi")
#Fetchall (hepsini al) komutunu kullanarak bütün verileri çekiyoruz ve #veritabanına yazdğımız kodları entegre ediyoruz.
kisiler=imlec.fetchall()
print(kisiler)
