#MENGKONVERSI SUHU DARI CELSIUS

#Judul
print ('*'*40)
print ('   PROGRAM KONVERSI SUHU DARI CELSIUS')
print ('*'*40 , '\n')

#Input Suhu Celsius
celsius = float (input('Masukkan suhu dalam derajat celsius : '))
print ('Celsius                             : %f' %celsius ,'°C')

#Cara Konversi
print ('\n HASIL KONVERSI SUHU \n')
kon_F = celsius * 9/5  + 32 
kon_R = celsius * 4/5 
kon_K = celsius + 273

#Hasil Konversi
print ('Fahrenheit : %f' %kon_F , '°F')
print ('Reamur     : %f' %kon_R , '°R')
print ('Kelvin     : %f' %kon_K , 'K')
