'''
# mengambil input user


# program menghitung luas


# hasil

'''

import os

def header():
    os.system("cls")
    print(f"{'program menghitung luas':^40}")
    print(f"{'dan keliling persegi panjang':^40}")
    print(f"{'-'*40:^40}")


def inputUser():
    lebar = int(input(f"masukkan nilai lebar : "))
    panjang = int(input(f"masukkan nilai panjang : "))
    return lebar, panjang

def hasilLuas():
    luas = panjang * lebar
    return luas

def hasilKeliling():
    keliling = 2 * (panjang + lebar)
    return keliling

# program utama
while True:
    header()
    lebar, panjang = inputUser()
    luas = hasilLuas()
    keliling = hasilKeliling()

    pilihan = int(input(f"\nmasukkan pilihan (1,2,3) : "))
    if pilihan == 1:
        print(f"hasil dari keliling = {keliling}\n")
    
    elif pilihan == 2:
        print(f"\nhasil dari luas = {luas}\n")

    elif pilihan == 3:
        print(f"\nhasil dari luas = {luas}")
        print(f"hasil dari keliling = {keliling}\n")

    
    isContinue = input(f"apakah lanjut? (y/n) ")
    if isContinue == "n":
        break

print("\nprogram selesai")