# Write a Python-script that performs the standard math functions on the data.
# The name of function and data are set on the command line when the script is run.
# The script should be launched like this:
# $ python my_task.py add 1 2

import argparse

def parse(op, arg1, arg2):
    if arg1 and op and arg2:
        if arg1.isnumeric() and arg2.isnumeric():
            if op == "add":
                print(f"{arg1} + {arg2} = {int(arg1) + int(arg2)}")
            elif op == "subtract":
                print(f"{arg1} - {arg2} = {int(arg1) - int(arg2)}")
            elif op == "multiply":
                print(f"{arg1} * {arg2} = {int(arg1) * int(arg2)}")
            elif op == "divide":
                print(f"{arg1} / {arg2} = {(int(arg1) / int(arg2)):0.2f}")
            else:
                print("Please, enter one of these operators: '+', '-', '*', '/'")
        else:
            print("This program works only with number. Please, enter valid arguments")
    else:
        print("Please, enter all values")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("operator", nargs='?')
    parser.add_argument("argument1", nargs='?')
    parser.add_argument("argument2", nargs='?')
    args = parser.parse_args()

    parse(args.operator, args.argument1, args.argument2)


if __name__ == "__main__":
    main()