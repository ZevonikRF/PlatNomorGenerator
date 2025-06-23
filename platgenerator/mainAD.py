import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (Keresidenan Surakarta) & jenis kendaraan 

# Format : D XXXX SSd / D XXXX Sd
# D : Daerah (otomatis AD)
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
    arraySurakarta = ["A","H","S","U"]
    arraySukoharjo = ["B","K","O","T"]
    arrayKlaten = ["C","J","L","Q","V"]
    arrayBoyolali = ["D","M","W"]
    arraySragen = ["E","N","Y"]
    arrayKaranganyar = ["F","P","Z"]
    arrayWonogiri = ["G","I","R"]


    match userDomisili:
        case 1: kodePelat = random.choice(arraySurakarta)
        case 2: kodePelat = random.choice(arraySukoharjo)
        case 3: kodePelat = random.choice(arrayKlaten)
        case 4: kodePelat = random.choice(arrayBoyolali)
        case 5: kodePelat = random.choice(arraySragen)
        case 6: kodePelat = random.choice(arrayKaranganyar)
        case 7: kodePelat = random.choice(arrayWonogiri)
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    match kodePelat:
        case "A" | "B" | "C" | "D" | "E"| "F" | "G" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet)
                PelatHuruf2 = random.choice(alfabet)
                print(f"AD {str(angkaAcak)} {PelatHuruf1}{PelatHuruf2}{kodePelat}")
            else:
                PelatHuruf2 = random.choice(alfabet)
                print(f"AD {str(angkaAcak)}  {PelatHuruf2}{kodePelat}")
        case _:
            PelatHuruf2 = random.choice(alfabet)
            print(f"AD {str(angkaAcak)}  {PelatHuruf2}{kodePelat}")


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
