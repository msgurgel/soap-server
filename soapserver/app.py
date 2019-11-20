from . import config
from soapserver.lib.logphant import logphant

# Setup logphant
config.setupConfig()

log_port = config.readVal('logphant', 'port')

logger = logphant.Logger(log_port)
config.setVal('logphant', 'token', logger.token)

from wsgiref.simple_server import make_server
from soapserver.service_getter import getWsgiApp

def run(serverType, port):
    wsgi_app = getWsgiApp(serverType)

    logger.log("info", "listening to http://127.0.0.1:%d" % port)
    logger.log("info", "wdsl is at: http://localhost:%d/?wsdl" % port)

    server = make_server('127.0.0.1', port, wsgi_app)
    server.serve_forever()
