from tkinter import *
import io
import sys
sys.path.append(".")

import platgenerator.mainB , platgenerator.mainD, platgenerator.mainZ , data.datadomisili, data.datatipekendaraan 

# Program untuk menampilkan antarmuka GUI 

layar = Tk()

layar.geometry("330x280")
layar.title("Pelat Nomor Generator")

dataDomisiliMeta = {
    "B - Jabodetabek": data.datadomisili.domisiliJakarta,
    "D - Bandung Raya dan Cimahi": data.datadomisili.domisiliBandungRaya,
    "Z - Priangan Timur": data.datadomisili.domisiliPrianganTimur,
}

#########################################################################################################
def updateDomisili(*args):
    pilihan = clickDaerah.get()
    menu = dropdownDomisili["menu"]
    menu.delete(0,"end")

    if pilihan in dataDomisiliMeta:
        for dom in dataDomisiliMeta[pilihan]:
            menu.add_command(label=dom, command=lambda value=dom: clickedDomisili.set(value))
        clickedDomisili.set(dataDomisiliMeta[pilihan][0])
    else:
        clickedDomisili.set("Pilih Domisili") 
#########################################################################################################
def generatePelat():
    daerah = clickDaerah.get()
    domisili = clickedDomisili.get()
    tipe = clickedTipeKendaraan.get()

    if daerah not in dataDomisiliMeta or domisili not in dataDomisiliMeta[daerah]:
        hasilLabel.config(text="Pilih domisili yang sesuai!")
        return
    try:
        domisiliIndeks = dataDomisiliMeta[daerah].index(domisili) + 1
        tipeKendaraanIndeks = data.datatipekendaraan.tipeKendaraan.index(tipe) + 1
        output = io.StringIO()
        sys.stdout = output

        match daerah:
            case "B - Jabodetabek":
                platgenerator.mainB.generator(domisiliIndeks, tipeKendaraanIndeks)
            case "D - Bandung Raya dan Cimahi":
                platgenerator.mainD.generator(domisiliIndeks, tipeKendaraanIndeks)
            case "Z - Priangan Timur":
                platgenerator.mainZ.generator(domisiliIndeks, tipeKendaraanIndeks)

        sys.stdout = sys.__stdout__
        hasil = output.getvalue().strip()
        hasilLabel.config(text=hasil)
    except Exception as e:
        hasilLabel.config(text=f"Error: {e}")
#########################################################################################################

Label(layar, text="Pilih Daerah").pack()
clickDaerah = StringVar()
clickDaerah.set("Pilih Daerah")
dropdownDaerah = OptionMenu(layar,clickDaerah,*dataDomisiliMeta.keys())
dropdownDaerah.pack()

Label(layar, text="Pilih Domisili").pack()
clickedDomisili = StringVar()
clickedDomisili.set("Pilih Domisili")
dropdownDomisili = OptionMenu(layar,clickedDomisili,"")
dropdownDomisili.pack()

clickDaerah.trace("w", updateDomisili)

opsiTipeKendaraan = data.datatipekendaraan.tipeKendaraan
Label(layar, text="Pilih Tipe Kendaraan").pack()
clickedTipeKendaraan = StringVar()
clickedTipeKendaraan.set("Pilih Tipe Kendaraan")
dropdownKendaraan = OptionMenu(layar,clickedTipeKendaraan,*opsiTipeKendaraan)
dropdownKendaraan.pack()

tombol = Button(layar,text="Generate Pelat Nomor", command=generatePelat)
tombol.pack()

hasilLabel = Label(layar, text="", font=("Courier", 30))
hasilLabel.pack(pady=10)

layar.mainloop()