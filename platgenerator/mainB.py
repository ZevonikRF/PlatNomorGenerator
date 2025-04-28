import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (JABODETABEK) & jenis kendaraan 

# Format : D XXXX dSS
# D : Daerah (Karena Jakarta => otomatis B)
# X : Angka Acak (tergantung tipe kendaraan)
# d : Domisili
# S : Huruf Acak

# def lihatDomisili():
#     for i in datadomisili.domisiliJakarta:
#         print(i)

# def lihatTipeKendaraan():
#     for i in datatipekendaraan.tipeKendaraan:
#         print(i)

def generator(userDomisili, userTipe):
    alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    arrayJakBar = ["B","H"]
    arrayJakTim = ["T","R"]
    arrayJakSel = ["S","D"]
    arrayDepok = ["E","Z"]
    arrayTangerangKota = ["C","V"]
    arrayTangerangSelatan = ["N","W"]
    match userDomisili:
        case 1: kodePelat = "P"
        case 2: 
            if userTipe == 2:
                kodePelat = random.choice(arrayJakBar)
            else:
                kodePelat = "B"
        case 3: 
            if userTipe == 2:
                kodePelat = random.choice(arrayJakTim)
            else:
                kodePelat = "T"
        case 4: kodePelat = "U"
        case 5: 
            if userTipe == 2:
                kodePelat = random.choice(arrayJakSel)
            else:
                kodePelat = "S"
        case 6: kodePelat = "F"
        case 7: kodePelat = "K"
        case 8: kodePelat = random.choice(arrayDepok)
        case 9: kodePelat = "J"
        case 10: kodePelat = random.choice(arrayTangerangKota)
        case 11: kodePelat = random.choice(arrayTangerangSelatan)
    match userTipe:
        case 1: angkaAcak = random.randint(3000,6999)
        case 2: angkaAcak = random.randint(1000,2999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    PelatHuruf1 = random.choice(alfabet)
    PelatHuruf2 = random.choice(alfabet)
    print(f"B {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")


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
