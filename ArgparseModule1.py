import argparse
# Creating an ArgumentParser object.This object parser holds all information necessary
# to parse command line into python data types.
parser = argparse.ArgumentParser(description='process some integers')
# add_argument method tells the ArgumentParser how to make strings on command line and 
# turn them into objects.
parser.add_argument('integers',metavar='N',type=int,nargs='+',
                    help='an integer for accumulator')
parser.add_argument('--sum',dest='accumulate',action='store_const',const=sum,default=max,
                    help='sum of integers(default: find max)')
# Calling parse_args() return an object with two attributes accumulate and integers.
# Integers attribute is list of one or more ints, and accumulate will be sum if --sum was
# mentioned on command or else by default it performs max operation on interger attribute list
args = parser.parse_args()
# print(args): Namespace(accumulate=<built-in function sum>, integers=[12, 3, 4])
print(args)
# print(args.accumulate(args.integers)) : 19
print(args.accumulate(args.integers))
