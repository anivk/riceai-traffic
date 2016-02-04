import datetime
import requests
from lxml import html
import mysql.connector
import time as timer
import sys

"""
3 arguments:
1) segment_id
2) start datetime i.e. 2015-12-16 12:59:00
3) end datetime
"""

cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                              database='akunapar_riceai_traffic')

add_measurement = ("INSERT INTO speeds "
              "(measurement_id, speed, timestamp, measurement_timestamp, segment_id) "
              "VALUES (%s, %s, %s, %s, %s)")



key = sys.argv[1]
print key
start_datetime = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d %H:%M:%S")#datetime.datetime(2015, 12,01, 00, 00)
end_datetime = datetime.datetime.strptime(sys.argv[3],  "%Y-%m-%d %H:%M:%S")


c = cnx.cursor()
c.execute('SELECT max(timestamp) FROM speeds WHERE segment_id = "{}"'.format(key))
results = c.fetchall()

print
if results[0][0] is not None:
    current_datetime = results[0][0]
else:
    current_datetime = start_datetime


while current_datetime <= end_datetime:

    timer_start = timer.time()

    current_datetime += datetime.timedelta(minutes=15)

    url = "http://traffic.houstontranstar.org/map_archive/getspeed_maparchive.aspx?src=/map_archive_data_share/{}/{}/{}/xml/speeds/{:0>2d}{:0>2d}{:0>2d}{:0>2d}&segment={}".format(
        current_datetime.year, current_datetime.month, current_datetime.day, current_datetime.month,
        current_datetime.day, current_datetime.hour, current_datetime.minute, key)

    try:
        #download page
        page = requests.get(url)
        tree = html.fromstring(page.content)

        measurement_timestamp = tree.xpath('//span[@id="lblDataAge"]/text()')[0]
        measurement_timestamp = datetime.datetime.strptime(measurement_timestamp,
                                                "%A, %B %d, %Y %I:%M %p").strftime("%Y-%m-%d %H:%M:%S")

        speed = tree.xpath('//span[@id="lblSpeed"]/text()')
        speed = int(speed[0][:speed[0].find(" ")])

        c = cnx.cursor()
        c.execute(add_measurement, (key + " " + current_datetime.strftime("%Y-%m-%d %H:%M:%S"), speed, current_datetime, measurement_timestamp, key))
        c.close()
        cnx.commit()

        print "INSERTED:", str(timer.time()-timer_start) + "s" , (key + " " + current_datetime.strftime("%Y-%m-%d %H:%M:%S"), speed, current_datetime, measurement_timestamp, key)
    except:
        print "ERROR", url

cnx.close()
