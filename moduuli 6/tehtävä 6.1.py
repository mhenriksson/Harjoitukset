import random

def heita_noppa():
    return random.randint(1, 6)
heitto = 0
luku = 0
while luku != 6:
    luku = heita_noppa()
    heitto += 1
    print(f"Heiton {heitto} tulos: {luku}")

print(f"Kuutonen saatiin {heitto} heitolla.")