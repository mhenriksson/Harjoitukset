import random

oikee = random.randint(1,10)
veikkaus = int(input("Veikkaa luku: "))

while veikkaus != oikee:
    if veikkaus <oikee:
        print("Liian pieni luku")
    else:
        print("Liian suuri luku")

    veikkaus = int(input("Veikkaa luku: "))

print("Oikea veikkaus!!")