from collections import defaultdict 
import json
import os
import urllib2
import time
import datetime

global URL
URL = "https://traffic.api.here.com/traffic/6.1/flow.json?app_code=djPZyynKsbTjIUDOBcHZ2g&app_id=xWVIueSv6JL0aJ5xqTxb&bbox=30.16524,-95.96463;29.47547,-94.87398&i18n=true&jsoncallback=angular.callbacks._3&lg=en&responseattributes=simplifiedShape&units=metric"
incidentURL = "https://traffic.api.here.com/traffic/6.1/incidents.json?app_code=djPZyynKsbTjIUDOBcHZ2g&app_id=xWVIueSv6JL0aJ5xqTxb&bbox=30.16524,-95.96463;29.47547,-94.87398&i18n=true&jsoncallback=angular.callbacks._3&lg=en&responseattributes=simplifiedShape&units=metric"


def retrieve_data(url):

	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()

    # Omit the first several letters not in json form
	result_object = json.loads( the_page[21:-1])

	return result_object


def convert_time_trafficflow(timestring):
    """
    Input:
    flowtimestampstring

    Output:
    timestring that is deducted 5 hours to houston time
    """
    year = int(timestring[:4])
    month = int(timestring[5]) * 10 + int(timestring[6])
    day = int(timestring[8]) * 10 + int(timestring[9])
    hour = int(timestring[11]) * 10 + int(timestring[12])
    minute = int(timestring[14]) * 10 + int(timestring[15])
    second = int(timestring[17]) * 10 + int(timestring[18])

    d = datetime.datetime(year, month, day, hour, minute, second)
    return str(d - datetime.timedelta(hours = 5))

# TEST
#print convert_time_trafficflow("2015-06-30T03:14:16.000+0000")


def convert_time_trafficincident(timestring):
    """
    Input:
    flowtimestampstring

    Output:
    timestring that is deducted 5 hours to houston time
    """
    year = int(timestring[6:10])
    month = int(timestring[0]) * 10 + int(timestring[1])
    day = int(timestring[3]) * 10 + int(timestring[4])
    hour = int(timestring[11]) * 10 + int(timestring[12])
    minute = int(timestring[14]) * 10 + int(timestring[15])
    second = int(timestring[17]) * 10 + int(timestring[18])

    d = datetime.datetime(year, month, day, hour, minute, second)
    return str(d - datetime.timedelta(hours = 5))


# test
#print convert_time_trafficincident('07/07/2015 20:19:36 GMT')



def store_data():

    get_incident = True
    get_flow = True
    # incident api has a frequency of 2 min and 4 min alternatively so storing incident api data is relatively complicated
    last_time = time.time()
    b = retrieve_data(incidentURL)
    last_time_incident = time.time()
    b["TIMESTAMP"] = convert_time_trafficincident(b['TIMESTAMP'])
    incident_last_time_stamp = b["TIMESTAMP"]
    print "incident",incident_last_time_stamp

    # EVery day there is a folder, and every hour there is a json file
    f_ile =  "incident/incident" + incident_last_time_stamp[5:10] + "/" + "incident" + incident_last_time_stamp[5:10] +"_"+ incident_last_time_stamp[11:13] + ".json"
    directory = os.path.dirname(f_ile)
    if not os.path.exists(directory):
        os.makedirs(directory)


    jsonfile = open("incident/incident" + incident_last_time_stamp[5:10] + "/" + "incident" + incident_last_time_stamp[5:10] +"_"+ incident_last_time_stamp[11:13] + ".json", 'a')
    
    json.dump(b,jsonfile)
    jsonfile.write(os.linesep)
    jsonfile.close()
    
    
    freq = 120
    while True:
        try:
        
            if time.time() - last_time_incident >= freq:
                
                
                b = retrieve_data(incidentURL)
                
                b["TIMESTAMP"] = convert_time_trafficincident(b['TIMESTAMP'])
                if b["TIMESTAMP"] != incident_last_time_stamp:
                    last_time_incident = time.time()
                    incident_last_time_stamp = b["TIMESTAMP"]
                    print ("incident",b["TIMESTAMP"])

                    f_ile =  "incident/incident" + incident_last_time_stamp[5:10] + "/" + "incident" + incident_last_time_stamp[5:10] +"_"+ incident_last_time_stamp[11:13] + ".json"
                    directory = os.path.dirname(f_ile)
                    if not os.path.exists(directory):
                        os.makedirs(directory)


                    jsonfile = open("incident/incident" + incident_last_time_stamp[5:10] + "/" + "incident" + incident_last_time_stamp[5:10] +"_"+ incident_last_time_stamp[11:13] + ".json", 'a')

    
                    
                    json.dump(b,jsonfile)
                    jsonfile.write(os.linesep)
                    jsonfile.close()
                    
                    freq = 120
                else:
                    freq = 240
    
            if time.time() - last_time >= 180 or get_flow == False:
                    get_flow = False
                    last_time = time.time()
                    a = retrieve_data(URL)
                    get_flow = True
                    a['CREATED_TIMESTAMP'] = convert_time_trafficflow(a['CREATED_TIMESTAMP'])
                    flow_timestamp =  a['CREATED_TIMESTAMP']
                    print "flow" + a['CREATED_TIMESTAMP']


                    f_ile =  "flow/flow" + flow_timestamp[5:10] + "/" + "flow" + flow_timestamp[5:10] +"_"+ flow_timestamp[11:13] + ".json"
                    directory = os.path.dirname(f_ile)
                    if not os.path.exists(directory):
                        os.makedirs(directory)


                    jsonfile = open("flow/flow" + flow_timestamp[5:10] + "/" + "flow" + flow_timestamp[5:10] +"_"+ flow_timestamp[11:13] + ".json", 'a')

                    json.dump(a,jsonfile)
                    jsonfile.write(os.linesep)
                    jsonfile.close()
                    time.sleep(20)

        except Exception, e:
                ### Extra code in case of a network fail or error
                print "exception time" + str(e)
                print time.asctime( time.localtime(time.time()))
                #index = (index + 1) % 4
                time.sleep(20)
                continue
		
		
store_data()

