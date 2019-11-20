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
from spyne.model.fault import Fault

# Functions
from . import case_converter as cc

class TextService(ServiceBase):
    @srpc(String, UnsignedInteger, _returns=String)
    def ConvertCase(string, conversionType):
        switcher = {
            1: cc.Convert.TO_UPPER,
            2: cc.Convert.TO_LOWER
        }

        if switcher.get(conversionType, -1) == -1:
            logger.log("info", "invalid request to 'ConvertCase' – Reason: invalid conversion type – Value: conversionType = %s" % conversionType)
            raise InvalidConversionTypeError()

        enum_val = switcher.get(conversionType)
        result = cc.convertCase(string, enum_val)


        logger.log("debug", "Successful request made to 'ConvertCase'")

        return result

class InvalidConversionTypeError(Fault):
    def __init__(self):
        super(InvalidConversionTypeError, self).__init__(faultcode="Client", faultstring="Invalid conversion type. Options are 1: Uppercase, 2: Lowercase.")
