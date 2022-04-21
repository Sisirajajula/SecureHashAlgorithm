import argparse
parser = argparse.ArgumentParser(description='process some integers')
parser.add_argument('integers',metavar='N',type=int,nargs='+',
                    help='an integer for accumulator')
parser.add_argument('--sum',dest='accumulate',action='store_const',const=sum,default=max,
                    help='sum of integers(default: find max)')
args = parser.parse_args()
print(args)
print(args.accumulate(args.integers))
