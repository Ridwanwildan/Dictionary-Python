kontak = {
    "nama":["Ari", "Dina"], 
    "no":["081267888", "087677776"]
    }

# Tampilkan kontaknya Ari
print(kontak["nama"][0])
print(kontak["no"][0])

# Tambah kontak baru dengan nama Riko, nomor 087654544
kontak["nama"].append("Riko")
kontak["no"].append("087654544")

# Ubah kontak Dina dengan nomor baru 088999776
kontak["no"][1] = "088999776"

# Tampilkan semua Nama
print(kontak["nama"])

# Tampilkan semua Nomor
print(kontak["no"])

# Tampilkan daftar Nama dan nomornya
print(kontak)

# Hapus kontak Dina
kontak["nama"].remove("Dina")
kontak["no"].remove("088999776")
