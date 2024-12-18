import os
from rich.console import Console
from rich.align import Align
console = Console()

# ======================================== Fungsi untuk Create ======================================== #
def tambah_pesawat(connection):
    # Dekorasi input dengan lebih estetis
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("═"*60,justify="center")
    console.print("🌟  TAMBAH PESAWAT BARU  🌟",justify="center")
    console.print("═"*60,justify="center")

    # Input dengan dekorasi
    tail_number = input(" "*83+"✈️  Nama Pesawat                  : ")
    print("\n"+" "*83+"(Bomber, Jet Tempur, Pesawat Angkut, Pesawat Pengintai)")
    type = input(" "*83+"🚀 Tipe Pesawat                  : ")
    print("\n"+" "*83+"(Ready / Maintenance)")
    status = input(" "*83+"🔧 Status                        : ")
    print("\n"+" "*83+"(yyyy-mm-dd)")
    last_check = input(" "*83+"📅 Tanggal Pemeriksaan Terakhir  : ")

    # Menjalankan query untuk menyimpan data pesawat
    cursor = connection.cursor()
    query = "INSERT INTO aircraft (tail_number, type, status, last_check) VALUES ('"+tail_number+"', '"+type+"', '"+status+"', '"+last_check+"')"
    cursor.execute(query)
    connection.commit()

    # Dekorasi output
    console.print("─"*60,justify="center")
    console.print("✨  PESAWAT BERHASIL DITAMBAHKAN  ✨",justify="center",style="green")
    console.print("─"*60,justify="center")
    console.print(f" "*84+f"Pesawat dengan Nama: {tail_number}")
    console.print(f" "*84+f"Tipe: {type}")
    console.print(f" "*84+f"Status: {status}")
    console.print(f" "*84+f"Tanggal Pemeriksaan Terakhir: {last_check}")
    console.print("\n  Informasi pesawat berhasil ditambahkan ke sistem.",justify="center")
    console.print("─"*60,justify="center")

    # Tanyakan apakah ingin menambahkan lagi
    choice = input("\n"+" "*85+"Apakah Anda ingin menambahkan pesawat lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        tambah_pesawat(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

# ======================================== Fungsi untuk read ======================================== #
def lihat_daftar_pesawat(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()
    query = "SELECT * FROM aircraft"
    cursor.execute(query)
    result = cursor.fetchall()

    # Dekorasi output jika data ditemukan
    if cursor.rowcount == 0:
        console.print("─"*60,justify="center")
        console.print("🚨  Tidak Ada Data Tersedia  🚨",justify="center")
        console.print("─"*60,justify="center")
    else:
        console.print("\n" + "═"*75,justify="center")
        console.print("🌟  DAFTAR PESAWAT YANG TERDAFTAR  🌟",justify="center")
        console.print("═"*75,justify="center")

        # Header tabel dengan format yang rapi
        console.print(f"{'ID':<5} {'Nama Pesawat':<25} {'Tipe':<15} {'Status':<15} {'Last Check':<15}",justify="center")
        console.print("─" * 75,justify="center")

        # Menampilkan setiap data pesawat dalam format tabel
        for data in result:
            if data[3].lower() == "maintenance":  # Jika status "Maintenance"
                console.print(
                    f"[red]{data[0]:<5} {data[1]:<25} {data[2]:<15} {data[3]:<15} {data[4]}[/red]",
                    justify="center",
                )
            else:  # Jika status selain "Maintenance" (termasuk "Ready")
                status_color = "green" if data[3].lower() == "ready" else "yellow"
                console.print(
                    f"{data[0]:<5} {data[1]:<25} {data[2]:<15} [{status_color}]{data[3]:<15}[/{status_color}] {data[4]}",
                    justify="center",
                )
        console.print("═"*75+"\n",justify="center")


# ======================================== Fungsi untuk update ======================================== #
def edit_data_pesawat(connection):
    cursor = connection.cursor()
    lihat_daftar_pesawat(connection)
    
    # Input untuk memilih ID pesawat yang ingin diubah
    aircraft_id = input(" "*78+"✏️  Pilih ID Pesawat yang Ingin Diubah: ")

    # Input data baru
    tail_number = input(" "*78+"✈️  Nama Pesawat                  : ")
    print("\n"+" "*78+"(Bomber, Jet Tempur, Pesawat Angkut, Pesawat Pengintai)")
    type = input(" "*78+"🚀 Tipe Pesawat                  : ")
    print("\n"+" "*78+"(Ready / Maintenance)")
    status = input(" "*78+"🔧 Status                        : ")
    print("\n"+" "*78+"(yyyy-mm-dd)")
    last_check = input(" "*78+"📅  Tanggal Pemeriksaan Terakhir : ")

    # Proses update data
    query = f"UPDATE aircraft SET tail_number = '{tail_number}', type = '{type}', status = '{status}', last_check = '{last_check}' WHERE aircraft_id = '{aircraft_id}'"
    cursor.execute(query)
    connection.commit()

    # Dekorasi output untuk konfirmasi perubahan
    console.print("─"*75,justify="center")
    console.print("✨  PERUBAHAN BERHASIL!  ✨",justify="center",style="Green")
    console.print("─"*75,justify="center")
    console.print(f"Pesawat dengan ID {aircraft_id} berhasil diubah menjadi:",justify="center")
    
    # Tampilkan data baru dalam format tabel
    console.print(f"\n{'ID':<5} {'Nama Pesawat':<25} {'Tipe':<15} {'Status':<15} {'Last Check':<15}",justify="center")
    console.print("═"*75,justify="center")
    console.print(f"{aircraft_id:<5} {tail_number:<25} {type:<15} {status:<15} {last_check:<15}",justify="center")
    console.print("═"*75,justify="center")

    choice = input("\n"+" "*78+"Apakah Anda ingin mengedit pesawat lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        edit_data_pesawat(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')


# ======================================== Fungsi untuk delete ======================================== #
def hapus_pesawat(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()
    lihat_daftar_pesawat(connection)
    
    # Input untuk memilih ID pesawat yang ingin dihapus
    aircraft_id = input("\n"+" "*77+"🗑️  Pilih ID Pesawat yang Ingin Dihapus: ")

    # Proses penghapusan data
    query = f"DELETE FROM aircraft WHERE aircraft_id = '{aircraft_id}'"
    cursor.execute(query)
    connection.commit()

    # Dekorasi output untuk konfirmasi penghapusan
    console.print("\n" + "─"*75,justify="center")
    console.print("✨  PENGHAPUSAN BERHASIL!  ✨",justify="center",style="Green")
    console.print(f"Pesawat dengan ID {aircraft_id} berhasil dihapus dari daftar pesawat.",justify="center")
    console.print("─"*75,justify="center")

    # Tanyakan apakah ingin menghapus lagi
    choice = input("\n"+" "*80+"Apakah Anda ingin menghapus pesawat lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        hapus_pesawat(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')



# ======================================== Fungsi untuk search ======================================== #
def cari_pesawat(connection):
    cursor = connection.cursor()
    
    # Input kata kunci pencarian
    keyword = input("\n"+" "*93+"🔍  Masukkan Kata Kunci Pencarian: ")

    # Proses pencarian data
    query = f"SELECT * FROM aircraft WHERE tail_number LIKE '%{keyword}%' OR type LIKE '%{keyword}%' OR status LIKE '%{keyword}%'"
    cursor.execute(query)
    result = cursor.fetchall()

    # Tampilan hasil pencarian
    if cursor.rowcount == 0:
        console.print("─"*60+"\n", justify="center")
        console.print("⚠️  Tidak Ada Data yang Ditemukan!",justify="center",style="red")
        console.print("\n"+"─"*60, justify="center")
    else:
        console.print("\n" + "─"*48,justify="center")
        console.print(f"📑  Hasil Pencarian untuk '{keyword}':",justify="center")
        console.print("─"*48,justify="center")
        console.print(f"\n{'ID':<5}║{'Nama Pesawat':<25}║{'Tipe':<15}║{'Status':<15}║{'Last Check':<15}",justify="center")
        console.print("═"*76,justify="center")
        for data in result:
            status_color = "green" if data[3].lower() == "ready" else "red"
            console.print(f"{data[0]:<5}║{data[1]:<25}║{data[2]:<15}║[{status_color}]{data[3]:<15}[/{status_color}]║{data[4]:}",justify="center")
        console.print("═"*76,justify="center")

    # Tanyakan apakah ingin kembali ke menu kelola
    choice = input("\n"+" "*93+"Apakah Anda ingin mencari lagi? (y/n): ").strip().lower()
    if choice == 'y':
        cari_pesawat(connection)
    else:
        console.print("🔙 Kembali ke menu utama.",justify="center")
        os.system('cls' if os.name == 'nt' else 'clear')




# ======================================== Fungsi untuk kelola ======================================== #
def kelola_pesawat(connection):
    while True:
        # Header dengan dekorasi
        
        console.print("┌"+"─"*42+"┐",justify="center")
        console.print("│            "+"[cyan]MENU KELOLA PESAWAT[/cyan]"+"           │",justify="center")
        console.print("├"+"─"*42+"┤",justify="center")
        console.print("│      "+"🔹 Pilih opsi yang tersedia: 🔹"+"     │",justify="center")

        # Menu dengan ikon untuk setiap opsi
        console.print("│"+"[1] Tambah Pesawat Baru "+"                  │",justify="center")
        console.print("│"+"[2] Lihat Daftar Pesawat "+"                 │",justify="center")
        console.print("│"+"[3] Edit Data Pesawat "+"                    │",justify="center")
        console.print("│"+"[4] Hapus Pesawat "+"                        │",justify="center")
        console.print("│"+"[5] Cari Pesawat "+"                         │",justify="center")
        console.print("│"+"[6] Kembali "+"                              │",justify="center")
        console.print("└" + "─"*42+"┘",justify="center")

        # Input pilihan
        pilihan = input(" "*93+"💡 Masukkan nomor pilihan Anda (1-6): ")   
        
        # Validasi dan navigasi menu
        if pilihan == "1":
            console.print("\n➕ Anda memilih *Tambah Pesawat Baru*\n",justify="center")
            tambah_pesawat(connection)
        elif pilihan == "2":
            console.print("\n📋 Anda memilih *Lihat Daftar Pesawat*\n",justify="center")
            lihat_daftar_pesawat(connection)
        elif pilihan == "3":
            console.print("\n✏️ Anda memilih *Edit Data Pesawat\n*",justify="center")
            edit_data_pesawat(connection)
        elif pilihan == "4":
            console.print("\n❌ Anda memilih *Hapus Pesawat*\n",justify="center")
            hapus_pesawat(connection)
        elif pilihan == "5":
            console.print("\n🔍 Anda memilih *Cari Pesawat*",justify="center")
            cari_pesawat(connection)
        elif pilihan == "6":
            console.print("\n🔙 Kembali ke menu utama.\n",justify="center")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
