import requests
from lxml import html
import datetime
import mysql.connector
import time as timer


cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani',
                                  host='box1112.bluehost.com',
                                  database='akunapar_riceai_traffic')

def crawl_sensor_for_date(date, key):
    url = 'http://www.harriscountyfws.org/GageDetail/Index/' + str(key) \
            +'?From='+ date.strftime("%m/%d/%Y %I:%M:%S %p") + '&span=1&unit=dd'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    number_of_water_level_readings = 0


    cursor = cnx.cursor()
    while True:
        sensor_reading = tree.xpath('//tr[@id="StreamElevationCumulativeGridView_DXDataRow' + str(number_of_water_level_readings) + '"]')
        if len(sensor_reading) == 0:
            break
        else:
            reading_datetime = sensor_reading[0][1].text
            reading_datetime = datetime.datetime.strptime(reading_datetime, "%m/%d/%Y %I:%M %p")
            reading_datetime = reading_datetime.strftime("%Y-%m-%d %H:%M:%S")
            elevation = sensor_reading[0][2].text[:-1]

            measurement_id = str(key) + " " + reading_datetime
            sensor_id = str(key)
            measurement_timestamp = reading_datetime
            stream_elevation = elevation

            sql = 'INSERT INTO flood_sensors VALUES ("{}",{},"{}",{})'.format(measurement_id, sensor_id, measurement_timestamp, stream_elevation)
            try:
                cursor.execute(sql)
            except:
                print "ERROR:", measurement_id
        number_of_water_level_readings += 1
    cnx.commit()
    cursor.close()

keys_to_query =
start_date = datetime.datetime.strptime("1/1/2014","%m/%d/%Y")
for i in range(365*2):
    start = timer.time()
    start_date += datetime.timedelta(days=1)
    crawl_sensor_for_date(start_date,570)
    print start_date.strftime("%Y-%m-%d %H:%M:%S"), timer.time() - start

cnx.close()