import mysql.connector
import csv


def select_to_csv(select_query, filename):
    cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                               database='akunapar_riceai_traffic')

    cursor = cnx.cursor()
    cursor.execute(select_query)

    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerows(cursor)

    cursor.close()
    cnx.close()

select_to_csv('SELECT timestamp, speed FROM speeds WHERE segment_id="95-96" AND timestamp>="2014-01-01" AND timestamp<"2015-01-01"', "speed.csv")
select_to_csv('SELECT measurement_timestamp, precip_intensity FROM weather WHERE measurement_timestamp>"2015-01-01" AND measurement_timestamp<="2016" AND segment_id = "1247-1245"', "weather.csv")

