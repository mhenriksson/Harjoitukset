Kuukausi = int(input("Anna kuukauden numero (1-12):"))
kaudet = ("Talvi", "Kevät", "Kesä", "Syksy")
ind = (Kuukausi % 12) // 3

print(kaudet[ind])