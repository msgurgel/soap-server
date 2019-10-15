from zeep import Client
import re

def resolveIP(ip):
    # Check IP address
    if not (validateIP(ip)):
        raise Exception('Invalid IP address')

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

def validateIP(ip):
    valid_ip = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    return True if valid_ip else False

class IPInfo(object):

    def __init__(self, city, stateProvince, country, organization, latitude, longitude):
        self.city = city
        self.stateProvince = stateProvince
        self.country = country
        self.organization = organization
        self.latitude = latitude
        self.longitude = longitude
