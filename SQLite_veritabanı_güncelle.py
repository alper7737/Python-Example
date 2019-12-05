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
#Veritabanımızı güncellemek için gerekli olan SQL kodlarımızı giriyoruz.
imlec.execute("UPDATE kisi_bilgisi SET adi='Haydar' WHERE adi='Alper'")
vt.commit()
#Veritabanımızı seçiyoruz.
imlec.execute("SELECT * FROM kisi_bilgisi")
kisiler=imlec.fetchall()
print(kisiler)
