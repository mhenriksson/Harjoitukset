sukupuoli = input("syötä sukupuoli: ").lower()

if sukupuoli == "nainen":
    hemog = float(input("Syötä hemoglobiiniarvo: "))
    if hemog >= 117 and hemog <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    elif hemog > 0 and hemog < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemog > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Tarkista syöttämäsi arvosi.")

elif sukupuoli == "mies":
    hemog = float(input("Syötä hemoglobiiniarvo: "))
    if hemog >=134 and hemog <= 195:
        print("Hemoglibiiniarvosi on normaali.")
    elif hemog > 0 and hemog < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemog > 195:
        print("Hemoglobiiniarvosi on korkea")
    else:
        print("Tarkista syöttämäsi arvosi.")
else:
    print("Tarkista syöttämäsi sukupuoli")