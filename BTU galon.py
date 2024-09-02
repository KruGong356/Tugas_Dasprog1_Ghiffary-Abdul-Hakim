# efisiensi tungku minyak
efisiensi = float(input("masukan efisiensi tungku minyak => "))

# jumlah minyak
galon = float(input("masukan jumlah galon yang akan dibakar => "))

# hasil BTU
jumlah_BTU = galon / 42 * 5800000 * (efisiensi / 100)
print(f"jumlah BTU yang dihasilkan => {jumlah_BTU:.3f} BTU")