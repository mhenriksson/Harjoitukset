import random

määrä = int(input("Kuinka monta kertaa heitetään?: "))

summa = 0
for i in range(määrä):
    noppa = random.randint(1,6)
    summa += noppa

print(summa)
