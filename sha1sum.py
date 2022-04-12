import sys
import hashlib
import os
#Basic seperation of option and arguments from command line program arguments.
#It does not solve the condition where string contains a hypen.
opts = [opt for opt in sys.argv[1:] if opt.startswith('-')]
args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
print(f'options:{opts} and arguments:{args}')
if '-c' in opts:
    print(" ".join(arg.capitalize() for arg in args))
elif '-u' in opts:
    print(" ".join(arg.upper() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
# we can also use os.fsencode to get original bytes of a python command line arguments
# Usage of hashlib and secure hash algorithm1.Hash value generated will never change for a given string until and unless string changes. 
try:
    arg = sys.argv[1] # arg = os.fsencode(sys.argv[1])
    m = hashlib.sha1() # m = hashlib.sha1()
    m.update(bytes(arg,'utf-8')) # m.update(arg)
    print(m.hexdigest()) # print(m.hexdigest())
except IndexError:
    raise SystemExit(f"Usage: {sys.argv[0]} has no command line arguments given")    



