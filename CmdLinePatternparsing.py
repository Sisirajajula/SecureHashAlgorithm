
from re import match
import sys
import hashlib
import os
import re
from typing import Dict
#Basic seperation of option and arguments from command line program arguments.
#It does not solve the condition where string contains a hypen.
# opts = [opt for opt in sys.argv[1:] if opt.startswith('-')]
# args = [arg for arg in sys.argv[1:] if not arg.startswith('-')]
# print(f'options:{opts} and arguments:{args}')
# if '-c' in opts:
#     print(" ".join(arg.capitalize() for arg in args))
# elif '-u' in opts:
#     print(" ".join(arg.upper() for arg in args))
# else:
#     raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")
# # we can also use os.fsencode to get original bytes of a python command line arguments
# # Usage of hashlib and secure hash algorithm1.Hash value generated will never change for a given string until and unless string changes. 
# try:
#     arg = sys.argv[1] # arg = os.fsencode(sys.argv[1])
#     m = hashlib.sha1() # m = hashlib.sha1()
#     m.update(bytes(arg,'utf-8')) # m.update(arg)
#     print(m.hexdigest()) # print(m.hexdigest())
# except IndexError:
#     raise SystemExit(f"Usage: {sys.argv[0]} has no command line arguments given")    
# Usage of regular expressions to handle python command line arguments.
# Regular expression used to check if a string contains the specified search pattern
args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)? # "?"represent zero or one occurences. "|" Either or
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
   re.VERBOSE,
)
# To handle arguments are needed to be in the form of a string.

arg_line = " ".join(sys.argv[1:])
print(arg_line)
def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
       args = {k: v for k, v in match_object.groupdict().items() if v is not None}
    return args
print(parse(arg_line))