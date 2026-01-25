o_kayttaja = "Python"
o_salasana = "rules"

kayttaja = input("Käyttäjätunnus: ")
salasana = input("salasana: ")

if kayttaja == o_kayttaja and salasana == o_salasana:
    print("Tervetuloa.")
else:
    print("virheellinen käyttäjätunnus tai salasana.")

    yritykset = 1

    while yritykset < 5:
        kayttaja = input("Käyttäjätunnus: ")
        salasana = input("salasana: ")

        if kayttaja == o_kayttaja and salasana == o_salasana:
            print("Tervetuloa.")
            break
        else:
            yritykset += 1
            if yritykset < 5:
                print("virheellinen käyttäjätunnus tai salasana.")

    if yritykset == 5:
        print("Pääsy evätty.")
