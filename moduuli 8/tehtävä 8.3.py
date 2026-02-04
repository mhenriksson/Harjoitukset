from geopy import distance
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='bc555',
         autocommit=True
         )


def get_location_from_icao(icao1, icao2):
    sql = """
    SELECT ident, latitude_deg, longitude_deg
    FROM airport
    WHERE ident IN (%s, %s)
    """
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao1, icao2))
    results = kursori.fetchall()

    loc1 = loc2 = None

    for rivi in results:
        if rivi["ident"] == icao1:
            loc1 = (rivi["latitude_deg"], rivi["longitude_deg"])
        elif rivi["ident"] == icao2:
            loc2 = (rivi["latitude_deg"], rivi["longitude_deg"])

    return loc1, loc2

icao1 = input("Anna icao 1: ")
icao2 = input("Anna icao 2: ")
loc1, loc2 = get_location_from_icao(icao1, icao2)
print(loc1, loc2)

print(distance.distance(loc1, loc2).km)

