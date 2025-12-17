with open("file1.txt", "r") as f1:
    isi_file1 = f1.read()

with open("file2.txt", "r") as f2:
    isi_file2 = f2.read()

with open("gabungan.txt", "w") as fg:
    fg.write(isi_file1)
    fg.write("\n")
    fg.write(isi_file2)

print("File berhasil digabungkan ke gabungan.txt")
