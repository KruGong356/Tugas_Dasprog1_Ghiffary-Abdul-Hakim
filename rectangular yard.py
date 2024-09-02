# panjang dan lebar halaman
Ph = float(input("masukan panjang halaman dalam kaki => "))
Lh   = float(input("masukan lebar halaman dalam kaki => "))

# panjang dan lebar rumah
kecepatan = 2
if Ph > Lh:
    Pr = float(input("masukan panjang rumah dalam kaki => "))
    Lr = float (input("masukan lebar rumah dalam kaki => "))
    if Pr > Lr:
            luas_h = Ph * Lh
            luas_r = Pr * Lr
            daerah_yg_dipotong = luas_h-luas_r
            waktu = daerah_yg_dipotong / kecepatan
            print(f"dibutuhkan {waktu} detik untuk memotong rumput halaman dengan luas {daerah_yg_dipotong} kaki persegi.")

    else:
            print("NOTE: Panjang halaman harus Lebih dari Lebar halaman ")
else:
    print("NOTE: Panjang rumah harus lebih dari Lebar rumah")