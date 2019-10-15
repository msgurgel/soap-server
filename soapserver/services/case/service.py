import logging
logger = logging.getLogger(__name__)

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

        try:
            enum_val = switcher.get(conversionType)
        except AttributeError:
            logger.info("Invalid request to 'ConvertCase' – Reason: Invalid conversion type")
            raise InvalidConversionTypeError()

        result = cc.convertCase(string, enum_val)

        logger.debug("Successful request made to 'ConvertCase'")
        return result

class InvalidConversionTypeError(Fault):
    def __init__(self):
        super(InvalidConversionTypeError, self).__init__(faultcode="Client", faultstring="Invalid conversion type. Options are 1: Uppercase, 2: Lowercase.")
