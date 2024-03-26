def anagram(a,b):
    if len(a) != len(b):
        return False
    tampung = a[::-1]
    return sorted(tampung) == sorted(b)

a = str(input("Masukkan Kata 1:")).lower()
b = str(input("Masukkan Kata 2:")).lower()
if anagram(a,b):
    print('Anagram')
else:
    print('Tidak Anagram')
