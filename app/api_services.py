#coding: utf-8
from urllib2 import Request, urlopen, URLError
import json
from models import TrainStation
HOST="http://localhost:5000"

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
            name = station["name"].encode("utf-8")
            howbig = station["howbig"].encode("utf-8")
            latitude = station["latitude"]
            longitude = station["longitude"]
            postal_code = station["postalCode"]
            city = station["city"].encode("utf-8")
            department= station["department"].encode("utf-8")
            region =station["region"].encode("utf-8")
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

if __name__ == "__main__":
    get_nearest_train_station("14 rue de vignolle, 51120 saint-quentin-le-verger")
