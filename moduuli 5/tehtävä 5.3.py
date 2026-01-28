num = int(input("Anna kokonaisluku: "))
if num < 2:
    print("Luku ei ole alkuluku.")
else:
    alk = True
    for i in range(2, num):
        if num % i == 0:
            alk = False
            break
    if alk:
        print(f" {num} On alkuluku.")
    else:
        print(f"{num} ei ole alkuluku.")