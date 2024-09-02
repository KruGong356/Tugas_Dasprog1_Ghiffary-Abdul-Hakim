#odometer awal dan akhir
odometer_awal = float(input("odometer awal => "))
odometer_akhir = float(input("odometer akhir => "))

# mencari jarak dan tarif
total_jarak = odometer_akhir-odometer_awal
tarif = total_jarak*1.50
print(f"tarif anda adalah $ {tarif:.2f} total jarak => {total_jarak:.3f} mile")