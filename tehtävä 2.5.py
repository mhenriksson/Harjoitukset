leiviska = float(input("Anna Leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

naulat = leiviska * 20 + naula
luodit = naulat * 32 + luoti
gramma = luodit * 13.3
kg = int(gramma / 1000)
g = gramma % 1000

print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja {g:.2f} grammaa. ")
