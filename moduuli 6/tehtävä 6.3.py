def galloinatlitroiksi(g):
    return g * 3.785
while True:
    g = float(input("Anna bensiinin määrä[Gallonaa]: "))
    if g <0:
        print("Virheellinen lukumäärä.")
        break
    l = galloinatlitroiksi(g)
    print(f"{g} Gallonaa on {l:.3f} litraa.")
