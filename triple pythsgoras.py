# input
m = int(input("masukan nilai (bilangan bulat) m => "))
n = int(input("masukan nilai (bilangan bulat) n => "))

# perhitungan
if m > n:
    sisi_1 = (m ** 2) - (n ** 2)
    sisi_2 = 2 * m * n
    sisi_miring = (m ** 2) + (n ** 2)
    print(f"triple pythagorasnya adalah => {sisi_1}, {sisi_2}, dan {sisi_miring}")
    
else:
    print("(NOTE: nilai m harus lebih besar dari nilai n)")
