# Waktu yang sudah berlalu
jam = float(input("berapa jam yang telah berlalu sejak listrik padam? =>"))
menit = float(input("berapa menit yang telah berlalu sejak listrik padam? =>"))

# waktu ke jam desimal
T = jam + (menit / 60)

# Menghitung suhu
suhu = (4*(T ** 2) / (T + 2)) - 20
print(f"suhu di freezer kira-kira adalah {suhu:.3f} derajat Celcius")