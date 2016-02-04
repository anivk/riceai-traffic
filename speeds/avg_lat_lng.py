import mysql.connector

def calc_avg_latlng(segment_id, db_connection):
    c = db_connection.cursor()
    select_query = "SELECT lat, lng FROM segment_info WHERE segment_id = %s"

    c.execute(select_query, (segment_id,))

    update_query = "UPDATE segment_info SET avg_lat = %s, avg_lng = %s WHERE segment_id = %s"

    for lat, lng in c:
        lat = [float(x) for x in lat.split(' ')]
        lng = [float(x) for x in lng.split(' ')]
        avg_lat = sum(lat)/len(lat)
        avg_lng = sum(lng)/len(lng)
        c.execute(update_query, (avg_lat, avg_lng, segment_id))

    c.close()
    cnx.commit()


cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                              database='akunapar_riceai_traffic')

cursor = cnx.cursor()
cursor.execute("SELECT segment_id FROM segment_info")
ids = list(cursor)
cursor.close()

for segment_id in ids:
    calc_avg_latlng(segment_id[0], cnx)
    print "Updated:", segment_id


cnx.close()

