import argparse
parser = argparse.ArgumentParser('Trying to pass option and Arguments through command line')
parser.add_argument('-v','--verbose',action='store_true',help='Verbosity')
parser.add_argument('-t','--turn_on', action='store_false')# if exists on command line false is retuned
parser.add_argument('-s','--start',action='store_true')# if exists on command line True is returned
parser.add_argument('integers', metavar='N', type=int, nargs='+')# N and file positional arguments should be given in command line
parser.add_argument('-f', '--foo', help='foo help')
parser.add_argument('-b', '--bar', help='bar help')
parser.add_argument('-z', '--baz', help='baz help')
# Hiphen symbol makes the difference
# if it is added before it is taken as optional argument or else it is a positional arguments.
parser.add_argument('file',type=argparse.FileType('r'))
parser.add_argument('stringaddtion', type=str)
args = parser.parse_args()
print(args)
print(args.integers)
print(args.turn_on)
print(args.file.read())

