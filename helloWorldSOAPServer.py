# from spyne import Application, rpc, ServiceBase, Iterable, UnsignedInteger, Unicode
from spyne.application import Application

from spyne.decorator import rpc

from spyne.service import ServiceBase

from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):
    @rpc(Unicode, UnsignedInteger, _returns=Iterable(Unicode)) # Defines Types and order of SOAP params, as well as the type of the return value
    def say_hello(ctx, name, times):
        for i in range(times):
            yield u'Hello, %s' % name

# Deploying the service usign SOAP via WSGI
app = Application([HelloWorldService], 'target.namespace',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )

wsgi_app = WsgiApplication(app)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wdsl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()