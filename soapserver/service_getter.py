from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.application import Application

from soapserver.services.case.service import TextService
from soapserver.services.loan.service import VinniesLoanService
from soapserver.services.ip.service import ResolveIP

def getWsgiApp(type):
    if type == 'case':
        service = TextService
    elif type == 'ip':
        service = ResolveIP
    elif type == 'loan':
        service = VinniesLoanService
    else:
        raise Exception('Invalid service type.')

    app = Application([service], 'magu.dev',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )

    return WsgiApplication(app)
