# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen, URLError
import json
from models import TrainStation
import os

HOST = os.environ.get("API_URL")


def get_nearest_train_station(address):
    url = HOST + "/nearest-station?address=" + address
    url = url.replace(" ", "%20")
    request = Request(url)
    print "Requesting url : " + url
    try:
        response = urlopen(request)
        station = json.loads(response.read())

        print "#####"
        print station
        print "#####"
        if "error" not in station:
            print "Reading response"
            #m_id = station["_id"]["$oid"]
            name = station["name"]
            howbig = station["howbig"]
            latitude = station["latitude"]
            longitude = station["longitude"]
            postal_code = station["postalCode"]
            city = station["city"]
            department= station["department"]
            region =station["region"]
            station = TrainStation()
            station.initialize("1", name, howbig, latitude, longitude, postal_code, city, department, region)
            return station
        else:
            return json.dumps(station)

    except URLError, e:
        print e
        if "HTTP Error 400" in str(e):
            return 400
        else:
            return -1
