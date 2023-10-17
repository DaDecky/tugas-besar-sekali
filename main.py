ls_menu = [
    {
        "nomor_menu": 1,
        "nama_menu": "Bakso",
        "harga_menu": 5000,
    },
    {
        "nomor_menu": 2,
        "nama_menu": "Mie Ayam",
        "harga_menu": 5000,
    },
    {
        "nomor_menu": 3,
        "nama_menu": "Sushi",
        "harga_menu": 10000,
    },
    {
        "nomor_menu": 4,
        "nama_menu": "x",
        "harga_menu": 5000,
    },
    {
        "nomor_menu": 5,
        "nama_menu": "y",
        "harga_menu": 7000,
    },
]
data_customer = []
# [[[0], [""], [0]]]


def menu():
    print(
        """1. Periksa Ketersediaan Meja
2. Pesan
3. Reservasi     
0. Keluar dari program"""
    )

    return


def greeting():
    print(
        """
# ---------------------------------------------------------------------------- #
#                         selamat datang di restoran pengkom                   #
# ---------------------------------------------------------------------------- #
"""
    )
    return


def jenis_dine():
    print(
        """tulis apa?
1. Dine In
2. Take Away"""
    )
    return


def list_menu():
    for menu in ls_menu:
        print(f'{menu["nomor_menu"]}. {menu["nama_menu"]} - {menu["harga_menu"]}')
    return


def pesan():
    while True:
        pesanan = int(input("Masukkan angka menu: "))
        # ------------------------ validasi input yang sesuai ------------------------ #
        menu_ada = False
        for menu in ls_menu:
            if menu["nomor_menu"] == pesanan:
                menu_ada = True
        # ---------------------------------------------------------------------------- #
        if menu_ada == True:
            jumlah = int(input("Masukkan jumlahnya: "))
            print(f"Memesan ")
    return


def dine_in():
    print(
        """

"""
    )
    return


def take_away():
    list_menu()
    pesan()
    return


def sepparator():
    return print(
        """

# ---------------------------------------------------------------------------- #


"""
    )


# ---------------------------------------------------------------------------- #


def main():
    greeting()

    # Pilih Jenis Dine
    jenis_dine()
    u_input = int(input("Pilihan: "))  # 1 atau 2

    # ------------------------ validasi input yang sesuai ------------------------ #
    opsi_valid = [1, 2]
    while u_input not in opsi_valid:
        print("Pilihan tidak sesuai, pilih 1 atau 2")
        u_input = int(input("Pilihan: "))
    # ---------------------------------------------------------------------------- #

    if u_input == 1:
        print("Anda memilih Dine In")
        sepparator()
        dine_in()
    else:  # u_input == 2:
        print("Anda memilih Take Away")
        sepparator()
        take_away()


while True:
    main()
