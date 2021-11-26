a = input("Masukan kalimat untuk nanti dihitung: ")
def hitung(a):

    count = len(a) - a.count(" ")
    pembulatan= count * 2/3
    return pembulatan

print(hitung(a))