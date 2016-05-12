from pymongo import MongoClient
from bson.objectid import ObjectId
import mysql.connector

cnx = mysql.connector.connect(user='root', host='localhost', database='test')

add_measurement = (r"INSERT INTO 'test'.'flow' ('flow_id', 'coords', 'lenght', 'desc', 'queuing_direction', " \
                  r"'confidence', 'speed_with_limit', 'speed_without_limit', 'jam_factor', 'road_type', " \
                  r"'free_flow_speed', 'created_timestamp', 'base_timestamp') "
                   r"VALUES ('', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s')")

client = MongoClient('localhost', 27017)
db = client['traffic']
flow = db['flow']

def add_document(document, cursor):
    created_timestamp = document['CREATED_TIMESTAMP']
    for i in range(len(document['RWS'])):
        for j in range(len(document['RWS'][i]['RW'])):
            base_timestamp = document['RWS'][i]['RW'][j]['PBT']
            for k in range(len(document['RWS'][i]['RW'][j]['FIS'])):
                for l in range(len(document['RWS'][i]['RW'][j]['FIS'][k]['FI'])):
                    FI = document['RWS'][i]['RW'][j]['FIS'][k]['FI'][l]

                    coords = FI['SHP'][0]['value'][0]
                    lenght = FI['TMC']['LE']
                    desc =  FI['TMC']['DE']
                    queuing_direction = FI['TMC']['QD']
                    confidence = FI['CF'][0]['CN']
                    speed_with_limit = FI['CF'][0]['SP']
                    speed_without_limit = FI['CF'][0]['SU']
                    jam_factor = FI['CF'][0]['JF']
                    road_type = FI['CF'][0]['TY']
                    free_flow_speed = FI['CF'][0]['FF']

                    print created_timestamp, base_timestamp

x = flow.find_one({'added': {'$ne': True}})
# print x['RWS'][0]['RW'][0]['PBT']
add_document(x, None)
# object_id = ObjectId(x['_id'])
#
# y = flow.update_one(filter={'_id': object_id}, update={'$set': {'added': True}})
# print y.modified_count





