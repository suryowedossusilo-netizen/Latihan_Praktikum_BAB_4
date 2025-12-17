teks = "Total pembayaran 25000 rupiah"

angka = ""
for char in teks:
    if char.isdigit():
        angka += char

print(angka)
