import argparse
parser = argparse.ArgumentParser()
# argparse by default treats the options we give as strings so we have used type
# option below to specify that the command line to be sent is integer.
parser.add_argument('-v','--verbose',help= "increase output verbosity",type= int,choices=[0,1,2])
parser.add_argument("square",help="dispaly square of a number",type= int)
args = parser.parse_args()
ans  = args.square ** 2
if args.verbose == 2:
    print(f"square of {args.square} is equal to {ans}")
elif args.verbose == 1:
    print(f"{args.square^2} == {ans}")
else:
    print(ans)
    
