from InquirerPy import inquirer
from InquirerPy.separator import Separator

properties = []

def tambah_data():
    nama = inquirer.text(message="Masukkan nama properti:").execute()
    harga = inquirer.text(message="Masukkan harga properti:").execute()
    lokasi = inquirer.text(message="Masukkan lokasi properti:").execute()
    properties.append({"nama": nama, "harga": harga, "lokasi": lokasi})
    print("\n Data berhasil ditambahkan!\n")

def lihat_data():
    if not properties:
        print("\n  Belum ada data properti.\n")
        return
    print("\n=== DATA PROPERTI ===")
    for i, prop in enumerate(properties, start=1):
        print(f"{i}. {prop['nama']} | {prop['harga']} | {prop['lokasi']}")
    print()

def edit_data():
    if not properties:
        print("\n  Tidak ada data untuk diedit.\n")
        return
    pilihan = inquirer.select(
        message="Pilih properti yang ingin diedit:",
        choices=[f"{i+1}. {p['nama']}" for i, p in enumerate(properties)],
        qmark="",  # hilangkan tanda ?
    ).execute()
    index = int(pilihan.split(".")[0]) - 1
    prop = properties[index]

    prop["nama"] = inquirer.text(message="Nama baru:", default=prop["nama"], qmark="").execute()
    prop["harga"] = inquirer.text(message="Harga baru:", default=prop["harga"], qmark="").execute()
    prop["lokasi"] = inquirer.text(message="Lokasi baru:", default=prop["lokasi"], qmark="").execute()
    print("\n  Data berhasil diperbarui!\n")

def hapus_data():
    if not properties:
        print("\n  Tidak ada data untuk dihapus.\n")
        return
    pilihan = inquirer.select(
        message="Pilih properti yang ingin dihapus:",
        choices=[f"{i+1}. {p['nama']}" for i, p in enumerate(properties)],
        qmark="",  # hilangkan tanda ?
    ).execute()
    index = int(pilihan.split(".")[0]) - 1
    properties.pop(index)
    print("\n  Data berhasil dihapus!\n")

def main():
    while True:
        choice = inquirer.select(
            message=(
                "  ===========================\n"
                "  |    PENJUALAN PROPERTI   |\n"
                "  ===========================  "
            ),
            choices=[
                "| 1. Tambah Data Properti |",
                "| 2. Lihat Data Properti  |",
                "| 3. Edit Data Properti   |",
                "| 4. Hapus Data Properti  |",
                "| 5. Keluar Program       |",
                Separator("==========================="),  # ini tidak selectable
            ],
            qmark="",
            instruction="",
        ).execute()

        if choice.startswith("| 1"):
            tambah_data()
        elif choice.startswith("| 2"):
            lihat_data()
        elif choice.startswith("| 3"):
            edit_data()
        elif choice.startswith("| 4"):
            hapus_data()
        elif choice.startswith("| 5"):
            print("\n Terima kasih telah menggunakan program!\n")
            break


if __name__ == "__main__":
    main()
