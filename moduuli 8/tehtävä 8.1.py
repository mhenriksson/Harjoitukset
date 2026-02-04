import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='bc555',
         autocommit=True
         )

def info_from_icao(icao):
     sql = "SELECT name, iso_country FROM airport WHERE ident = %s"
     kursori = yhteys.cursor(dictionary=True)
     kursori.execute(sql, (icao,))
     tulos = kursori.fetchone()
     return tulos

icao = input("Syötä ICAO: ")
tulos = info_from_icao(icao)
print(tulos)
