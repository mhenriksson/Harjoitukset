import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='bc555',
         autocommit=True
         )

def uusi_lentokentta(icao, nimi):
    sql = "INSERT INTO airport (ident, name) VALUES (%s, %s)"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao, nimi))
    tulos = f"UUSI LENTOKENTTÄ {name} LISÄTTY"
    return tulos

def icao_search(icao):
    sql = "SELECT * FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    return tulos

i = 0

while i  == 0:
    valinta = int(input("valitse toiminta (1-3): 1. LISÄÄ LENTOKENTTÄ 2. HAE LENTOKENTTÄ 3. LOPETA:   "))
    if valinta == 1:
        name = input("LENTOKENTÄN NIMI: ")
        icao = input("LENTOKENTÄN ICAO: ")
        ul = uusi_lentokentta(icao, name)
        print(ul)
    elif valinta == 2:
        icao = input("SYÖTÄ LENTOKENTÄN ICAO TUNNUS: ")
        it = icao_search(icao)
        print(it)
    elif valinta == 3:
        print("Lopetetaan ohjelma...")
        i = 1
