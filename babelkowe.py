dane = [1, 6, 5, 8, 2, 7, 9 ]
n = len(dane)
for i in range (0, n-1):
    for j in range (0, n-1-i):
        if dane[j] > dane [j+1]:
            dane[j], dane[j+1]= dane[j+1], dane[j]
print (dane)