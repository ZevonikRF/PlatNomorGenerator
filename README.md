# Indonesian License Plate Generator
### Generator Pelat Nomor Indonesia

Ini adalah program python sederhana untunk mengenerate pelat nomor kendaraan sesuai ketentuan Peraturan Kapolri Nomor 7 Tahun 2021.

Program dijalankan melalui GUI.

Data wilayah yang ditambahkan ke program ini (Pulau Jawa):
| Kode | Cakupan |
| ------ | ------ |
|A| <ul><li>**Kota Serang** (Ax/Bx/Cx/Dx)</li><li>**Kab. Serang** (Ex/Fx/Gx/Hx/Ix)</li><li>**Kab. Pandeglang** (Jx/Kx/Lx/Mx)</li><li>**Kab. Lebak** (Nx/Ox/Px/Qx)</li><li>**Kota Cilegon** (Rx/Sx/Tx/Ux)</li><li>**Kab. Tangerang (Balaraja)** (Vx/Wxx/Xxx/Yx/Zx)</li></ul>|
|AA|Soon|
|AB|Soon|
|AD|Soon|
|B| <ul><li>**Jakarta** (Bxx/Dxx/Hxx/Pxx/Rxx/Sxx/Txx/Uxx)</li><li>**Kota Depok** (Exx/Zxx)</li><li>**Kota Tangerang** (Cxx/Vxx)</li><li>**Kota Tangerang Selatan** (Nxx/Wxx)</li><li>**Kab. Tangerang (Kelapa Dua)** (Jxx)</li><li>**Kota Bekasi** (Kxx)</li><li>**Kab. Bekasi** (Fxx)</li></ul> |
|D| <ul><li>**Kota Bandung** (Axx/Bx/Cx/Dx/Ex/Fx/Gx/Hx/Ix/Jx/Kx/Lx/Mx/Nx/Ox/Px/Qx/Rx)</li><li>**Kab. Bandung** (Vxx/Yxx/Zxx),</li><li>**Kab. Bandung Barat** (Uxx/Xxx)</li><li>**Kota Cimahi** (Sxx/Tx)</li></ul> |
|E| <ul><li>**Kota Cirebon** (Ax/Bxx/Cx/Dx/Ex/Fx/Gx)</li><li>**Kab. Cirebon** (Hxx/Ix/Jx/Kx/Lx/Mxx/Nx/Ox)</li><li>**Kab. Indramayu** (Px/Qx/Rx/Sx/Tx)</li><li>**Kab. Majalengka** (Uxz/Vx/Wx/Xx)</li><li>**Kab. Kuningan** (Yxx/Zxx)</li></ul>|
|F| <ul><li>**Kota Bogor** (Axx/Bx/Cx/Dx/Ex)</li><li>**Kab. Bogor** (Fxx/Gx/Hx/Ix/Jx/Kx/Lx/Mx/Nx/Px/Rx)</li><li>**Kota Sukabumi** (Ox/Sx/Txx)</li><li>**Kab. Sukabumi** (Qxx/Ux/Vx)</li><li>**Kab. Cianjur** (Wxx/Xx/Yx/Zx)</li></ul>|
|G| <ul><li>**Kota Pekalomngan** (xA/xH/xS)</li><li>**Kab. Pekalongan** (xxB/xK/xO/xT)</li><li>**Kab. Batang** (xxC/xL/xV)</li><li>**Kab. Pemalang** (xxD/xI/xM/xW)</li><li>**Kota Tegal** (xxE/xN/xY)</li><li>**Kab. Tegal** (xxF/xP/xQ/xZ)</li><li>**Kab. Brebes** (xxG/xJ/xR/xU)</li></ul>|
|H| <ul><li>**Kota Semarang** (xxA/xF/xxG/xH/xP/xQ/xR/xS/xxW/xY/xZ)</li><li>**Kab. Semarang** (xxC/xI/xL/xV)</li><li>**Kota Salatiga** (xxB/xK/xO/xT)</li><li>**Kab. Kendal** (xxD/xM/xU)</li><li>**Kab. Demak** (xxE/xJ/xN)</li></ul>|
|K| <ul><li>**Kab. Pati** (xxA/xG/xH/xS/xU)</li><li>**Kab. Kudus** (xxB/xK/xO/xR/xT)</li><li>**Kab. Jepara** (xxC/xL/xQ/xV)</li><li>**Kab. Rembang** (xxD/xI/xM/xW)</li><li>**Kab. Blora** (xxE/xN/xY)</li><li>**Kab. Grobogan** (xxF/xJ/xP/xZ)</li></ul>|
|R|Soon|
|T| <ul><li>**Kab. Purwakarta** (Ax/Bx/Cx/Ix/Jx)</li><li>**Kab. Karawang** (Dx/Ex/Fx/Gx/Hx/Kx/Lx/Mx/Nx/Ox/Px/Qx/Rx/Sx)</li><li>**Kab. Subang** (Tx/Ux/Vx/Wx/Xx/Yx/Zx)</li></ul>|
|Z| <ul><li>**Kota Sumedang** (Axx/Bx/Cx)</li><li>**Kota Garut** (Dxx/Ex/Fx/Gx)</li><li>**Kota Tasikmalaya** (Hxx/Ix/Jx/Kx/Lx/Mx)</li><li>**Kab. Tasikmalaya** (Nx/Ox/Px/Qx/Rx/Sx)</li><li>**Kab. Ciamis** (Txx/Vx/Wx)</li><li>**Kab. Pangandaran** (Ux)</li><li>**Kota Banjar** (Xx/Yx/Zx)</li></ul> |

*berdasarkan Source: [Wikipedia](https://id.wikipedia.org/wiki/Tanda_Nomor_Kendaraan_Bermotor_Indonesia), [Samsat](https://samsat.info/daftar-lengkap-kode-plat-nomor-polisi-kendaraan-daerah-di-indonesia), [Dokumen Perpol](https://peraturan.bpk.go.id/Details/225016/perpol-no-7-tahun-2021)

### To Be Added/Worked
- Executable GUI (Preq. Pulau Jawa + Madura selesai)
- Re-adjust README (Preq. Pulau Jawa + Madura selesai)
- Kode S (Bojonegoro, Mojokerto, Lamongan, dsb)
- Kode W (Gresik, Sidoarjo)