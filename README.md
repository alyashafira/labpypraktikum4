
# labpypraktikum4 :octocat:
**Nama  : Alya Shafira**

**Nim   : 311910010**

**Kelas : TI.19.D.1**

*Tugas Bahasa Pemrograman*

*Tugas Praktikum 4*

*LATIHAN 4*

*PRAKTIKUM 4*

# LATIHAN 4
 ![Capture1](https://user-images.githubusercontent.com/56963083/69342052-509bad80-0c9d-11ea-9359-feae559acf72.PNG)
 
 ** HASIL DARI LATIHAN 4 **


# PRAKTIKUM 4

** Code Program **
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
     


# ALUR ALGORITMA Praktikum 4

      A. Input
     Buat lah sebuah list terlebih dahulu
     NML =[]             { Keterangan List untuk Nama Mahasiswa }
     NIML =[]            { Keterangan List untuk NIM }
     NTL =[]             { Keterangan List untuk Nilai Tugas}
     NUTSL =[]           { Keterangan List untuk Nilai UTS }
     NUASL =[]           { Keterangan List untuk Nilai UAS }
     NAML=[]             { Keterangan List untuk Nilai Akhir Mahasiswa }
     print("PROGRAM MENAMBAHKAN DATA DAN MENENTUKAN NILAI AKHIR MAHASISWA")
        >>> Berfungsi untuk mencetak teks "PROGRAM MENAMBAHKAN DATA DAN MENENTUKAN NILAI AKHIR MAHASISWA") 
 
      B. Proses
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
           
           ## "while"  	: disebut uncounted loop (perulangan yang tak terhitung),
           ## "float()" : berfungsi mengubah bilangan menjadi float. dan berfungsi mengkonversi bilangan maupun string angka menjadi                               bilangan bulat (integer).
           ## "append()": berfungsi untuk menambahkan nilai baru
           
      C. Output
      lagi = input("Tambah Data [y/t]? :")       { Pernyataan tambah data [y/t]
              print("")
              if lagi =="t":
              break
              
              ## " if "  : "if disini digunakan untuk menyatakan suatu kondisi jika ingin menambahkan data lagi dijawab tidak "t", maka                             ia akan berhenti. "
              ## "break" : "break adalah pernyataan untuk berhenti."
              
              for n in range (len(NML)):
              print(' ',n+1,   ' |  ',NML[n],  '| ',NIML[n],' | ',NTL[n],' | ',NUTSL[n],' |  ',NUASL[n],' | ',NAML[n],' |' )
              
              ## for n in range (len(NML)):
                >>> digunakan untuk menambahkan data pada list dan juga untuk menentukan nilai akhir dari operasi hitung yang telah di                       input yang dimasukan kedalam tabel.
                
                
                
                ** HASIL DARI PRAKTIKUM 4 **
                
                
                
      

