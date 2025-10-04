tiket = {
    "1" : 200000,
    "2" : 150000,
    "3" : 180000,
    "4" : 200000,
    "5" : 100000
}

# tiket = [20000, 150000, 180000, 200000, 100000]

data = []

def tambah():
    nama = input('Masukan nama pelanggan : ')
    print("""
    Kota Tujuan tersedia :
    1.Jakarta
    2.Bandar Lampung
    3.Bandung
    4.Yogyakarta
    5.Palembang
""")

    Tujuan = input('pilih no kota tujuan :')

    if Tujuan in tiket:
        jumlah = int(input('Masukan Jumlah tiket :'))
        total = tiket[Tujuan] * jumlah
        print(f"Total harga tiket : {total}")

    else:
        print('Kota tujuan tidak tersedia')
tambah()

