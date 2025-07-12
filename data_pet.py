import os
from csv import DictWriter

data_pets = [
    {"event": "Lunar", "egg": "Night Egg", "pet": "Hedgehog", "harga": "2000"},
    {"event": "Lunar", "egg": "Night Egg", "pet": "Mole", "harga": "2000"},
    {"event": "Lunar", "egg": "Night Egg", "pet": "Frog", "harga": "5000"},
    {"event": "Lunar", "egg": "Night Egg", "pet": "Echo Frog", "harga": "20000"},
    {"event": "Lunar", "egg": "Night Egg", "pet": "Night Owl", "harga": "10000"},
    {"event": "Lunar", "egg": "Night Egg", "pet": "Raccoon", "harga": "60000"},

    {"event": "Bee Swarm", "egg": "Bee Egg", "pet": "Bee", "harga": "2000"},
    {"event": "Bee Swarm", "egg": "Bee Egg", "pet": "Honey Bee", "harga": "5000"},
    {"event": "Bee Swarm", "egg": "Bee Egg", "pet": "Bear Bee", "harga": "20000"},
    {"event": "Bee Swarm", "egg": "Bee Egg", "pet": "Petal Bee", "harga": "10000"},
    {"event": "Bee Swarm", "egg": "Bee Egg", "pet": "Queen Bee", "harga": "40000"},

    {"event": "Bee Swarm", "egg": "Anti Bee Egg", "pet": "Wasp", "harga": "1000"},
    {"event": "Bee Swarm", "egg": "Anti Bee Egg", "pet": "Tarantula Hawk", "harga": "5000"},
    {"event": "Bee Swarm", "egg": "Anti Bee Egg", "pet": "Moth", "harga": "10000"},
    {"event": "Bee Swarm", "egg": "Anti Bee Egg", "pet": "Butterfly", "harga": "40000"},
    {"event": "Bee Swarm", "egg": "Anti Bee Egg", "pet": "Disco Bee", "harga": "50000"},

    {"event": "Summer", "egg": "Oasis Egg", "pet": "Meerkat", "harga": "2000"},
    {"event": "Summer", "egg": "Oasis Egg", "pet": "Sand Snake", "harga": "2000"},
    {"event": "Summer", "egg": "Oasis Egg", "pet": "Axolotl", "harga": "5000"},
    {"event": "Summer", "egg": "Oasis Egg", "pet": "Hyacinth Macaw", "harga": "10000"},
    {"event": "Summer", "egg": "Oasis Egg", "pet": "Fennec Fox", "harga": "50000"},

    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Raptor", "harga": "2000"},
    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Triceratops", "harga": "7000"},
    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Stegosaurus", "harga": "5000"},
    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Pterodactyl", "harga": "10000"},
    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Brontosaurus", "harga": "40000"},
    {"event": "Prehistoric", "egg": "Dinosaurus Egg", "pet": "Trex", "harga": "60000"},
]

data_sementara = data_pets.copy()

def login_admin():
    print("\n=== LOGIN ADMIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    if username == "Jesen" and password == "1125":
        print("Login berhasil, selamat datang Admin!")
        return True
    else:
        print("Username atau password salah, coba lagi ya.")
        return False

def tampilkan_data():
    print("\n=== LIST DATA PET ===")
    for i, pet in enumerate(data_sementara, start=1):
        print(f"{i}. Event: {pet['event']} | Egg: {pet['egg']} | Pet: {pet['pet']} | Harga: Rp {pet['harga']}")


def tambah_pet_baru():
    print("\n=== TAMBAH PET BARU ===")
    event = input("Masukkan nama event: ").strip()
    egg = input("Masukkan jenis egg: ").strip()
    pet = input("Masukkan nama pet: ").strip()
    harga = input("Masukkan harga pet: ").strip()

    if event and egg and pet and harga:
        data_sementara.append({
            "event": event,
            "egg": egg,
            "pet": pet,
            "harga": harga
        })
        print("Pet baru berhasil ditambahkan di data sementara.")
    else:
        print("Data tidak lengkap, coba lagi ya.")

def edit_pet():
    tampilkan_data()
    try:
        pilih = int(input("Pilih nomor pet yang mau diedit: "))
        if 1 <= pilih <= len(data_sementara):
            idx = pilih - 1
            pet = data_sementara[idx]
            print("Kosongkan jika tidak ingin diubah.")
            event = input(f"Event baru (sekarang: {pet['event']}): ").strip() or pet['event']
            egg = input(f"Egg baru (sekarang: {pet['egg']}): ").strip() or pet['egg']
            nama_pet = input(f"Nama pet baru (sekarang: {pet['pet']}): ").strip() or pet['pet']
            harga = input(f"Harga baru (sekarang: {pet['harga']}): ").strip() or pet['harga']

            data_sementara[idx] = {
                "event": event,
                "egg": egg,
                "pet": nama_pet,
                "harga": harga
            }
            print("Data pet berhasil diedit di buffer.")
        else:
            print("Nomor yang kamu pilih gak valid.")
    except:
        print("Inputnya salah, coba ulang.")

def hapus_pet():
    tampilkan_data()
    try:
        pilih = int(input("Pilih nomor pet yang mau dihapus: "))
        if 1 <= pilih <= len(data_sementara):
            idx = pilih - 1
            pet = data_sementara.pop(idx)
            print(f"Pet {pet['pet']} berhasil dihapus dari data sementara.")
        else:
            print("Nomor gak valid, coba lagi.")
    except:
        print("Inputnya salah, coba ulang.")

def menu_pembeli():
    try:
        events = sorted(set(p['event'] for p in data_sementara))
        print("\n=== PILIH EVENT ===")
        for i, ev in enumerate(events, start=1):
            print(f"{i}. {ev}")
        pilih_ev = int(input("Pilih nomor event: "))
        event_dipilih = events[pilih_ev - 1]

        eggs = []
        for p in data_sementara:
            if p['event'] == event_dipilih and p['egg'] not in eggs:
                eggs.append(p['egg'])

        print(f"\n=== PILIH EGG DI EVENT {event_dipilih} ===")
        for i, egg in enumerate(eggs, start=1):
            print(f"{i}. {egg}")
        pilih_egg = int(input("Pilih nomor egg: "))
        egg_dipilih = eggs[pilih_egg - 1]

        pets = [p for p in data_sementara if p['event'] == event_dipilih and p['egg'] == egg_dipilih]

        print(f"\n=== PILIH PET DI EGG {egg_dipilih} ===")
        for i, pet in enumerate(pets, start=1):
            print(f"{i}. {pet['pet']} (Rp {pet['harga']})")

        pilih_pet = int(input("Pilih nomor pet yang mau dibeli: "))
        pet_dipilih = pets[pilih_pet - 1]

        nama_pembeli = input("Masukkan nama Anda: ").strip()
        if not nama_pembeli:
            print("Nama gak boleh kosong ya!")
            return

        sudah_ada = os.path.isfile("transaksi.csv")
        with open("transaksi.csv", "a", newline="") as file:
            fieldnames = ['nama', 'event', 'egg', 'pet', 'harga']
            writer = DictWriter(file, fieldnames=fieldnames)

            if not sudah_ada or os.stat("transaksi.csv").st_size == 0:
                writer.writeheader()

            writer.writerow({
                "nama": nama_pembeli,
                "event": pet_dipilih['event'],
                "egg": pet_dipilih['egg'],
                "pet": pet_dipilih['pet'],
                "harga": pet_dipilih['harga']
            })

        print(f"\nSip! {pet_dipilih['pet']} sudah dibeli sama {nama_pembeli} dengan harga Rp {pet_dipilih['harga']}")

    except Exception as e:
        print("Waduh, ada error nih:", e)

def menu_admin():
    if login_admin():
        while True:
            print("\n=== MENU ADMIN ===")
            print("1. Tambah data pet")
            print("2. Edit data pet")
            print("3. Hapus data pet")
            print("4. Kembali ke menu utama")
            pilih = input("Pilih menu (1-4): ").strip()

            if pilih == "1":
                tambah_pet_baru()
            elif pilih == "2":
                edit_pet()
            elif pilih == "3":
                hapus_pet()
            elif pilih == "4":
                print("Kembali ke menu utama...")
                break
            else:
                print("Pilihan gak valid, coba lagi.")

def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Masuk sebagai pembeli")
        print("2. Masuk sebagai admin")
        print("3. Keluar")
        pilih = input("Pilih menu (1-3): ").strip()

        if pilih == "1":
            menu_pembeli()
        elif pilih == "2":
            menu_admin()
        elif pilih == "3":
            print("Makasih sudah main, sampai jumpa!")
            break
        else:
            print("Pilihan gak valid, coba ulang ya.")

if __name__ == "__main__":
    menu_utama()
