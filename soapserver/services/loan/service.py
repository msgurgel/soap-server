from soapserver.lib.logphant import logphant
from soapserver import config

token = config.readVal('logphant', 'token')
log_port = config.readVal('logphant', 'port')
logger = logphant.Logger(log_port, token)

from spyne.decorator import srpc
from spyne.service import ServiceBase

# Types
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import Float
from spyne.model.fault import Fault

# Functions
from . import loan_calculator as lc

class PaymentsIsEqualToZeroError(Fault):
    def __init__(self):
        super(PaymentsIsEqualToZeroError, self) \
            .__init__(faultcode="Client.PaymentsIsEqualToZeroError", faultstring="Payments cannot be zero.")

class VinniesLoanService(ServiceBase):
    @srpc(Float, Float, UnsignedInteger, _returns=Float, _throws=PaymentsIsEqualToZeroError)
    def LoanPayment(principle, rate, payments):
        try:
            result = lc.loanPayment(principle, rate, payments)
            logger.log("debug", "Successful request made to 'LoanPayment'")
            return result
        except Exception as e:
            logger.log("info", "invalid request to 'LoanPayment' – Reason: payment is equal to zero – Values: principle = %s, rate = %s, payments = %s" % principle, rate, payments)
            raise PaymentsIsEqualToZeroError()
