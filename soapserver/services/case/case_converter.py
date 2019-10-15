from enum import Enum

class Convert(Enum):
    TO_UPPER = 0
    TO_LOWER = 1

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
