__author__ = 'Tian'

import sqlite3
import mysql.connector

cnx = mysql.connector.connect(user='akunapar_ani', password='ttt124!@#riceilovetianani', host='box1112.bluehost.com',
                              database='akunapar_riceai_traffic')

c = cnx.cursor()

c.execute('''CREATE TABLE flow_data
             (unique_collection_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
             flow_item_id TINYTEXT,
             sub_flow_item_id TINYTEXT,
             description TINYTEXT,
             length FLOAT,
             speed_without_limit FLOAT,
             free_flow_speed FLOAT,
             tmc_location_code TINYTEXT,
             road_type TINYTEXT,
             speed_with_limit FLOAT,
             queuing_direction CHAR(1),
             confidence FLOAT,
             jam_factor FLOAT,
             created_time_stamp DATETIME,
             base_time_stamp DATETIME,
             coords TEXT
             )''')

cnx.commit()

cnx.close()


# f = open("test_csv.csv")

# SQL lite connection
# conn = sqlite3.connect('flow.db')
# c = conn.cursor()
#
# c.execute('''CREATE TABLE flow_data
#              (unique_collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
#              flow_item_id TEXT,
#              sub_flow_item_id TEXT,
#              description TEXT,
#              length REAL,
#              speed_without_limit REAL,
#              free_flow_speed REAL,
#              tmc_location_code TEXT,
#              road_type TEXT,
#              speed_with_limit REAL,
#              queuing_direction CHARACTER(20),
#              confidence REAL,
#              jam_factor REAL,
#              created_time_stamp DATE,
#              base_time_stamp DATE,
#              coords TEXT
#              )''')
#
# conn.commit()
#
# conn.close()
