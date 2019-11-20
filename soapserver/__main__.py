import argparse
from . import app

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Host a predifined SOAP server.")
    parser.add_argument('type', metavar='<Server Type>', type=str, help='Name of the server type to host. Supported: case, ip, loan')
    parser.add_argument('port', metavar='<Port>', type=int, help='Port to host')
    args = parser.parse_args()

    try:
        app.run(args.type, args.port)
    except Exception as e:
        print(e)