tiket = {
    "jakarta" : 200000, 
    "bandar Lampung" : 150000,
    "bandung" : 180000,
    "yogyakarta" : 200000,
    "palembang" : 100000
}



data = []

def tambah():
    nama = input('Masukan nama pelanggan : ')
    print("""
    Kota Tujuan tersedia :
    Jakarta : 200000
    Bandar Lampung : 150000
    Bandung : 180000
    Yogyakarta : 200000
    Palembang : 100000
""")

    tujuan = input('pilih  kota tujuan :').lower()

    if tujuan in tiket:
        jumlah = int(input('Masukan Jumlah tiket :'))
        total = tiket[tujuan] * jumlah
        print(f"Total harga tiket : {total}")
        print(f"""
    =====E CELERON TICKET=====
          
    Nama pemesan tiket : {nama}
    Kota tujuan yang dipesan : {tujuan} 
    Jumlah tiket yang dipesan : {jumlah}
    Total harga bayar : {total}

         SIMPAN RESI INI
    UNTUK BUKTI TRANSAKSI YANG SAH
    """)
    
    else:
        print('Kota tujuan tidak tersedia')

tambah()




