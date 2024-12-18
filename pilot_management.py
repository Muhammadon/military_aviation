import os
from rich.console import Console
console = Console()

# ======================================== Fungsi untuk Create ======================================== #
def tambah_pilot(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()
    console.print("═"*60,justify="center")
    console.print("🌟  TAMBAH DATA PILOT BARU  🌟",justify="center")
    console.print("═"*60,justify="center")

    # Input data pilot
    name = input(" "*84+"✈️  Nama Pilot: ")
    console.print("\n"+" "*84+"(Letnan, Mayor, Jendral)")
    rank = input(" "*84+"📋 Jabatan Pilot: ")

    # Menyimpan data pilot ke database
    query = "INSERT INTO pilot (name, `rank`) VALUES (%s, %s)"
    cursor.execute(query, (name, rank))
    connection.commit()

    # Pesan sukses
    console.print("─"*60,justify="center")
    console.print("✨  Pilot Berhasil Ditambahkan!  ✨",justify="center",style="Green")
    console.print("─"*60,justify="center")
    console.print(" "*86+f"  Nama   : {name}")
    console.print(" "*86+f"  Jabatan: {rank}\n")
    console.print("Informasi Pilot berhasil ditambahkan ke sistem.",justify="center")
    console.print("─"*60,justify="center")

    # Tanyakan apakah ingin menambahkan lagi
    choice = input("\n"+" "*85+"Apakah Anda ingin menambahkan pilot lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        tambah_pilot(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


# ======================================== Fungsi untuk read ======================================== #
def lihat_daftar_pilot(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()
    query = "SELECT * FROM pilot"
    cursor.execute(query)
    result = cursor.fetchall()

    if cursor.rowcount == 0:
        console.print("─"*60,justify="center")
        console.print("🚨  Tidak Ada Data Tersedia  🚨",justify="center")
        console.print("─"*60,justify="center")
    else:
        console.print("\n" + "═"*75,justify="center")
        console.print("🌟  DAFTAR PILOT YANG TERDAFTAR  🌟",justify="center")
        console.print("═"*75,justify="center")

        console.print(f"{'ID Pilot':<10} {'Nama Pilot':<20} {'Jabatan':<15} {'ID Pesawat':<10}",justify="center")
        console.print("─"*75,justify="center")
        
        for data in result:
            if not data[3]:  # Jika ID Pesawat adalah None atau kosong
                console.print(
                    f"[red]{data[0]:<10} {data[1]:<20} {data[2]:<15} N/A[/red]",
                    justify="center",
                )
            else:
                console.print(
                    f"{data[0]:<10} {data[1]:<20} {data[2]:<15} {data[3]:<10}",
                    justify="center",
                )
        console.print("═"*75+"\n",justify="center")



# ======================================== Fungsi untuk update ======================================== #
def edit_data_pilot(connection):
    cursor = connection.cursor()
    lihat_daftar_pilot(connection)
    
    pilot_id = input(" "*87+"✏️  Pilih ID Pilot yang Ingin Diubah : ")

    name = input(" "*87+"Nama Baru Pilot                     : ")
    print("\n"+" "*87+"(Letnan, Mayor, Jendral)")
    rank = input(" "*87+"Jabatan Baru Pilot                  : ")

    console.print("\nDaftar Pesawat ",justify="center")
    console.print("ID Pilot │ Nama Pesawat",justify="center")
    console.print("─"*54,justify="center")
    cursor.execute("SELECT aircraft_id, tail_number FROM aircraft")
    aircrafts = cursor.fetchall()
    for aircraft in aircrafts:
        test1 = print(" "*107+f"{aircraft[0]:<4} │ {aircraft[1]:<10}")
    console.print("─"*54,justify="center")

    aircraft_id = input(" "*93+"Nomor Baru Pesawat yang Digunakan   : "+"\n")

    query = "UPDATE pilot SET name = '"+name+"', `rank` = '"+rank+"', aircraft_id = '"+aircraft_id+"' WHERE pilot_id = '"+pilot_id+"'"
    cursor.execute(query)
    connection.commit()
    console.print("─"*75,justify="center")
    console.print(f"✨  Pilot dengan ID {pilot_id} berhasil diubah.  ✨",justify="center",style="Green")
    console.print("─"*75,justify="center")

    choice = input("\n"+" "*88+"Apakah Anda ingin mengedit pesawat lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        edit_data_pilot(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


# ======================================== Fungsi untuk delete ======================================== #
def hapus_pilot(connection):
    lihat_daftar_pilot(connection)  # Menampilkan daftar pilot
    
    pilot_id = input(" "*83+"🗑️  Masukkan ID Pilot yang ingin dihapus: ")

    query = "DELETE FROM pilot WHERE pilot_id = '" + pilot_id + "'"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("\n" + "─"*75,justify="center")
    console.print("✨  PENGHAPUSAN BERHASIL!  ✨",justify="center",style="Green")
    console.print(f"✔️ Pilot dengan ID {pilot_id} berhasil dihapus dari daftar pilot.",justify="center")
    console.print("─"*75,justify="center")

    # Tanyakan apakah ingin menghapus lagi
    choice = input(" "*87+"Apakah Anda ingin menghapus data pilot lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        hapus_pilot(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')



# ======================================== Fungsi untuk search ======================================== #
def cari_pilot(connection):
    cursor = connection.cursor()

    keyword = input("\n"+" "*93+"🔍  Masukkan Kata Kunci Pencarian: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    query = "SELECT * FROM pilot WHERE name LIKE '%{}%' OR `rank` LIKE '%{}%'".format(keyword, keyword)
    cursor.execute(query)
    result = cursor.fetchall()

    if cursor.rowcount == 0:
        console.print("─"*60+"\n", justify="center")
        console.print("⚠️  Tidak Ada Data yang Ditemukan!",justify="center",style="red")
        console.print("\n"+"─"*60, justify="center")
    else:
        console.print("\n" + "─"*48,justify="center")
        console.print(f"📑  Hasil Pencarian untuk '{keyword}':",justify="center")
        console.print("─"*48,justify="center")
        console.print("\n{:<10} {:<20} {:<15} {:<10}".format("ID", "Nama Pilot", "Jabatan", "ID Pesawat"),justify="center")
        console.print("═"*68,justify="center")
        for data in result:
            if not data[3]:  # Jika ID Pesawat adalah None atau kosong
                console.print(
                    f"[red]{data[0]:<10} {data[1]:<20} {data[2]:<15} N/A[/red]",
                    justify="center",
                )
            else:
                console.print(
                    f"{data[0]:<10} {data[1]:<20} {data[2]:<15} {data[3]:<10}",
                    justify="center",
                )
        console.print("═" * 68, justify="center")

# Tanyakan apakah ingin kembali ke menu kelola
    choice = input("\n"+" "*93+"Apakah Anda ingin mencari lagi? (y/n): ").strip().lower()
    if choice == 'y':
        cari_pilot(connection)
    else:
        console.print("🔙 Kembali ke menu utama.",justify="center")
        os.system('cls' if os.name == 'nt' else 'clear')




# ======================================== Fungsi untuk kelola ======================================== #
def kelola_pilot(connection):
    while True:
        # Header dengan dekorasi
        
        console.print("┌"+"─"*42+"┐",justify="center")
        console.print("│          "+"  MENU KELOLA PILOT  "+"           │",justify="center",style="cyan")
        console.print("├"+"─"*42+"┤",justify="center")
        console.print("│     "+"🔹 Pilih opsi yang tersedia: 🔹"+"      │",justify="center")

        # Menu dengan ikon untuk setiap opsi
        console.print("│"+"[1] Tambah Pilot Baru "+"                    │",justify="center")
        console.print("│"+"[2] Lihat Daftar Pilot "+"                   │",justify="center")
        console.print("│"+"[3] Edit Data Pilot "+"                      │",justify="center")
        console.print("│"+"[4] Hapus Pilot "+"                          │",justify="center")
        console.print("│"+"[5] Cari Pilot "+"                           │",justify="center")
        console.print("│"+"[6] Kembali "+"                              │",justify="center")
        console.print("└" + "─"*42+"┘",justify="center")
        
        # Input pilihan
        pilihan = input(" "*93+"💡 Masukkan nomor pilihan Anda (1-6): ")
        
        # Validasi dan navigasi menu
        if pilihan == "1":
            console.print("\n➕ Anda memilih *Tambah Pilot Baru*\n",justify="center")
            tambah_pilot(connection)
        elif pilihan == "2":
            console.print("\n📋 Anda memilih *Lihat Daftar Pilot*\n",justify="center")
            lihat_daftar_pilot(connection)
        elif pilihan == "3":
            console.print("\n✏️ Anda memilih *Edit Data Pilot\n*",justify="center")
            edit_data_pilot(connection)
        elif pilihan == "4":
            console.print("\n❌ Anda memilih *Hapus Pilot*\n",justify="center")
            hapus_pilot(connection)
        elif pilihan == "5":
            console.print("\n🔍 Anda memilih *Cari Pilot*",justify="center")
            cari_pilot(connection)
        elif pilihan == "6":
            console.print("\n🔙 Kembali ke menu utama.\n",justify="center")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')