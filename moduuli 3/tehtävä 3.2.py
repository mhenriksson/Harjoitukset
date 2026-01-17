Hyttiluokka = input ("Anna laivan hyttiluokka (LUX, A, B, C): ")

if Hyttiluokka == "LUX":
    print("Lux on parvekkeellinen hytti yläkannella.")
elif Hyttiluokka == "A":
    print("A on ikkunallinen hytti autokanna yläpuolella.")
elif Hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif Hyttiluokka == "C":
    print("C on ikkunaton hytti autokannan alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
