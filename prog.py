# Argparse Tutorial

# import argparse

# parser = argparse.ArgumentParser()
# parser.parse_args()



### Introducing Postitional Arguments

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help='echo the string you use here')
# args = parser.parse_args()
# print(args.echo)



### Doing something even more useful
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)



### Adding optional arguments

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--v", help="increase output verbosity")
# args = parser.parse_args()
# if args.v:
#     print("verbosity turned on")



### Introducing Optional Arguments
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-anyThing", help="increase output verbosity")
# args = parser.parse_args()
# if args.anyThing:
#     print("verbosity turned on")



### Modying the previous code

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")



### Short Options

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")



### Combing Positional and Optional arguments

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbose:
#     print("the square of {} equals {}".format(args.square, answer))
# else:
#     print(answer)



### Multiple Verbosity Values
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], 
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



### Turning the verbosity into a flag 

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display the square of a given number")
# parser.add_argument("-v", "--verbosity", action="count",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



### Fixing a bug when we got "16" from entering python prog.py 4 -vvv

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2

### bugfix: replace == with >=
# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity >= 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



### Fixing a bug when we got error from note entering any verbosity "python prog.py 4"

import argparse
parser = argparse.ArgumentParser(description='Learning Argparse Module')
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)    