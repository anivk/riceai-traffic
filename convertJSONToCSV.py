__author__ = 'Tian'

import json
import mysql.connector


def process_dir(dir):
    pass


def addFileToDB(filename):
    f = open(filename)

    ## Read the first line
    line = f.readline()

    # SQL lite connection
    conn = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani',
                                   host='box1112.bluehost.com',
                                   database='akunapar_riceai_traffic')
    c = conn.cursor()


    i = 0
    try:
        while line:

            data = json.loads(line)
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
                                    %s)""", row)

                            print (i)

                            i += 1

                            if i % 10000 == 0:
                                conn.commit()
            f.readline()  # skip one line
            line = f.readline()
    finally:
        conn.commit()
        conn.close()


addFileToDB("flow11-02_10.json")