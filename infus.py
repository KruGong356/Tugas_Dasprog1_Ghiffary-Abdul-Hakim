# input untuk infus
volume = float(input("jumlah volume yang akan diinfuskan => "))
menit = float(input(" jumlah menit menginfus => "))

# Konversi menit ke jam
jam = menit / 60

# laju infus
laju = volume / jam

# hasil
print(f"VTBI => {volume:.2f} ml")
print(f"Rate => {laju:.2f} ml/jam")

