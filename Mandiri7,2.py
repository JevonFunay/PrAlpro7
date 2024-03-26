kata = input("Masukkan Kata: ").lower()
ditanya = input("Masukkan kata yang DITANYA: ").lower()
displit = kata.split()
jumlah = 0
for kata in displit:
    if kata == ditanya:
        jumlah += 1
print(jumlah)