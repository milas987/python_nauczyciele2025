dane = [1, 6, 5, 8, 2]
n = len(dane)

for i in range (1,n):
    aktualny=dane[i]
    for j in range (0, i):
        if aktualny <dane [j]:
            dane.pop(i)
            dane.insert(j, aktualny)
            break
print(dane)
