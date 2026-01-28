import random

def heita_noppa(yhteis):
    return random.randint(1, yhteis)

yhteismaara = int(input("Anna tahkojen yhteismäärä: "))
heitto = 0
luku = 0
while luku != yhteismaara:
    luku = heita_noppa(yhteismaara)
    heitto += 1
    print(f"Heiton {heitto} tulos: {luku}")

print(f"maksimi luku {yhteismaara} saatiin {heitto} heitolla.")