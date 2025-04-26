import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (Bogor, Sukabumi, Cianjur) & jenis kendaraan 

# Format : D XXXX dSS / D XXXX dS
# D : Daerah (otomatis A)
# X : Angka Acak (tergantung tipe kendaraan)
# d : Domisili
# S : Huruf Acak

# def lihatDomisili():
#     for i in datadomisili.domisiliBandungRaya:
#         print(i)

# def lihatTipeKendaraan():
#     for i in datatipekendaraan.tipeKendaraan:
#         print(i)

def generator(userDomisili, userTipe):
    alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    arraySerangKota = ["A","B","C","D"]
    arraySerangKabupaten = ["E","F","G","H","I"]
    arrayPandeglang = ["J","K","L","M"]
    arrayLebak = ["N","O","P","Q"]
    arrayCilegon = ["R","S","T","U"]
    arrayTangerang = ["V","W","X","Y","Z"]

    match userDomisili:
        case 1: kodePelat = random.choice(arraySerangKota)
        case 2: kodePelat = random.choice(arraySerangKabupaten)
        case 3: kodePelat = random.choice(arrayPandeglang)
        case 4: kodePelat = random.choice(arrayLebak)
        case 5: kodePelat = random.choice(arrayCilegon)
        case 6: kodePelat = random.choice(arrayTangerang)
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    match kodePelat:
        # Alfabet 1 untuk 3 abjad masih belum akurat; perlu data lagi, sementara pake semua alfabet
        case "V" | "W" | "X" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet)
                PelatHuruf2 = random.choice(alfabet)
                print(f"A {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf1 = random.choice(alfabet)
                PelatHuruf2 = random.choice(alfabet)
                print(f"A {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case _:
            PelatHuruf2 = random.choice(alfabet)
            print(f"A {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")


# def mainProgram():
#     iterasi = 0
#     print("===================================================")
#     print()
#     lihatDomisili()
#     print()
#     userInputDomisili = int(input("Pilihan Domisili: "))
#     print()
#     print("===================================================")
#     print()
#     lihatTipeKendaraan()
#     print()
#     userInputTipe = (int(input("Pilihan Tipe Kendaraan: ")))
#     print()
#     print("===================================================")
#     print()
#     banyakGenerate = (int(input("Mau Berapa Kali Generate?: ")))
#     print()
#     print("===================================================")
#     print("Pelat Nomor yang Di-Generate:")
#     print()
#     while iterasi < banyakGenerate:
#         generator(userInputDomisili, userInputTipe)
#         iterasi = iterasi + 1
#     print()
#     print("===================================================")
# mainProgram()
