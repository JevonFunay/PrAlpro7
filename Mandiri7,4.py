def panjangpendek(kalimat):
    temp_kalimat = kalimat.split()
    kata_pendek= temp_kalimat[0]
    kata_panjang = temp_kalimat[0]
    for kata in temp_kalimat:
        if len(kata) > len(kata_panjang):
            kata_panjang = kata
        if len(kata) < len(kata_pendek):
            kata_pendek = kata
    return kata_pendek, kata_panjang
    
kalimat = input("Masukkan kata anda: ")
kata_panjang, kata_pendek = panjangpendek(kalimat)
print(kata_panjang)
print(kata_pendek)
    