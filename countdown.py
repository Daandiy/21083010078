from datetime import datetime, timedelta

# Fungsi untuk menghitung waktu mundur
def hitung_waktu_mundur(deadline):
    # Mendapatkan waktu sekarang
    sekarang = datetime.now()

    # Menghitung selisih waktu antara deadline dan sekarang
    selisih = deadline - sekarang

    # Mengembalikan selisih waktu dalam hari, jam, menit, dan detik
    return selisih.days, selisih.seconds // 3600, (selisih.seconds // 60) % 60, selisih.seconds % 60

print("+==============================================+")
print( "|Program dibuat oleh : Dandi Nur Faizi|")
print( "|NPM : 21083010078|")
print( "|Jurusan : Sains Data|")
print("+==============================================+")
print(" ")
print("|Program menghitung waktu mundur tugas kuliah|")
print(" ")
print("+==============================================+")
print(" ")


# Mendapatkan tanggal deadline dari user
print("Masukkan tanggal deadline (dd/mm/yyyy hh:mm:ss):") #CONTOH(22/12/2022 23:59:59)
deadline = input()

# Mengubah tanggal deadline menjadi objek datetime
deadline = datetime.strptime(deadline, '%d/%m/%Y %H:%M:%S')

# Menghitung waktu mundur
hari, jam, menit, detik = hitung_waktu_mundur(deadline)

# Menampilkan hasil perhitungan
print(" ")
print("+-----------------------------------------------------------------------------+")
print(f"Waktu pengumpulan tersisa: {hari} hari, {jam} jam, {menit} menit, {detik} detik")
print("Segera Dikumpulkan!!! ")
print("+-----------------------------------------------------------------------------+")
