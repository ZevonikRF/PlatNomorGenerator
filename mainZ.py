import random
import datadomisili
import datatipekendaraan

# Program untuk men-generate pelat nomor berdasarkan domisili (Sumedang dkk) & jenis kendaraan 

# Format : D XXXX dSS / D XXXX dS
# D : Daerah (otomatis Z)
# X : Angka Acak (tergantung tipe kendaraan)
# d : Domisili
# S : Huruf Acak

# def lihatDomisili():
#     for i in datadomisili.domisiliPrianganTimur:
#         print(i)

# def lihatTipeKendaraan():
#     for i in datatipekendaraan.tipeKendaraan:
#         print(i)

def generator(userDomisili, userTipe):
    alfabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    arraySumedang = ["A","B","C"]
    arrayGarut = ["D","E","F","G"]
    arrayTasik = ["H","I","J","K","L","M"]
    arrayTasikKab = ["N","O","P","Q","R","S"]
    arrayCiamis = ["T","V","W"]
    arrayPangandaran = ["U"]
    arrayBanjar = ["X","Y","Z"]

    alfabet1SumedangTasikCiamis = ["A"]
    alfabet1Garut = ["A","B","C","D","E","F"] 

    match userDomisili:
        case 1: kodePelat = random.choice(arraySumedang)
        case 2: kodePelat = random.choice(arrayGarut)
        case 3: kodePelat = random.choice(arrayTasik)
        case 4: kodePelat = random.choice(arrayTasikKab)
        case 5: kodePelat = random.choice(arrayCiamis)
        case 6: kodePelat = random.choice(arrayPangandaran)
        case 7: kodePelat = random.choice(arrayBanjar)
    
    match userTipe:
        case 1: angkaAcak = random.randint(2000,6999)
        case 2: angkaAcak = random.randint(1000,1999)
        case 3 | 4: angkaAcak = random.randint(7000,7999)
        case 5: angkaAcak = random.randint(8000,9999)
    
    match kodePelat:
        case "A" | "H" |"T" : 
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet1SumedangTasikCiamis)
                PelatHuruf2 = random.choice(alfabet)
                print(f"Z {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf2 = random.choice(alfabet)
                print(f"Z {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case "D" | "G" :
            angkaNentuinBelakang = random.randint(1,2)
            if angkaNentuinBelakang == 1:
                PelatHuruf1 = random.choice(alfabet1Garut)
                PelatHuruf2 = random.choice(alfabet)
                print(f"Z {str(angkaAcak)} {kodePelat}{PelatHuruf1}{PelatHuruf2}")
            else:
                PelatHuruf2 = random.choice(alfabet)
                print(f"Z {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")
        case _:
            PelatHuruf2 = random.choice(alfabet)
            print(f"Z {str(angkaAcak)}  {kodePelat}{PelatHuruf2}")


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
