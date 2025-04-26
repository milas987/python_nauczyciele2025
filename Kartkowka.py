import random

alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alfabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + list("ąćęłóśźż")
alfabet= "aąbcćdeęfghijklłmnopqrsśtuvwxyzźż"
random.shuffle(alfabet)
print(alfabet)



def odszyfruj(napis, klucz):
    zaszyfrowany_napis = "eax toćę ksbax khlwex, fhsmws"
    szyfr = [alfabet[(i + klucz) % len(alfabet)] for i in range(len(alfabet))]
    wynik = ""
    for znak in napis:

        if znak in alfabet:

            zaszyfrowany_znak = alfabet[szyfr.index(znak)]
            wynik += zaszyfrowany_znak
        else:
            wynik += znak
    return wynik



    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    print(odszyfrowany_napis)