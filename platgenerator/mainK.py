import random
# from ..data.datadomisili import *
# from ..data.datatipekendaraan import *

# Program untuk men-generate pelat nomor berdasarkan domisili (Keresidenan Pati) & jenis kendaraan 

# Format : D XXXX SSd / D XXXX Sd
# D : Daerah (otomatis K)
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
    arrayPati = ["A","G","H","S","U"]
    arrayKudus = ["B","K","O","R","T"]
    arrayJepara = ["C","L","Q","V"]
    arrayRembang = ["D","I","M","W"]
    arrayBlora = ["E","N","Y"]
    arrayGrobongan = ["F","J","P","Z"]

    match userDomisili:
        case 1: kodePelat = random.choice(arrayPati)
        case 2: kodePelat = random.choice(arrayKudus)
        case 3: kodePelat = random.choice(arrayJepara)
        case 4: kodePelat = random.choice(arrayRembang)
        case 5: kodePelat = random.choice(arrayBlora)
        case 6: kodePelat = random.choice(arrayGrobongan)
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    match kodePelat:
        # Alfabet 1 untuk 3 abjad masih belum akurat; perlu data lagi, sementara pake semua alfabet
        case "A" | "B" | "C" | "D" | "E" | "F" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet)
                PelatHuruf2 = random.choice(alfabet)
                print(f"K {str(angkaAcak)} {PelatHuruf1}{PelatHuruf2}{kodePelat}")
            else:
                PelatHuruf2 = random.choice(alfabet)
                print(f"K {str(angkaAcak)}  {PelatHuruf2}{kodePelat}")
        case _:
            PelatHuruf2 = random.choice(alfabet)
            print(f"K {str(angkaAcak)}  {PelatHuruf2}{kodePelat}")


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
