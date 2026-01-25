n = 0
luku = input("Anna luku: ")

while luku != "":
    numro = int(luku)

    if n  == 0:
        pienin = numro
        suurin = numro
    else:
        if numro < pienin:
            pienin = numro
        if numro > suurin:
            suurin = numro
    n = n + 1
    luku = input("Anna luku: ")

if n > 0:
    print("pienin: " + str(pienin))
    print("suurin: "+ str(suurin))
