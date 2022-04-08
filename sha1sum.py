
import sys
import hashlib
import os
# we can also use os.fsencode to get original bytes of a python command line arguments.
try:
    arg = sys.argv[1] # arg = os.fsencode(sys.argv[1])
    m = hashlib.sha1() # m = hashlib.sha1()
    m.update(bytes(arg,'utf-8')) # m.update(arg)
    print(m.hexdigest()) # print(m.hexdigest())
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} has no command line arguments given")    


