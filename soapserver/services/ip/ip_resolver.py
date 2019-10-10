from zeep import Client

def resolveIP(ip):
    client = Client("http://ws.cdyne.com/ip2geo/ip2geo.asmx?WSDL")

    result = client.service.ResolveIP(ip, 0)

    return IPInfo(
        result.City,
        result.StateProvince,
        result.Country,
        result.Organization,
        result.Latitude,
        result.Longitude
    )

class IPInfo(object):

    def __init__(self, city, stateProvince, country, organization, latitude, longitude):
        self.city = city
        self.stateProvince = stateProvince
        self.country = country
        self.organization = organization
        self.latitude = latitude
        self.longitude = longitude
