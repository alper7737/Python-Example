import sqlite3 as sql

veriad= sql.connect('kisiler.sqlite')

imlec = veriad.cursor()
imlec.execute("CREATE TABLE kisi_bilgisi (adi,soyadi,telefon)")
kisi_girisi = "INSERT INTO kisi_bilgisi VALUES ('Alper','Coşar','05307035076')"
imlec.execute(kisi_girisi)
veriad.commit()