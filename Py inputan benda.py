#Membuat Inputan Bertema Benda
print ('             *****************            ')
print ('      *******************************     ')
print ('******************************************')

print ('\nMASUKKAN SESUAI PERMINTAAN')
print ('**************************\n')

nama    =       input ('Nama barang : ')
jumlah  = int  (input ('Jumlah      : '))
panjang = int  (input ('Panjang(m)  : '))
berat   = float(input ('Berat(kg)   : '))
harga   = float(input ('Harga       : '))

print ('\nMENENTUKAN TIPE DATA')
print ('********************\n')

print ('Nama        : ', nama)
print ('Tipe data   : ', type (nama))
print ('Jumlah      : ', jumlah)
print ('Tipe data   : ', type (jumlah))
print ('Panjang     : ', panjang ,'m')
print ('Tipe data   : ', type (panjang))
print ('Berat       : ', berat , 'kg')
print ('Tipe data   : ', type (berat))
print ('Harga       : ', harga)
print ('Tipe data   : ', type (harga))

print ('\nMEMASUKKAN HASIL INPUT KE LIST')
print ('******************************\n')

hasil = [nama, jumlah, panjang, berat, harga]
print ('List inputan data diatas ', hasil, '\n')

print ('******************************************')
print ('      *******************************     ')
print ('             *****************            ')
