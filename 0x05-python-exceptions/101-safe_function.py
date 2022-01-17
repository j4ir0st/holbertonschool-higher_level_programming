#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as zd:
        print("Exception: {}".format(zd), file=sys.stderr)
        return None
