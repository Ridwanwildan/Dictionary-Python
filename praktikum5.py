data = {
    "nim":[],
    "nama":[],
    "uts":[],
    "uas":[],
    "tugas":[]
}

while True:
 menu = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]:")
 # menu tambah data
 if menu == "t" or menu == "T":
     print("\nTambah Data")
     data["nim"].append(input("NIM         :"))
     data["nama"].append(input("Nama        :"))
     data["uts"].append(int(input("Nilai UTS   :")))
     data["uas"].append(int(input("Nilai UAS   :")))
     data["tugas"].append(int(input("Nilai Tugas :")))

 # menu lihat data
 elif menu == "l" or menu == "L":
     print("Daftar Nilai")
     print("==========================================================================")
     print("| No  |          Nama           |    NIM    | TUGAS | UTS | UAS |  AKHIR |")
     print("==========================================================================")
     if len(data["nama"]) != 0:
         for i in range(len(data["nama"])):
             print("|", i+1, "  |", end="")
             print('{0:<25}'.format(data["nama"][i]), end="")
             print("|", data["nim"][i], end="")
             print(" |", data["tugas"][i], end="")
             print("    |", data["uts"][i], end="")
             print("  |", data["uas"][i], " | ", end="")
             print(f'{(data["tugas"][i]*30/100) + (data["uts"][i]*35/100) + (data["uas"][i]*35/100) :.2f}', " |")
     else:
         print("                         TIDAK ADA DATA                               ")      
     print("==========================================================================")

 # menu ubah data
 elif menu == "u" or menu == "U":
     if len(data["nama"]) != 0:
         print("Ubah Data")
         ubah = int(input("Data nomor berapa yang mau diubah ? "))
         if len(data["nama"]) >= ubah:
             print("\nData ke -",ubah)
             print("\nNIM sebelumnya :", data["nim"][ubah-1])
             data["nim"][ubah-1] = input("Masukkan NIM yang baru : ")            
             print("\nNama sebelumnya :", data["nama"][ubah-1])
             data["nama"][ubah-1] = input("Masukkan Nama yang baru : ")
             print("\nNilai tugas sebelumnya :", data["tugas"][ubah-1])
             data["tugas"][ubah-1] = int(input("Masukkan Nilai tugas yang baru : "))
             print("\nNilai UTS sebelumnya :", data["uts"][ubah-1])
             data["uts"][ubah-1] = int(input("Masukkan Nilai UTS yang baru : "))
             print("\nNilai UAS sebelumnya :", data["uas"][ubah-1])
             data["uts"][ubah-1] = int(input("Masukkan Nilai UAS yang baru : "))
         else:
             print("Data ke -", ubah, "tidak ada")
     else:
         print("\nTidak ada data yang bisa diubah")

 # menu hapus data
 elif menu == "h" or menu == "H":
     if len(data["nama"]) != 0:
         print("\nHapus Data")
         hapus = int(input("Data nomor berapa yang mau dihapus ? "))
         if len(data["nama"]) >= hapus:
             del data["nim"][hapus-1]
             del data["nama"][hapus-1]
             del data["tugas"][hapus-1]
             del data["uts"][hapus-1]
             del data["uas"][hapus-1]
             print("Data ke -", hapus, "berhasil dihapus")
         else:
             print("Data ke -", hapus, "tidak ada")
     else:
         print("\nTidak ada data yang bisa dihapus")

 # menu cari data
 elif menu == "c" or menu == "C":
     print("\nCari Data")
     cari = (input("Masukkan NIM atau Nama : "))
     a = cari in data["nim"]
     b = cari in data["nama"]
     if a == True or b == True:
         print(cari, "Ada didalam data")
     else:
         print(cari, "Tidak ada didalam data")

 # menu keluar
 elif menu == "k" or menu == "K":
     print("\nAnda telah keluar")
     print("Terimakasih")
     break

 # menu salah ketik
 else:
     print("\nMaaf perintah yang diketik salah")
     print("Ketik L : Untuk melihat data")
     print("Ketik T : Untuk menambahkan data")
     print("Ketik U : Untuk mengubah data")
     print("Ketik H : Untuk menghapus data")
     print("Ketik C : Untuk mencari data")
     print("Ketik K : Untuk keluar")