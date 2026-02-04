nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Nimi syötetti aikaisemmin...")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
print("Syötetyt nimet: ")
for n in nimet:
    print(n)
