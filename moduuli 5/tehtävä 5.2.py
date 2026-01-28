Luvut = []

print("Syötä lukuja, (Tyhjä rivi lopettaa ohjelman): ")

while True:
    syote = input("Anna Luku: ")
    if syote == "":
        break
    Luvut.append(float(syote))

Luvut.sort(reverse=True)

print("viisi suurinta: ")
for luku in Luvut[:5]:
    print(luku)
