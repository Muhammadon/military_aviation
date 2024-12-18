import mysql.connector
import os
import pyfiglet
import time
from rich import print
from rich.align import Align
from rich.console import Console
from rich.progress import Progress
console = Console()

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "military_aviation"
)

from aircraft_management import kelola_pesawat
from pilot_management import kelola_pilot
from relation_management import kelola_relasi

import pyfiglet
import time
import os
from rich import print
from rich.console import Console
from rich.progress import Progress
from rich.align import Align

os.system('cls' if os.name == 'nt' else 'clear')
console = Console()
ascii_art = r"""
     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠿⠛⡛⠉⠒⠒⠂⣤⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢋⣀⣱⣰⠃⢀⡠⠔⡪⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢱⡀⠀⠀⠀⠀⢒⡖⢻⠿⠋⢹⠉⠻⠑⢻⡧⣤⠴⠢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠳⡄⠀⠐⠈⢈⠄⠩⣶⣿⢽⣒⣦⣤⣔⡎⠁⠉⠢⢌⣦⠀⠀
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⢀⠀⠠⠧⠤⣴⣿⣖⣶⣾⣶⣋⣠⣿⣿⣿⣿⣾⣾⢯⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣷⠞⠓⢈⠭⡯⣽⣿⣷⣷⣿⣿⣯⡷⠟⢙⡩⢝⡻⠛⣟⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⢟⠋⠙⣿⣽⣿⣿⣿⠾⡧⠔⣊⠥⣞⣮⣿⣿⣿⡿⠿⢋⡰⢔⣪⠝⣎⣡⣾⣿⣿⣿⣿⣶⣴⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠺⠎⠉⣶⣿⣿⣿⣿⣛⣿⣥⣊⣩⣩⣵⣶⡶⣈⣿⣵⣿⣿⣿⣿⣿⢿⣀⣰⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠛⠛⢿⠿⠟⠛⠒⠚⠛⠫⢭⡿⠻⢯⠉⢀⣀⣤⣾⣦⢄⣠⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠉⠉⠲⠏⠙⠻⢿⢿⠿⠛⠊⠁⠀
"""

# Cetak teks ASCII art dengan justify center
console.print(Align.center(ascii_art),style="green")
figlet_text = pyfiglet.figlet_format("Combat Readiness System", font="Bloody", width= 1000)
console.print(figlet_text,style="red",justify="center")

with Progress() as progress:
    (progress)
    task1 = progress.add_task("[red]Downloading Database...", total=10)
    task2 = progress.add_task("[green]Processing...", total=10)

    while not progress.finished:
        progress.update(task1, advance=1)
        progress.update(task2, advance=0.3)
        time.sleep(0.1)
        
os.system('cls' if os.name == 'nt' else 'clear')
def main_system_menu(connection):
    # Dekorasi pembuka
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art1 = r"""⣰⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡾
⠀⠀⣿⡍⠛⠲⣶⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠞⠉⣠⡞⠀⠀
⠀⠀⠘⣽⢷⣦⣌⣈⠋⡚⠿⣦⡀⠀⠀⣴⣶⡄⠀⠀⣠⡶⠚⠛⣙⣭⠠⣤⣶⣯⠆⠀⠀⠀
⠀⠀⠀⣼⣷⣀⠀⠀⠈⠀⠀⠀⢻⡇⠺⡿⠛⣿⡅⠀⢿⠀⠀⣼⠿⣫⣭⣠⣤⡶⠂⠀⠀⠀
⠀⠀⠀⠀⠉⠛⠿⣹⣾⠔⠃⠀⠈⠳⠾⠏⠀⠻⣷⡺⠋⠀⣤⣸⣷⣶⡾⠖⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠒⠷⣿⡻⣞⣀⣄⣀⣀⡄⠀⠀⣠⣄⣸⡿⣾⣿⡽⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠟⠯⣽⢿⡿⠃⠀⢀⣿⡙⠑⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣯⣦⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⢩⡿⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣽⡃⠀⠀
"""

# Cetak teks ASCII art dengan justify center
    console.print(Align.center(ascii_art1),style="RED   ")
    console.print("┌"+"─"*42+"┐",justify="center")
    console.print("│"+"💼  WELCOME TO [red]COMBAT READINESS[/red] SYSTEM  💼"+"│",justify="center")
    console.print("├"+"─"*42+"┤",justify="center")
    console.print("│"+"     🔹 Silakan pilih menu berikut 🔹"+"     │",justify="center")
    
    # Menu dengan ikon untuk memperjelas maksud

    console.print("│"+"[1]  Kelola Pesawat              "+"         │",justify="center")
    console.print("│"+"[2]  Kelola Pilot                "+"         │",justify="center")
    console.print("│"+"[3]  Kelola Relasi Pilot-Pesawat "+"         │",justify="center")
    console.print("│"+"[4]  Keluar                      "+"         │",justify="center")
    console.print("└" + "─"*42+"┘",justify="center")

    # Input pilihan
    pilihan = input(" "*93+"💡 Masukkan nomor pilihan Anda (1-4): ")
    
    try:
        pilihan = int(pilihan)  # Pastikan input berupa angka
        if pilihan == 1:
            console.print("\n✈️ Anda memilih *Kelola Pesawat*",justify="center")
            kelola_pesawat(connection)
        elif pilihan == 2:
            console.print("\n👨‍✈️ Anda memilih *Kelola Pilot*",justify="center")
            kelola_pilot(connection)
        elif pilihan == 3:
            console.print("\n🤝 Anda memilih *Kelola Relasi Pilot-Pesawat*\n",justify="center")
            kelola_relasi(connection)
        elif pilihan == 4:
            console.print("\n🚪 Keluar dari sistem. Terima kasih atas kunjungan Anda!\n",justify="center")
            exit()
        else:
            console.print("❌  P3ilihan tidak valid. Masukkan angka antara 1-4.")
    except ValueError:
        print("❌  Input tidak valid. Harap masukkan angka antara 1-4.")

if __name__ == "__main__":
    while(True):
        main_system_menu(connection)
        