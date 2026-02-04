import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='bc555',
         autocommit=True
         )


def get_airports_by_country(country):
    sql = "SELECT type, COUNT(*) AS airport_count FROM airport WHERE iso_country = %s GROUP BY type";
    kursori = yhteys.cursor()
    kursori.execute(sql, (country,))
    results = kursori.fetchall()
    print(f"LENTOKENTÄT {country}:")
    for rivi in results:
        print(f"{rivi[0]}: {rivi[1]}")


get_airports_by_country("FI")



