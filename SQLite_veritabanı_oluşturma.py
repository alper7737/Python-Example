#SQLite kütüphanesi python ile birlikte geliyor herhangi #bir yükleme yapmanıza gerek yok.

#Bu kısımda kütüphanemizi çekiyoruz ve kısaltmak için  #‘sql’ tag’i #kullanıyoruz.
import sqlite3 as sql   
 
#Burada bir tanımlayıcı açıp oluşturmk istediğimiz kütphane adımızı #uzantısını yazıyoruz ve bağlanıyoruz.
veriad= sql.connect('kisiler.sqlite') 

#Veritabanını kontrol(verileri değiştirebilmek) edebilmemiz için ‘cursor’ adındaki tanımlayıcımızı kullanıyoruz.
imlec = veriad.cursor()

#imlec adındaki tanımlayıcımızı veritabanında değişiklik yapabilmek için çekiyoruz ve sql kodlarını girip ekleme yapıyoruz.
imlec.execute("CREATE TABLE kisi_bilgisi (adi,soyadi,telefon)")
kisi_girisi = "INSERT INTO kisi_bilgisi VALUES ('Alper','Coşar','05307035076')"

#Değişikliğimizi gerçekleştirebilmemiz için ‘execute’ kodunu kullanıyoruz.
imlec.execute(kisi_girisi)

#bağlantımızı gerçekleştirmek için ‘commit’ kodunu kullanıyoruz.
veriad.commit()

