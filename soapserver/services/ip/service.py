from soapserver.lib.logphant import logphant
from soapserver import config

token = config.readVal('logphant', 'token')
log_port = config.readVal('logphant', 'port')
logger = logphant.Logger(log_port, token)

from spyne.decorator import srpc
from spyne.service import ServiceBase

# Types
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.model.primitive import Float
from spyne.model.complex import ComplexModel
from spyne.model.fault import Fault

# Functions
from . import ip_resolver as ipr


class IpInfo(ComplexModel):
    City = String
    StateProvince = String
    Country = String
    Organization = String
    Latitude = Float
    Longitude = Float

class InvalidIPAddress(Fault):
    def __init__(self, faultstring):
        super(InvalidIPAddress, self) \
            .__init__(faultcode="Client.InvalidIPAddress", faultstring=faultstring)


class ResolveIP(ServiceBase):
    @srpc(String, _returns=IpInfo)
    def GetInfo(ipAddr):
        try:
            ipInfo = ipr.resolveIP(ipAddr)
            logger.log("debug", "Successful request made to 'GetInfo'")
        except Exception as e:
            logger.log("info", "invalid request to 'GetInfo' – Reason: %s – Value: ipAddr = %s" % e.args[0], ipAddr)
            raise InvalidIPAddress(e.args[0])

        return IpInfo (
            City=ipInfo.city,
            StateProvince=ipInfo.stateProvince,
            Country=ipInfo.country,
            Organization=ipInfo.organization,
            Latitude=ipInfo.latitude,
            Longitude=ipInfo.longitude
        )
