__author__ = 'Tian'

import json
from itertools import chain
import os
from glob import glob

import mysql.connector

buffer = []

def process_dir(dir):
    result = (chain.from_iterable(glob(os.path.join(x[0], '*.*')) for x in os.walk(dir)))

    for s in result:
        addFileToDB(s)
        print("Processed file: " + s)


def addFileToDB(filename):
    f = open(filename)

    ## Read the first line
    line = f.readline()

    while line:
        data = json.loads(line)
        addDataToDB(data)
        f.readline()  # skip one line
        line = f.readline()

def addDataToDB(data):
            created_time_stamp = data['CREATED_TIMESTAMP']

            for k in range(len(data['RWS'])):
                for j in range(len(data['RWS'][k]['RW'])):

                    flow_item_id = data['RWS'][k]['RW'][j]['LI']
                    base_time_stamp = data['RWS'][k]['RW'][j]['PBT']

                    for l in range(len(data['RWS'][k]['RW'][j]['FIS'])):
                        for i in range(len(data['RWS'][k]['RW'][j]['FIS'][l]['FI'])):
                            coords = data['RWS'][k]['RW'][j]['FIS'][l]['FI'][i]['SHP'][0]['value'][0]
                            TMC = data['RWS'][k]['RW'][j]['FIS'][l]['FI'][i]['TMC']
                            CF = data['RWS'][k]['RW'][j]['FIS'][l]['FI'][i]['CF'][0]

                            sub_flow_item_id = str(flow_item_id) + "_" + str(i)
                            description = TMC['DE']
                            length = TMC['LE']
                            free_flow_speed = CF['FF']
                            tmc_location_code = TMC['PC']
                            road_type = CF['TY']
                            speed_with_limit = CF['SP']
                            speed_without_limit = CF.get('SU', speed_with_limit)
                            queuing_direction = TMC['QD']
                            confidence = CF['CN']
                            jam_factor = CF['JF']


                            row = (
                            flow_item_id, sub_flow_item_id, description, float(length), float(speed_without_limit),
                            float(free_flow_speed),
                            tmc_location_code, road_type, float(speed_with_limit), queuing_direction,
                            float(confidence), float(jam_factor), created_time_stamp,
                            base_time_stamp.replace('T', ' ').replace('Z', ''), coords)

                            buffer.append(row)

                            if len(buffer)%100 == 0:
                                print( "Buffer processed" )
                                process_buffer()

                            #print (created_time_stamp + " " + sub_flow_item_id)

def process_buffer():
        # SQL lite connection
    conn = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani',
                                   host='box1112.bluehost.com',
                                   database='akunapar_riceai_traffic')

    try:
        c = conn.cursor()
        while len(buffer) != 0:
            c.execute("""INSERT INTO flow_data (
                                    flow_item_id,
                                    sub_flow_item_id,
                                    description,
                                    length,
                                    speed_without_limit,
                                    free_flow_speed,
                                    tmc_location_code,
                                    road_type,
                                    speed_with_limit,
                                    queuing_direction,
                                    confidence,
                                    jam_factor,
                                    created_time_stamp,
                                    base_time_stamp,
                                    coords)

                                    VALUES (
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s,
                                    %s)""", buffer.pop())

    except:
        print("INSERT ERROR")
    finally:
        conn.commit()
        conn.close()

indx = 0
process_dir('C:/Users/Tian/Desktop/flow10-31')
