def porownaj_napisy(napis1, napis2):
    najkrotsza_dlugosc= min(len(napis1), len(napis2))
    for in range(najkrotsza_dlugosc):
        if len(napis1) = len(napis2):
            return-(i+1)
        elif napis1[i] > napis2[i]:
            return i+1
        else:
            return najkrotsza_dlugosc
if__name__=='__main__':
    print(porownaj_napisy(napis1"Ala ma kota", napis2"Ala nie ma kota"))
    print(porownaj_napisy(napis1"Ala ma kota", napis2"ala ma kota"))
    print(porownaj_napisy(napis1"Ala ma kota", napis2"Ala ma kota"))
    print(porownaj_napisy(napis1"Ala ma kota", napis2"Ala ma kota"))