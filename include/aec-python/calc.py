# This is a build-on of the sum.py file to enable multiple calculation types instead of sum only

import argparse

# Parsers

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

# Add
add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs='*', type=int)

# Subtract
sub = subparsers.add_parser("sub", help='subtract integers')
sub.add_argument("ints_to_sub", nargs='*', type=int)

# Multiplication
mut = subparsers.add_parser("mut", help='multiply integers')
mut.add_argument("ints_to_mut", nargs='*', type=int)

# Division
div = subparsers.add_parser("div", help='divide integers')
div.add_argument("ints_to_div", nargs='*', type=int)



# Functions Definition to fit into argparser 

# def aec_subtract(ints_to_sub):
#   our_sub = ints_to_sub[0] - ints_to_sub[1]
#   print(f"The subtracted result is  {our_sub}")
#   return (our_sub)

# Adjusting the initial definition of aec_subtract to ensure the calculation can't go below zero
def aec_subtract(ints_to_sub):
  if len(ints_to_sub) > 2:
    raise Exception("More than two too much")
  else:
    arg_1 = ints_to_sub[0]
    arg_2 = ints_to_sub[1]
    our_sub = arg_1 - arg_2
    if our_sub < 0:
      our_sub = 0
    print(f"The subtracted result is {our_sub}")
    return our_sub

# def aec_division(ints_to_div):
#   if ints_to_div[1] == 0:
#     our_div = "Cannot Divide"
#     print(our_div)
#   else:
#     our_div = ints_to_div[0] / ints_to_div[1]
#     print(f"The Division result is  {our_div}")
#   return (our_div)

# Adjusting the initial function definition so that division by zero = 0
def aec_division(ints_to_div):
  if len(ints_to_div) > 2:
    raise Exception("More than two too much")
  else:
    if ints_to_div[1] == 0:
      our_div = 0
      print(f"The Division result is {our_div}")
    else:
      our_div = ints_to_div[0] / ints_to_div[1]
      print(f"The Division result is  {our_div}")
  return (our_div)


# Code Running

# We need to include a command that ensure the test only runs the commands that match that called from the CLI
if __name__ == "__main__":

  args = parser.parse_args()
  
  if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"the sum of values is: {our_sum}")

  # if args.command == 'sub':
  #   our_sub = args.ints_to_sub[0] - args.ints_to_sub[1]
  #   print(f"The subtracted result is  {our_sub}")

  # Using a function instead of manually defining
  if args.command == 'sub':
    aec_subtract(args.ints_to_sub)

  if args.command == 'mut':
    our_mut = 1
    for int in args.ints_to_mut:
      our_mut *= int # our_mut = our_mut * int
    print(f"The Multiplication result is  {our_mut}")

  # if args.command == 'div':
  #   if args.ints_to_div[1] == 0:
  #     print("Cannot Divide")
  #   else:
  #     our_div = args.ints_to_div[0] / args.ints_to_div[1]
  #     print(f"The Division result is  {our_div}")

  if args.command == 'div':
    aec_division(args.ints_to_div)