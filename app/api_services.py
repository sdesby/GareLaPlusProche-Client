#codint: utf-8
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
        print "Reading response"
        #m_id = station["_id"]["$oid"]
        name = station["name"]
        howbig = station["howbig"]
        latitude = station["latitude"]
        longitude = station["longitude"]
        postal_code = station["postalCode"]
        city = station["city"]
        region =station["region"]
        station = TrainStation()
        station.initialize("1", name, howbig, latitude, longitude, postal_code, city, "", region)
        return station

    except URLError, e:
		print "Erreur lors de la communication avec le service distant :" , e
		return -1
if __name__ == "__main__":
    get_nearest_train_station("14 rue de vignolle, 51120 saint-quentin-le-verger")
