def MenuUtama():
	print("Selamat Datang Di Warehouse Database")
	while (1):
		print("1. Daftar Produk")
		print("2. Tambah Produk")
		print("3. Update Produk")
		print("4. Hapus Produk")
		print("5. Sort Produk")
		print("6. Log Out")
		print("7. Exit")
		print("Masukkan Angka Menu:")
		n = int(input())
		if (n == 1):
			DaftarProduk()
		elif (n == 2):
			TambahProduk()
		elif (n == 3):
			UpdateProduk()
		elif (n == 4):
			HapusProduk()
		elif (n == 5):
			SortProduk()
		elif (n == 6):
			Log()
		elif (n == 7):
			exit()
		else:
			print("Pilihan yang diiput salah")

ListProduk = [["A001","Pengisi Nat",410,0,0],["A002","Pelapis",625,0,0],["A003","Bata Ringan",470,0,0],
	      ["A004","Plester",900,0,0],["A005","Acian",900,0,0]]
ListProdukBaru = []
def DaftarProduk():
	print("1. Tampilkan Semua Produk")
	print("2. Tampilkan Produk Berdasarkan Index")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	n = int(input())
	if (n == 1):
		print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
		for index,item in enumerate(ListProduk):
			print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')
		DaftarProduk()
	elif (n == 2):
		IndexProduk = int(input("Masukkan Index yang ingin ditampilkan :"))
		if 0<=IndexProduk<len(ListProduk):
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			DaftarProduk()
		else:
			print ("Data tidak ada")
			DaftarProduk()
	elif (n == 3):
		MenuUtama()
	else:
		print("Pilihan yang diiput salah")
		DaftarProduk()
	exit()

def TambahProduk():
	print("1. Tambah Produk")
	print("2. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		IndexProduk = int(input("Masukkan Index:"))
		if 0<=IndexProduk<len(ListProduk) :
			print("Data telah tersedia")
			TambahProduk()
		else :
			TambahKodeProduk = input("Masukkan Kode Produk:")
			TambahNamaProduk = input("Masukkan Nama Produk :")
			TambahStokAwal = int(input("Masukkan Stok Awal:"))
			TambahStokMasuk = int(input("Masukkan Stok Masuk:"))
			TambahStokKeluar = int(input("Masukkan Stok Keluar:"))
			ListProduk.append([TambahKodeProduk.capitalize(),TambahNamaProduk.capitalize(),TambahStokAwal,TambahStokMasuk,
		      					TambahStokKeluar])
			print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for index,item in enumerate(ListProduk):
				print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')
			Keputusan = input("Simpan Data?(ya/tidak)")
			if Keputusan == "ya":
				print("Data berhasil disimpan")
			else:
				ListProduk.pop()
			TambahProduk()
	elif (n == 2):
		MenuUtama()
	else:
		print("Pilihan yang diiput tidak ada")
		TambahProduk()

def UpdateProduk():
	print("1. Update Produk")
	print("2. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		IndexProduk = int(input("Masukkan Index:"))
		if 0<=IndexProduk<len(ListProduk) :
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			Keputusan = input("Lanjut update?(ya/tidak)")
			if Keputusan == "ya":
				Kolom = input("Pilih kolom yang akan diupdate:")
				if Kolom == "Kode Produk":
					Value1 = input("Masukkan data baru:")
					Keputusan2 = input("Update Data?(ya/tidak)")
					if Keputusan2 == "ya":
						ListProdukBaru[0][0] = Value1
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Nama Produk":
					Value2 = input("Masukkan data baru:")
					Keputusan3 = input("Update Data?(ya/tidak)")
					if Keputusan3 == "ya":
						ListProdukBaru[0][1] = Value2
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Awal":
					Value3 = int(input("Masukkan data baru:"))
					Keputusan4 = input("Update Data?(ya/tidak)")
					if Keputusan4 == "ya":
						ListProdukBaru[0][2] = Value3
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Masuk":
					Value4 = int(input("Masukkan data baru:"))
					Keputusan5 = input("Update Data?(ya/tidak)")
					if Keputusan5 == "ya":
						ListProdukBaru[0][3] = Value4
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Keluar":
					Value5 = int(input("Masukkan data baru:"))
					Keputusan6 = input("Update Data?(ya/tidak)")
					if Keputusan6 == "ya":
						ListProdukBaru[0][4] = Value5
						print("Data Berhasil Diupdate")
					else:
						pass
				else:
					pass
				UpdateProduk()
			else:
				UpdateProduk()
			UpdateProduk()
		else :
			print("Data yang dicari tidak ada")
			UpdateProduk()
	elif (n == 2):
		MenuUtama()
	else:
		print("Pilihan yang diiput tidak ada")
		HapusProduk()

def HapusProduk():
	print("1. Hapus Produk")
	print("2. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		IndexProduk = int(input("Masukkan Index:"))
		if 0<=IndexProduk<len(ListProduk) :
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			Keputusan = input("Hapus update?(ya/tidak)")
			if Keputusan == "ya":
				ListProdukBaru.clear()
				ListProduk.pop(IndexProduk)
				print("Data Berhasil dihapus")
				HapusProduk()
			else:
				HapusProduk()
			HapusProduk()
		else :
			print("Data yang dicari tidak ada")
			HapusProduk()
	elif (n == 2):
		MenuUtama()
	else:
		print("Pilihan yang diiput tidak ada")
		HapusProduk()

def SortProduk():
	print("1. Sort Produk Naik")
	print("2. Sort Produk Turun")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		ListProduk.sort()
		print("Data berhasil disortir")
		SortProduk()
	elif (n == 2):
		ListProduk.reverse()
		print("Data berhasil disortir")
		SortProduk()
	elif (n == 3):
		MenuUtama()
	else:
		print("Pilihan yang diiput tidak ada")
		SortProduk()

def MenuUtama2():
	print("Selamat Datang Di Warehouse Database")
	while (1):
		print("1. Daftar Produk")
		print("2. Tambah Produk")
		print("3. Update Produk")
		print("4. Sort Produk")
		print("5. Log Out")
		print("6. Exit")
		print("Masukkan Angka Menu:")
		n = int(input())
		if (n == 1):
			DaftarProduk2()
		elif (n == 2):
			TambahProduk2()
		elif (n == 3):
			UpdateProduk2()
		elif (n == 4):
			SortProduk2()
		elif (n == 5):
			Log()
		elif (n == 6):
			exit()
		else:
			print("Pilihan yang diiput salah")

def DaftarProduk2():
	print("1. Tampilkan Semua Produk")
	print("2. Tampilkan Produk Berdasarkan Index")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	n = int(input())
	if (n == 1):
		print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
		for index,item in enumerate(ListProduk):
			print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')
		DaftarProduk2()
	elif (n == 2):
		IndexProduk = int(input("Masukkan Index yang ingin ditampilkan :"))
		if 0<=IndexProduk<len(ListProduk):
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			DaftarProduk2()
		else:
			print ("Data tidak ada")
			DaftarProduk2()
	elif (n == 3):
		MenuUtama2()
	else:
		print("Pilihan yang diiput salah")
		DaftarProduk2()
	exit()

def TambahProduk2():
	print("1. Tambah Produk")
	print("2. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		IndexProduk = int(input("Masukkan Index:"))
		if 0<=IndexProduk<len(ListProduk) :
			print("Data telah tersedia")
			TambahProduk2()
		else :
			TambahKodeProduk = input("Masukkan Kode Produk:")
			TambahNamaProduk = input("Masukkan Nama Produk :")
			TambahStokAwal = int(input("Masukkan Stok Awal:"))
			TambahStokMasuk = int(input("Masukkan Stok Masuk:"))
			TambahStokKeluar = int(input("Masukkan Stok Keluar:"))
			ListProduk.append([TambahKodeProduk.capitalize(),TambahNamaProduk.capitalize(),TambahStokAwal,TambahStokMasuk,
		      					TambahStokKeluar])
			print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for index,item in enumerate(ListProduk):
				print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')
			Keputusan = input("Simpan Data?(ya/tidak)")
			if Keputusan == "ya":
				print("Data berhasil disimpan")
			else:
				ListProduk.pop()
			TambahProduk2()
	elif (n == 2):
		MenuUtama2()
	else:
		print("Pilihan yang diiput tidak ada")
		TambahProduk2()

def UpdateProduk2():
	print("1. Update Produk")
	print("2. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		IndexProduk = int(input("Masukkan Index:"))
		if 0<=IndexProduk<len(ListProduk) :
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			Keputusan = input("Lanjut update?(ya/tidak)")
			if Keputusan == "ya":
				Kolom = input("Pilih kolom yang akan diupdate:")
				if Kolom == "Kode Produk":
					Value1 = input("Masukkan data baru:")
					Keputusan2 = input("Update Data?(ya/tidak)")
					if Keputusan2 == "ya":
						ListProdukBaru[0][0] = Value1
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Nama Produk":
					Value2 = input("Masukkan data baru:")
					Keputusan3 = input("Update Data?(ya/tidak)")
					if Keputusan3 == "ya":
						ListProdukBaru[0][1] = Value2
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Awal":
					Value3 = int(input("Masukkan data baru:"))
					Keputusan4 = input("Update Data?(ya/tidak)")
					if Keputusan4 == "ya":
						ListProdukBaru[0][2] = Value3
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Masuk":
					Value4 = int(input("Masukkan data baru:"))
					Keputusan5 = input("Update Data?(ya/tidak)")
					if Keputusan5 == "ya":
						ListProdukBaru[0][3] = Value4
						print("Data Berhasil Diupdate")
					else:
						pass
				elif Kolom == "Stok Keluar":
					Value5 = int(input("Masukkan data baru:"))
					Keputusan6 = input("Update Data?(ya/tidak)")
					if Keputusan6 == "ya":
						ListProdukBaru[0][4] = Value5
						print("Data Berhasil Diupdate")
					else:
						pass
				else:
					pass
				UpdateProduk2()
			else:
				UpdateProduk2()
			UpdateProduk2()
		else :
			print("Data yang dicari tidak ada")
			UpdateProduk2()
	elif (n == 2):
		MenuUtama2()
	else:
		print("Pilihan yang diiput tidak ada")

def SortProduk2():
	print("1. Sort Produk Naik")
	print("2. Sort Produk Turun")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		ListProduk.sort()
		print("Data berhasil disortir")
		SortProduk2()
	elif (n == 2):
		ListProduk.reverse()
		print("Data berhasil disortir")
		SortProduk2()
	elif (n == 3):
		MenuUtama2()
	else:
		print("Pilihan yang diiput tidak ada")
		SortProduk2()

def MenuUtama3():
	print("Selamat Datang Di Warehouse Database")
	while (1):
		print("1. Daftar Produk")
		print("2. Sort Produk")
		print("3. Log Out")
		print("4. Exit")
		print("Masukkan Angka Menu:")
		n = int(input())
		if (n == 1):
			DaftarProduk3()
		elif (n == 2):
			SortProduk3()
		elif (n == 3):
			Log()
		elif (n == 4):
			exit()
		else:
			print("Pilihan yang diiput salah")

def DaftarProduk3():
	print("1. Tampilkan Semua Produk")
	print("2. Tampilkan Produk Berdasarkan Index")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	n = int(input())
	if (n == 1):
		print("Index | Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
		for index,item in enumerate(ListProduk):
			print(f'{index}     | {item[0]}        | {item[1]}         | {item[2]}     | {item[3]}          | {item[4]}')
		DaftarProduk3()
	elif (n == 2):
		IndexProduk = int(input("Masukkan Index yang ingin ditampilkan :"))
		if 0<=IndexProduk<len(ListProduk):
			ListProdukBaru.clear()
			ListProdukBaru.append(ListProduk[IndexProduk])
			print("Kode Produk | Nama Produk | Stok Awal | Stok Masuk | Stok Keluar")
			for item in ListProdukBaru:
				print(f'{item[0]}        | {item[1]}       | {item[2]}       | {item[3]}          | {item[4]}')
			DaftarProduk3()
		else:
			print ("Data tidak ada")
			DaftarProduk3()
	elif (n == 3):
		MenuUtama3()
	else:
		print("Pilihan yang diiput salah")
		DaftarProduk3()
	exit()

def SortProduk3():
	print("1. Sort Produk Naik")
	print("2. Sort Produk Turun")
	print("3. Kembali ke Menu Utama")
	print("Masukkan Angka Menu:")
	
	n = int(input())
	if (n == 1):
		ListProduk.sort()
		print("Data berhasil disortir")
		SortProduk3()
	elif (n == 2):
		ListProduk.reverse()
		print("Data berhasil disortir")
		SortProduk3()
	elif (n == 3):
		MenuUtama3()
	else:
		print("Pilihan yang diiput tidak ada")
		SortProduk3()

def Log():
	print("Pilih Salah Satu di bawah ini:")
	print("1. Manajer")
	print("2. Supervisor")
	print("3. Admin")
	print("4. Operator")
	print("5. Exit")
	n = int(input())
	if (n == 1):
		MenuUtama()
	elif (n == 2):
		MenuUtama2()
	elif (n == 3):
		MenuUtama2()
	elif (n == 4):
		MenuUtama3()
	elif (n == 5):
		exit()
	else:
		print("Pilihan Salah")
		Log()

Log()