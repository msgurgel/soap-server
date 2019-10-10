import logging
logger = logging.getLogger(__name__)

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
            logger.debug("Successful request to 'LoanPayment'")
            return result
        except Exception as e:
            logger.info("Invalid request to 'LoanPayment' – Reason: Payment is equal to zero.")
            raise PaymentsIsEqualToZeroError()
