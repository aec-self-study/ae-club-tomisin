# This is a build-on of the sum.py file to enable multiple calculation types instead of sum only

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

# Add
add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

# Subtract
sub = subparsers.add_parser("sub", help='subtract integers')
sub.add_argument("ints_to_sub", nargs=2, type=int)

# Multiplication
mut = subparsers.add_parser("mut", help='multiply integers')
mut.add_argument("ints_to_mut", nargs='*', type=int)

# Division
div = subparsers.add_parser("div", help='divide integers')
div.add_argument("ints_to_div", nargs=2, type=int)

 
args = parser.parse_args()
 
if args.command == "add":
  our_sum = sum(args.ints_to_sum)
  print(f"the sum of values is: {our_sum}")

if args.command == 'sub':
  our_sub = args.ints_to_sub[0] - args.ints_to_sub[1]
  print(f"The subtracted result is  {our_sub}")

if args.command == 'mut':
  our_mut = 1
  for int in args.ints_to_mut:
    our_mut *= int
  print(f"The Multiplication result is  {our_mut}")

if args.command == 'div':
  if args.ints_to_div[1] == 0:
    print("Cannot Divide")
  else:
    our_div = args.ints_to_div[0] / args.ints_to_div[1]
    print(f"The Division result is  {our_div}")