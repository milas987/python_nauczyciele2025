 def modyfikuj_liste(lista):
        wynik = []
        for i in range(len(lista)):
            if i % 2 == 0:  # indeks parzysty
                wynik.append(lista[i] * 2)
            else:  # indeks nieparzysty
                wynik.append(lista[i] / 2)
        return wynik



    # T(n)= 2n
    # O(n)= n