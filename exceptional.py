import sys
from math import log

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert(s):
    x = -1

    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]

        x = int( number)


    # We use the pass no-op statement to have an empty block which if we did not use would result in an IndentationError.
    #except (KeyError, TypeError ):
    #   pass

    except (KeyError, TypeError ) as e:
        print(F"Conversion error: {e!r}", file=sys.stderr)

        # We can use rase to re-raise the exception. 
        # We should always propagate exceptions to the client (i.e., caller of the function) instead of returnign an error code.
        # Error code can be ignored, but exceptions can not.  Let the client handle the exception.
        raise

    return x

def string_log(s):
    # convert to a number
    v = convert(s)

    #compute and return the natural log of the number
    return log(v)
