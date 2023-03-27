#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*ards)
        return result
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
