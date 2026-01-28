import math


def pizza_laskuri(halkaisija, hinta):
    halkaisija_m = halkaisija / 100

    sade_m = halkaisija_m / 2

    pinta_ala_m2 = math.pi * sade_m ** 2

    yksikkohinta = hinta / pinta_ala_m2

    return yksikkohinta

ha1 = float(input("anna halkaisija: "))
hi1 = float(input("anna hinta: "))
ha2 = float(input("anna halkaisija: "))
hi2 = float(input("anna hinta: "))
pizza1 = pizza_laskuri(ha1, hi1)
pizza2 = pizza_laskuri(ha2, hi2)

print(f"Pizza 1 yksikköhinta: {pizza1:.2f} €/m²")
print(f"Pizza 2 yksikköhinta: {pizza2:.2f} €/m²")

# Vertailu - pienempi yksikköhinta on parempi
if pizza1 < pizza2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif pizza2 < pizza1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat yhtä edullisia.")