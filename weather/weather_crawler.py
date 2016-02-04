import datetime
import requests
import json
import mysql.connector
import time as timer


def query_weather(segment_id, avg_lat, avg_lng, measurement_timestamp, db_connection):
    url = "https://api.forecast.io/forecast/eb5ea1930ce808a5c2be2aed1e4c88c7/{:f},{:f},{:%Y-%m-%dT%H:%M:%S}".format(
        avg_lat,
        avg_lng,
        measurement_timestamp)

    # Query the API for data
    page = requests.get(url)
    data = json.loads(page.content)["currently"]

    query = ("INSERT INTO weather "
             "(measurement_id, segment_id, measurement_timestamp, temperature, summary, precip_intensity, precip_probability, apparent_temp, dew_point, humidity, wind_speed, wind_bearing, visibility, pressure) "
             "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    # generate measurement_id
    key = segment_id + " " + measurement_timestamp.strftime("%Y-%m-%d %H:%M:%S")

    # add measurement to database
    c = db_connection.cursor()
    c.execute(query, (
        key, segment_id, measurement_timestamp, data["temperature"], data["summary"], data["precipIntensity"],
        data["precipProbability"], data["apparentTemperature"], data["dewPoint"], data["humidity"], data["windSpeed"],
        data["windBearing"], data["visibility"], data["pressure"]))
    c.close()
    db_connection.commit()


cnx1 = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                               database='akunapar_riceai_traffic')

cnx2 = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                               database='akunapar_riceai_traffic')

cursor = cnx2.cursor()
cursor.execute("SELECT speeds.segment_id, segment_info.avg_lat, segment_info.avg_lng, speeds.measurement_timestamp " +
               "FROM speeds, segment_info " + "WHERE speeds.segment_id = segment_info.segment_id")

for seg_id, avg_lat, avg_lng, measurement_timestamp in cursor:
    try:
        start = timer.time()
        query_weather(seg_id, avg_lat, avg_lng, measurement_timestamp, cnx1)
        print 'Sucessfully queried:', seg_id + " " + measurement_timestamp.strftime(
            "%Y-%m-%d %H:%M:%S"), "in", timer.time() - start
    except mysql.connector.errors.InterfaceError:
        print "Attempting to reconnect"
        cnx1 = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
           database='akunapar_riceai_traffic')
        continue
    except:
        print "Error at", seg_id + " " + measurement_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        continue

cnx1.commit()
cnx1.close()
cnx2.commit()
cnx2.close()
