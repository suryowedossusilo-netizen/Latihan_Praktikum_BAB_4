import string

teks = "Halo!!! Apa kabar???"

hasil = ""
for char in teks:
    if char not in string.punctuation:
        hasil += char

print(hasil)
