tiket = {
    "jakarta" : 200000, 
    "bandar lampung" : 150000,
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

    data.append([nama, tujuan, jumlah, total])
    print(data[0][1])

def cari_data():
    nama = input("Masukkan Nama yang ingin dicari : ")
    ketemu = False

    for i in data:
        if i[0].lower() == nama.lower():
            print(f"""
Data penumpang ditemukan
Nama            : {i[0]}    
Kota Tujuan     : {i[1]}    
Jumlah Tiket    : {i[2]}    
Total Harga     : {i[3]}    
                
""")
            
            ketemu = True
            break

        if not ketemu:
            print("Data tidak ketemu")













while True:
    print("""
=== SISTEM PEMESANAN TIKET TRAVEL ===
1. Tambah Data Penumpang
2. Cari Data Penumpang
3. Tampilkan Semua Data + Total Pendapatan
4. Keluar
""")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        cari_data()
    # elif pilihan == "3":
    #     tampilkan_data()
    # elif pilihan == "4":
        # print("Program selesai. Terima kasih 🙏")
        # break
    else:
        print("Pilihan tidak valid ❌")







