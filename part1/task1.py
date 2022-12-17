import argparse

def parse(arg1, op, arg2):
    if arg1 and op and arg2:
        if arg1.isnumeric() and arg2.isnumeric():
            if op == "+":
                print(f"{arg1} + {arg2} = {int(arg1) + int(arg2)}")
            elif op == "-":
                print(f"{arg1} - {arg2} = {int(arg1) - int(arg2)}")
            elif op == "*":
                print(f"{arg1} * {arg2} = {int(arg1) * int(arg2)}")
            elif op == "/":
                print(f"{arg1} / {arg2} = {(int(arg1) / int(arg2)):0.2f}")
            else:
                print("Please, enter one of these operators: '+', '-', '*', '/'")
        else:
            print("This program works only with number. Please, enter valid arguments")
    else:
        print("Please, enter all values")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("argument1", nargs='?')
    parser.add_argument("operator", nargs='?')
    parser.add_argument("argument2", nargs='?')
    args = parser.parse_args()

    parse(args.argument1, args.operator, args.argument2)


if __name__ == "__main__":
    main()