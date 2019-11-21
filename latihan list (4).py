print ("====================================================================")
print ('|                                                                  |')
print ("|                           LATIHAN 4                              |")
print ('|                                                                  |')
print ("====================================================================")
print ('')
print (" \t ALYA SHAFIRA                                    ")
print (" \t 33119100010                                     ")
print (" \t TI.19.D.1                                       ")
print ('')

alya_list= [ 'april', 'mei', 2,4,9,9]
print (alya_list)
print ('')
#MENGAKSES LIST

print ("Akses List")
Data1 = alya_list[2]
Data2 = alya_list[1:5]
Data3 = alya_list[-2]
print(Data1)
print(Data2)
print(Data3)
print ('')

#MENGUBAH ELEMEN LIST
print("Ubah Element List")
print(alya_list)
alya_list[2] = 30
print(alya_list)
alya_list[3:5] = [1,10,6]
print(alya_list)
print ('')

#MENAMBAHKAN ELEMEN LIST
print("Menambahkan Elemen List")
print(alya_list)
x = alya_list
print(x)
y = x[1:-6]
print (y)
x.append(20)
y.extend([18,20,24])
print (x)
print (y)
print ('')

#MENGGABUNGKAN ELEMEN LIST
print( "Menggabungkan Elemen List")
z = x+y
x.extend(y)
print (z)
