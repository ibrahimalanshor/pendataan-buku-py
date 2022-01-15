# Import
import sqlite3

# Connect DB 
conn = sqlite3.connect('./perpustakaan.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Fungsi

# Tampil Semua Buku
def tampilBuku():
  print("====================== Data Buku =======================")

  cursor.execute("SELECT * FROM buku")
  
  data_buku = cursor.fetchall()

  if len(data_buku) < 1:
    print("Data buku kosong")
  else:
    print("| ID | Judul | Penulis | Penerbit | Tahun |")
    for buku in data_buku:
      print("| {id} | {judul} | {penulis} | {penerbit} | {tahun} |".format(**buku))

# Tambah Buku
def tambahBuku():
  print("===================== Tambah Buku ======================")
  judul = input("Masukkan judul buku = ")
  penulis = input("Masukkan penulis buku = ")
  penerbit = input("Masukkan penerbit buku = ")
  tahun = input("Masukkan tahun buku = ")

  if (judul and penulis and penerbit and tahun):
    buku = (judul, penulis, penerbit, tahun)

    cursor.execute("INSERT INTO buku(judul, penulis, penerbit, tahun) VALUES(?,?,?,?)", buku)
    conn.commit()

    print("========================================================")
    print("Buku Berhasil Ditambahkan")
  else:
    print("Input tidak sesuai")

# Lihat Buku
def lihatBuku():
  print("===================== Lihat Buku =======================")
  id_buku = input("Masukkan id buku = ")

  cursor.execute("SELECT * FROM buku WHERE id = ?", id_buku)
  
  buku = cursor.fetchone()

  print("========================================================")
  if buku:
    print("| ID | Judul | Penulis | Penerbit | Tahun |")
    print("| {id} | {judul} | {penulis} | {penerbit} | {tahun} |".format(**buku))
  else:
    print("Buku Tidak Ditemukan")

# Edit Buku
def editBuku():
  print("====================== Edit Buku =======================")
  id_buku = input("Masukkan id buku = ")

  cursor.execute("SELECT COUNT(*) as total FROM buku WHERE id = ?", id_buku)
  
  data_buku = cursor.fetchone()
  total = data_buku['total']

  print("========================================================")
  if total > 0:
    judul = input("Masukkan judul buku = ")
    penulis = input("Masukkan penulis buku = ")
    penerbit = input("Masukkan penerbit buku = ")
    tahun = input("Masukkan tahun buku = ")

    if (judul and penulis and penerbit and tahun):
      buku = (judul, penulis, penerbit, tahun, id_buku)

      cursor.execute("UPDATE buku SET judul = ?, penulis = ?, penerbit = ?, tahun = ? WHERE id = ?", buku)
      conn.commit()

      print("========================================================")
      print("Buku Berhasil Diperbarui")
    else:
      print("Input tidak sesuai")
  else:
    print("Buku Tidak Ditemukan")

# Hapus Buku
def hapusBuku():
  print("====================== Hapus Buku =======================")
  id_buku = input("Masukkan id buku = ")

  cursor.execute("SELECT COUNT(*) as total FROM buku WHERE id = ?", id_buku)
  
  data_buku = cursor.fetchone()
  total = data_buku['total']

  if total > 0:
    cursor.execute("DELETE FROM buku WHERE id = ?", (id_buku))
    conn.commit()

    print("========================================================")
    print("Buku Berhasil Dihapus")
  else:
    print("Buku Tidak Ditemukan")

def pilihMenu(no):
  if no == 1:
    tampilBuku()
  elif no == 2:
    tambahBuku()
  elif no == 3:
    lihatBuku()
  elif no == 4:
    editBuku()
  elif no == 5:
    hapusBuku()
  else:
    print("No Harus Di antara 1-5")

def main():
  print("===================== Daftar Menu ======================")

  daftar_menu = ["Tampilkan Semua Buku", "Tambah Buku", "Lihat Buku", "Edit Buku", "Hapus Buku"]

  for no, menu in enumerate(daftar_menu, start = 1):
    print("{}. {}".format(no, menu))

  # Pilih Menu

  print("====================== Pilih Menu ======================")

  input_no = 0

  while (input_no < 1 or input_no > 5):
    input_no = int(input("Pilih No Menu = "))

    if (input_no < 1 or input_no > 5):
      print("No harus di antara 1-5")

  pilihMenu(input_no)

# Main

print("========== Sistem Pendataan Buku Perpustakaan ==========")

mulai = True

while mulai:
  main()

  print("========================================================")

  mulaiLagi = input("Mulai lagi ? Y/N ")
  mulai = mulaiLagi.lower() == "y"