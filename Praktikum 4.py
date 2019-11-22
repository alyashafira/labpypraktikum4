#PROGRAM MENAMBAHKAN DATA DAN MENENTUKAN NILAI AKHIR MAHASISWA


NML =[]
NIML =[]
NTL =[]
NUTSL =[]
NUASL =[]
NAML=[]
print(" PROGRAM MENAMBAHKAN DATA DAN MENENTUKAN NILAI AKHIR MAHASISWA ")
print("")
jawab ="y"
while jawab == "y" :
    
    NM=input("Nama Mahasiswa :")
    NIM=input("NIM :")
    NTUGAS=float(input("Nilai Tugas:"))
    NUTS=float(input("Nilai UTS:"))
    NUAS=float(input("Nilai UAS:"))
    nilai=float(NTUGAS)*30/100 + (NUTS)*35/100 + (NUAS)*35/100
    print("")


    NML.append(NM)
    NIML.append(NIM)
    NTL.append(NTUGAS)
    NUTSL.append(NUTS)
    NUASL.append(NUAS)
    NAML.append(nilai)

    lagi = input("Tambah Data [y/t]? :")
    print("")
    if lagi =="t":
        break

    
print ("                           DAFTAR MAHASISWA                           ")
print ("=======================================================================")
print ("|NO  |  Nama  |   NIM   |  Tugas   |   UTS   |   UAS   |  Akhir  |")
print ("=======================================================================")

for n in range (len(NML)):
    print(' ',n+1,   ' |  ',NML[n],  '| ',NIML[n],' | ',NTL[n],' | ',NUTSL[n],' |  ',NUASL[n],' | ',NAML[n],' |' )
print ("")
print ("=======================================================================")
    
    



