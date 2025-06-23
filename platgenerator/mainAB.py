import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (Yogyakarta) & jenis kendaraan 

# Format : D XXXX SSd / D XXXX Sd
# D : Daerah (otomatis AB)
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
    arrayYogyakarta = ["A","F","H","I","S"]
    arrayBantul = ["B","K","G","J","T"]
    arrayKulon = ["C","L","O","V","P"],
    arrayGunung = ["D","R","M","W"]
    arraySleman = ["E","N","Y","Q","U","X","Y","Z"]

    match userDomisili:
        case 1: kodePelat = random.choice(arrayYogyakarta)
        case 2: kodePelat = random.choice(arrayBantul)
        case 3: kodePelat = random.choice(arrayKulon)
        case 4: kodePelat = random.choice(arrayGunung)
        case 5: kodePelat = random.choice(arraySleman)
        
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    PelatHuruf2 = random.choice(alfabet)
    print(f"AB {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")


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
