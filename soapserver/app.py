import logging

from wsgiref.simple_server import make_server
from soapserver.service_getter import getWsgiApp

def run(serverType):
    wsgi_app = getWsgiApp(serverType)

    # Setup logger
    formatter = '%(asctime)s | %(levelname)s : %(name)s - %(message)s'
    logging.basicConfig(format=formatter, datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO, filename='soap_server.log')
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.getLogger('spyne.application.client').setLevel(logging.CRITICAL)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wdsl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()
