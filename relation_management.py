import os
from rich.console import Console
from rich.align import Align
console = Console()

# ======================================== Fungsi untuk Create ======================================== #
def tugaskan_pilot_ke_pesawat(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()

    console.print("═"*44,justify="center")
    console.print("Daftar Pilot (Tanpa Pesawat)",justify="center",style="red")
    console.print("═" *44+"\n",justify="center")
    cursor.execute("SELECT pilot_id, name, rank, aircraft_id FROM pilot WHERE aircraft_id IS NULL;")
    pilots = cursor.fetchall()
    if not pilots:
        console.print("⚠️  Tidak Ada Data yang Ditemukan!",justify="center",style="red")
        return
    console.print("{:<10} {:<20} {:<15} {:<10}".format("ID Pilot", "Nama Pilot","Jabatan","ID Pesawat"),justify="center")
    console.print("─" * 60,justify="center")
    for pilot in pilots:
        aircraft_id = pilot[3] if pilot[3] is not None else "[red]N/A[/red]"
        console.print("{:<10} {:<20} {:<15} {:<10}".format(pilot[0], pilot[1], pilot[2], aircraft_id),justify="center")
    console.print("═" * 60,justify="center")

    id_pilot = input(" "*93+"Masukkan ID Pilot yang Akan Ditugaskan: ")

    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("═" * 45,justify="center")
    console.print("Daftar Pesawat",justify="center",style="green")
    console.print("═" * 45+"\n",justify="center")
    cursor.execute("SELECT aircraft_id, tail_number FROM aircraft")
    aircrafts = cursor.fetchall()
    if not aircrafts:
        console.print("⚠️  Tidak ada pesawat yang tersedia.")
        return

    console.print(Align.center("{:<10}│{:<30}".format("ID Pesawat", "Nama Pesawat")))
    console.print("─" * 50,justify="center")
    for aircraft in aircrafts:
        console.print(Align.center("{:<10}│{:<30}".format(aircraft[0], aircraft[1])))
    console.print("═" * 50,justify="center")

    id_aircraft = input(" "*93+"Masukkan ID Pesawat yang akan Ditugaskan: ")

    cursor.execute("SELECT aircraft_id FROM pilot WHERE pilot_id = %s", (id_pilot,))
    result = cursor.fetchone()
    if result is not None and result[0] is not None:
        console.print("\n⚠️  Pilot ini sudah memiliki pesawat.",justify="center",style="red")
        return

    # Update Relasi
    cursor.execute("UPDATE pilot SET aircraft_id = %s WHERE pilot_id = %s", (id_aircraft, id_pilot,))
    connection.commit()
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("\n"+"─" * 68,justify="center")
    console.print(f"✨  Pilot dengan ID {id_pilot} berhasil ditugaskan ke pesawat dengan ID {id_aircraft}.  ✨",justify="center",style="green")
    console.print("─" * 68+"\n",justify="center")

# ======================================== Fungsi untuk read ======================================== #
def lihat_pilot_dengan_pesawat(connection):
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor = connection.cursor()

    # Judul dan pembatas
    console.print(Align.center("═" * 70))
    console.print(Align.center("Relasi Pilot dan Pesawat"))
    console.print(Align.center("═" * 70))
    
    # Query untuk mendapatkan data relasi pilot dan pesawat
    cursor.execute("""
        SELECT 
            pilot.name AS nama_pilot, 
            pilot.`rank` AS rank_pilot, 
            aircraft.tail_number AS nama_pesawat 
        FROM pilot 
        LEFT JOIN aircraft ON pilot.aircraft_id = aircraft.aircraft_id;
    """)
    relations = cursor.fetchall()

    if not relations:
        console.print(Align.center("⚠️  Tidak ada data relasi pilot dan pesawat.\n"))
    else:
        # Header tabel
        header = "{:<20} {:<20} {:<20}".format("Nama Pilot", "Pangkat Pilot", "Nama Pesawat")
        console.print(Align.center(header))
        console.print(Align.center("─" * 70))

        # Data relasi
        for relation in relations:
            nama_pilot, rank_pilot, nama_pesawat = relation
            if not nama_pesawat:
                nama_pesawat = "Belum Ditugaskan"
                row = "[red]{:<20} {:<20} {:<20}[/red]".format(nama_pilot, rank_pilot, nama_pesawat)
            else:
                row = "{:<20} {:<20} {:<20}".format(nama_pilot, rank_pilot, nama_pesawat)
            
            console.print(Align.center(row))

    console.print(Align.center("═" * 70))



# ======================================== Fungsi untuk delete ======================================== #
def hapus_pesawat_untuk_pilot(connection):
    cursor = connection.cursor()

    # Tampilan daftar pilot
    console.print("═" * 50,justify="center")
    console.print("Daftar Pilot (Dengan Pesawat)",justify="center")
    console.print("═" * 50,justify="center")

    cursor.execute(
        "SELECT pilot.pilot_id, pilot.name, aircraft.tail_number "
        "FROM pilot "
        "INNER JOIN aircraft ON pilot.aircraft_id = aircraft.aircraft_id;"
    )
    pilots = cursor.fetchall()

    if not pilots:
        console.print("\n   ⚠️  Tidak ada pilot yang memiliki pesawat.",justify="center")
    else:
        # Header tabel
        console.print(Align.center(f"{'ID Pilot':<10} {'Nama Pilot':<15} {'Nama Pesawat':<20}"))
        console.print("─" * 50,justify="center")

        # Data daftar pilot
        for pilot in pilots:
            row = (f"{pilot[0]:<10} {pilot[1]:<15} {pilot[2]:<20}")
            console.print(Align.center(row))

    # Input ID Pilot
    console.print("═" * 50 + "\n",justify="center")
    id_pilot = input(" "*90+"Masukkan ID Pilot yang ingin dihapus relasinya: ")

    # Validasi apakah ID pilot memiliki pesawat
    cursor.execute("SELECT aircraft_id FROM pilot WHERE pilot_id = %s", (id_pilot,))
    result = cursor.fetchone()

    if result is None or result[0] is None:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print("\n"+"─" * 45,justify="center")
        console.print("⚠️  ID pilot Invalid ⚠️",justify="center",style="red")
        console.print("─" * 45,justify="center")
        return

    # Hapus relasi pesawat dari pilot
    cursor.execute("UPDATE pilot SET aircraft_id = NULL WHERE pilot_id = %s", (id_pilot,))
    connection.commit()

    # Konfirmasi penghapusan
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("\n"+"─" * 75 + "\n",justify="center")
    console.print(f"✨  Relasi pesawat untuk Pilot ID {id_pilot} berhasil dihapus.  ✨\n",justify="center",style="green")
    console.print("─" * 75,justify="center")

    choice = input("\n"+" "*87+"Apakah Anda ingin menghapus relasi lainnya? (y/n): ").strip().lower()
    if choice == 'y':
        hapus_pesawat_untuk_pilot(connection)  # Jika ya, panggil ulang fungsi
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

# ======================================== Fungsi untuk kelola ======================================== #
def kelola_relasi(connection):
    while True:
        # Header dengan dekorasi
        console.print("┌"+"─"*42+"┐",justify="center")
        console.print("│  "+"  MENU KELOLA RELASI PILOT - PESAWAT  "+"  │",justify="center",style="cyan")
        console.print("├"+"─"*42+"┤",justify="center")
        console.print("│      "+"🔹 Pilih opsi yang tersedia: 🔹"+"     │",justify="center")

        # Menu dengan ikon untuk setiap opsi
        console.print("│"+"[1] Tambah Relasi Baru"+"                    │",justify="center")
        console.print("│"+"[2] Lihat Relasi Pilot - Pesawat "+"         │",justify="center")
        console.print("│"+"[3] Hapus Relasi Pilot - Pesawat"+"          │",justify="center")
        console.print("│"+"[4] Kembali "+"                              │",justify="center")
        console.print("└" + "─"*42+"┘",justify="center")
        
        # Input pilihan
        pilihan = input(" "*93+"💡 Masukkan nomor pilihan Anda (1-4): ")
        
        # Validasi dan navigasi menu
        if pilihan == "1":
            console.print("\n➕ Anda memilih *Tambah Relasi Baru*",justify="center")
            tugaskan_pilot_ke_pesawat(connection)
        elif pilihan == "2":
            console.print("\n📑 Anda memilih *Lihat Relasi Pilot - Pesawat*",justify="center")
            lihat_pilot_dengan_pesawat(connection)
        elif pilihan == "3":
            console.print("\n❌ Anda memilih *Hapus Relasi Pilot - Pesawat*",justify="center")
            hapus_pesawat_untuk_pilot(connection)
        elif pilihan == "4":
            console.print("\n🔙 Kembali ke menu utama.")
            break
        else:
            # Pesan error untuk input tidak valid
            console.print("\n❌ Opsi tidak valid. Masukkan angka antara 1-4.",justify="center")
