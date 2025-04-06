# alfabet = ""
# for i in range (ord('a'), ord('z')+1):
#     alfabet+=(chr(i))



alfabet= [chr(i) for i in range(ord ('a'), ord('z')+1)]

def szyfruj (napis, klucz):
    szyfr= [alfabet[(i+ klucz)% len (alfabet)] for i in range (len(alfabet))]
    print(szyfr)
def odszyfruj (napis, klucz):
    pass

if __name__== '__main__':
    napis = "ala ma kota"
    klucz = 3
    zaszyfrowany_napis = szyfruj(napis, klucz)
    print(zaszyfrowany_napis)

    odszyfrowany_napis = odszyfruj(zaszyfrowany_napis, klucz)
    print (odszyfrowany_napis)
