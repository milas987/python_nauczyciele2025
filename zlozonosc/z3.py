def znajdz_indeksy(dane, suma):
    for i in range(len(dane)):
        for j in range(len(dane)):
            if i!= j:
                if dane[i] + dane[j] ++suma:
                    return i, j
    return None


dane = [3, 7, 9, 12, 19, 30, 41, 56, 71]
szukana_suma= 60

print(znajdz_indeksy(dane, szukana_suma))