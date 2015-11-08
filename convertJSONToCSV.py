__author__ = 'Tian'

import json
import csv

filename = ""

f = open('flow11-02_10.json')
## Read the first line
line = f.readline()

# CSV table headers
headers = ['flow_item_id', 'sub_flow_item_id', 'description', 'length', 'speed_without_limit', 'free_flow_speed',
           'tmc_location_code', 'road_type', 'speed_with_limit', 'queuing_direction', 'confidence', 'jam_factor',
           'created_time_stamp',
           'base_time_stamp']

c = open("test_csv.csv", 'a', newline='')
try:
    writer = csv.writer(c)
    while line:

        data = json.loads(line)

        for k in range(len(data.RWS)):

            for j in range(len(data.RWS[k].RW)):
                flow_item_id =
                for l in range(len(data.RWS[k].RW[j].FIS)):

                    for i in range(len(data.RWS[k].RW[j].FIS[l].FI)):
                        row = []

                        coords = data.RWS[k].RW[j].FIS[l].FI[i].SHP[0].value[0];
                        speed = data.RWS[k].RW[j].FIS[l].FI[i].CF[0].SU;

        writer.writerow(headers)
        writer.writerow([5,3,"hello"])
        writer.writerow([2,'lol lol', 'hello,.js'])
finally:
    c.close()

# open CSV line
## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    data = json.loads(line)

    for k in range(len(data.RWS)):

        for j in range(len(data.RWS[k].RW)):

            for l in range(len(data.RWS[k].RW[j].FIS)):

                for i in range(len(data.RWS[k].RW[j].FIS[l].FI)):
                    var
                    coords = data.RWS[k].RW[j].FIS[l].FI[i].SHP[0].value[0];
                    var
                    speed = data.RWS[k].RW[j].FIS[l].FI[i].CF[0].SU;
                    addPolygon(convertCoords2LatLng(coords), speed);

    print
    line
    line = f.readline()
f.close()
