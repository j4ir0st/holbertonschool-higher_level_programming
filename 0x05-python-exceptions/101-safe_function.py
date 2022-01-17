#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(args[0], args[1])
    except Exception as zd:
        print("Exception: {}".format(zd), file=sys.stderr)
        return None
