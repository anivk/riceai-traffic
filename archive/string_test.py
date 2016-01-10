__author__ = 'Tian'

print ("""LOAD DATA LOW_PRIORITY LOCAL INFILE '"""+ "Hello.txt" + """'
            INTO TABLE `akunapar_riceai_traffic`.`flow_data1`
            FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\\n'
            (`flow_item_id`, `sub_flow_item_id`, `description`, `length`, `speed_without_limit`, `free_flow_speed`, `tmc_location_code`, `road_type`, `speed_with_limit`, `queuing_direction`, `confidence`, `jam_factor`, `created_time_stamp`, `base_time_stamp`, `coords`);""")
