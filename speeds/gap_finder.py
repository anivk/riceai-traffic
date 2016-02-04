import mysql.connector

id = "94-95"

cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                              database='akunapar_riceai_traffic')


c = cnx.cursor()
c.execute('SELECT timestamp FROM speeds WHERE segment_id = "94-95" ORDER BY timestamp')

gaps = []
prev_time = None
for timestamp, in c:
    if prev_time is None:
        prev_time = timestamp
    # print str(timestamp-prev_time) = "0:15:00"
    if str(timestamp-prev_time) != "0:15:00":
        gaps.append(timestamp)
    prev_time = timestamp

print len(gaps)
for i in range(len(gaps)-1):
    print gaps[i] -gaps[i+1]