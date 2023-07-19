# Project_Capstone_1
Project ini menggunakan topik tentang stok barang gudang

Ketika coding dijalankan, user memilih perannya sesuai dengan pilihan yang tersedia

Tiap user memiliki menu utama yang berbeda-beda

Manajer memiliki full menu utama

Supervisor & Admin juga full menu utama tanpa ada menu "Hapus Produk"

Operator hanya dapat melihat daftar produk & sortir produk saja

Coding menggunakan perintah regular function yang telah dibuat

Sama juga dengan menu utama Daftar Produk, Tambah Produk, Update Produk, Hapus Produk, & Sort Produk menggunakan regular function

Ada juga Pilihan menu "Log Out" untuk keluar dari program tanpa harus menghentikan program

Untuk menampilkan semua Produk:

print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")

for index,item in enumerate(ListProduk):
  
  print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')

Untuk menampilkan Produk berdasarkan index:

ListProdukBaru.clear()

ListProdukBaru.append(ListProduk[IndexProduk])

Kalau tidak ada perintah "clear()", Data pada ListProdukBaru akan menumpuk

Tambah Produk:

ListProduk.append([TambahKodeProduk.capitalize(),TambahNamaProduk.capitalize(),TambahStokAwal,TambahStokMasuk,
							    TambahStokKeluar])

Update Produk:

ListProdukBaru[List ke berapa][item ke berapa] = Value1

ListProduk juga ikut terupdate

Hapus Produk:

ListProduk.pop(IndexProduk)

Sort Produk naik:

ListProduk.sort()

Sort Produk turun:

ListProduk.reversed()
            
