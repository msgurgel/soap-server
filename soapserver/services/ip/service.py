from spyne.decorator import srpc
from spyne.service import ServiceBase

# Types
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.model.primitive import Float
from spyne.model.complex import ComplexModel

# Functions
from . import ip_resolver as ipr


class IpInfo(ComplexModel):
    City = String
    StateProvince = String
    Country = String
    Organization = String
    Latitude = Float
    Longitude = Float

class ResolveIP(ServiceBase):
    @srpc(String, _returns=IpInfo)
    def GetInfo(ipAddr):
        ipInfo = ipr.resolveIP(ipAddr)
        return IpInfo (
            City=ipInfo.city,
            StateProvince=ipInfo.stateProvince,
            Country=ipInfo.country,
            Organization=ipInfo.organization,
            Latitude=ipInfo.latitude,
            Longitude=ipInfo.longitude
        )
