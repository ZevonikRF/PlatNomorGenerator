from tkinter import *
import io
import sys

import mainB
import mainD
import datadomisili
import datatipekendaraan

# Program untuk menampilkan antarmuka GUI 

layar = Tk()

layar.geometry("800x400")
layar.title("Pelat Nomor Generator")

dataDomisiliMeta = {
    "B - JABODETABEK": datadomisili.domisiliJakarta,
    "D - Bandung Raya dan Cimahi": datadomisili.domisiliBandungRaya
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
        tipeKendaraanIndeks = datatipekendaraan.tipeKendaraan.index(tipe) + 1
        output = io.StringIO()
        sys.stdout = output

        match daerah:
            case "B - JABODETABEK":
                mainB.generator(domisiliIndeks, tipeKendaraanIndeks)
            case "D - Bandung Raya dan Cimahi":
                mainD.generator(domisiliIndeks, tipeKendaraanIndeks)

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

opsiTipeKendaraan = datatipekendaraan.tipeKendaraan
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