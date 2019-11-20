import configparser

config = configparser.ConfigParser()

def setupConfig():
    config['logphant'] = {
        'token': '',
        'port': '8080',
    }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


def setVal(group, key, val):
    config[group][key] = val

    with open('config.ini', 'w') as configfile:
        config.write(configfile)



def readVal(group, key):
    config.read('config.ini')
    return config[group][key]