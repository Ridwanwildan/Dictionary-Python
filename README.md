# Latihan membuat dictionary python  

* Nama          : Hizbullah Ridwan
* NIM           : 312110055
* Kelas         : TI.21.C.1
* Mata Kuliah   : Bahasa Pemrograman
----------------------------------
Dalam latihan membuat conditional dan loop [python](https://www.python.org/) ini, saya menggunakan [visual studio code](https://code.visualstudio.com/) sebagai teks editornya.     
    

* [Latihan](https://github.com/Ridwanwildan/Dictionary-Python#latihan)         
* [Tugas](https://github.com/Ridwanwildan/Dictionary-Python#tugas)        


## Latihan         

Mendeklarasikan dictionary yang didalamnya ada ***nama***, ***no*** sebagai key dan ***values*** nya yaitu ***ari***, ***Dina***, ***081267888***, ***087677776*** yang kita masukkan kedalam list.       

```bash
kontak = {
    "nama":["Ari", "Dina"], 
    "no":["081267888", "087677776"]
    }
```         

Untuk menampilkan kontak Ari maka caranya seperti ini :         
```bash
# Tampilkan kontaknya Ari
print(kontak["nama"][0])
print(kontak["no"][0])
```        

Kita bisa menambahkan values yang baru dengan cara seperti ini :       
```bash
# Tambah kontak baru dengan nama Riko, nomor 087654544
kontak["nama"].append("Riko")
kontak["no"].append("087654544")
```         

Untuk mengubah values maka caranya seperti ini :       
```bash
# Ubah kontak Dina dengan nomor baru 088999776
kontak["no"][1] = "088999776"
```        

Jika ingin menampilkan masing-masing values yang sudah kita masukkan maka caranya seperti ini :       
```bash
# Tampilkan semua Nama
print(kontak["nama"])
# Tampilkan semua Nomor
print(kontak["no"])
```        

Dan kalau mau menampilkan key beserta values gunakan cara ini :      
```bash
# Tampilkan daftar Nama dan nomornya
print(kontak)
```         

Terakhir yaitu jika kita ingin menghapus values nya gunakan cara ini :      
```bash
# Hapus kontak Dina
kontak["nama"].remove("Dina")
kontak["no"].remove("088999776")
```               

