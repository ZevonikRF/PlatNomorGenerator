import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (Bandung Raya & Cimahi) & jenis kendaraan 

# Format : D XXXX dSS / D XXXX dS
# D : Daerah (otomatis D)
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
    arrayBandungKota = ["A","A","A","A","A","A","A","A","A","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]
    arrayCimahi = ["S","T"]
    arrayBandungBarat = ["U","X"]
    arrayBandungKab = ["V","Y","Z"]

    alfabet1BandungKota = ["A","B","C","D","E","F","G","H","I","J","K"]
    alfabet1Cimahi = ["A","B"]
    alfabet1BandungBarat1 = ["A","B","C","D","E","F"]
    alfabet1BandungBarat2 = ["G","H"]
    alfabet1BandungKab = ["B","C","D","E","F"]


    match userDomisili:
        case 1: kodePelat = random.choice(arrayBandungKota)
        case 2: kodePelat = random.choice(arrayCimahi)
        case 3: kodePelat = random.choice(arrayBandungBarat)
        case 4: kodePelat = random.choice(arrayBandungKab)
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    match kodePelat:
        case "A" : 
            PelatHuruf1 = random.choice(alfabet1BandungKota)
            PelatHuruf2 = random.choice(alfabet)
            print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
        case "S" :
            PelatHuruf1 = random.choice(alfabet1Cimahi)
            PelatHuruf2 = random.choice(alfabet)
            print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
        case "U" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet1BandungBarat1)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf1 = random.choice(alfabet1BandungBarat1)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case "V" : 
            PelatHuruf1 = random.choice(alfabet1BandungKab)
            PelatHuruf2 = random.choice(alfabet)
            print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
        case "X" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet1BandungBarat2)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf1 = random.choice(alfabet1BandungBarat2)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case "Y" | "Z" : 
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet1BandungKab)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf1 = random.choice(alfabet1BandungKab)
                PelatHuruf2 = random.choice(alfabet)
                print(f"D {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case _:
            PelatHuruf2 = random.choice(alfabet)
            print(f"D {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")


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
