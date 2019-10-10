from enum import Enum

class Convert(Enum):
    toUpper = 0
    toLower = 1

def convertCase(string, conversion):

    switcher = {
        0: str.upper,
        1: str.lower
    }

    try:
        func = switcher.get(conversion.value)
        return func(string)
    except AttributeError:
        raise Exception('Invalid conversion type')
