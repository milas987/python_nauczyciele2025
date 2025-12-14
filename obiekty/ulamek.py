class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def czy_calkowita(self):
        return self.licznik % self.mianownik == 0

    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

def porownaj(a: Ulamek, b: Ulamek):
    wartosc_a = float(a)
    wartosc_b = float(b)
    if wartosc_a < wartosc_b: return -1
    elif wartosc_a == wartosc_b: return 0
    else: return 1

if __name__ == '__main__':
    u = Ulamek(2,3)
    print(float(u))
    print(porownaj(Ulamek(2, 3), Ulamek(3,4)))