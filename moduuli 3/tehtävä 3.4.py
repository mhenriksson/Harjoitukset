vuosi = int(input("Kerro vuosiluku: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"vuosi {vuosi} on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi")
