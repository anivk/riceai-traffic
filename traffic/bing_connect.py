#bing_connect.py
import requests
import json
import ast
import time
import urllib2

key = '5lr03uc8ED3BKCehrM4s~UeZYhEuwi5E-XmN3wnP7Ew~AuVG-mN8njenB8rQfdOR28vfuFYqAm7BB56b6l5MNKAld_cYwrkD32bjSvPa4yV2'
#URL Format: 'http://dev.virtualearth.net/REST/v1/Traffic/Incidents/37,-105,45,-94?key=YourBingMapsKey'
def query_incidents(bb, key):
    url = 'http://dev.virtualearth.net/REST/v1/Traffic/Incidents/{0},{1},{2},{3}?key={4}'.format(bb[0], bb[1], bb[2], bb[3], key)

    print url, '\n'

    page = requests.get(url)
    data = json.loads(page.content)
    print data
    return data

def strip_u(orig):
    new = str(orig).replace(' u\'',' \'' )
    new = new.replace('{u\'','{\'' )
    return ast.literal_eval(new)

#Houston Bounding Box
bb = [29.522261,-95.645041,29.999123,-95.09572]


# incidents = strip_u(incidents_orig)
# incidents = str(incidents_orig).replace('u\'','\'' )
# incidents = ast.literal_eval(incidents)
# print incidents
# print type(incidents)
while(True):
    incidents_orig = query_incidents(bb, key)
    millis = int(round(time.time() * 1000))
    name = 'incidentcase_bing_'+str(millis)+'.json'
    with open(name, 'w') as fp:
        json.dump(incidents_orig, fp)
    print "Bing Incident File Written: " + name
    time.sleep(3600)
