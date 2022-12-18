# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF
# syntax (without using regular expressions).
# Formula = Number* | (Formula Sign Formula)
# Sign = '+' | '-'
# Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
# Input: string
# Result: (True / False, The result value / None)
# Example,
# user_input = '1+2+4-2+5-1' result = (True, 9)
# user_input = '123' result = (True, 123)
# user_input = 'hello+12' result = (False, None)
# user_input = '2++12--3' result = (False, None)
# user_input = '' result = (False, None)
# Example how to call the script from CLI:
# $ python task_1_ex_3.py 1+5-2

import argparse

def operation(acc, op, num):
    if op == '+':
        return acc + num
    elif op == '-':
        return acc - num
    elif op == 'null':
        return num

def parse(expression):
    acc = 0
    num = 0
    op = 'null'

    if expression is None:
        return (False, None)

    for symbol in expression:
        if symbol.isnumeric():
            if num is None:
                num = 0
            num = num * 10 + int(symbol)
        elif symbol == "+" or symbol == "-":
            if num is None:
                return False, None
            acc = operation(acc, op, num)
            op = symbol
            num = None
        else:
            return False, None
    return True, operation(acc, op, num)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("expression", nargs='?')
    expression = parser.parse_args().expression

    print(parse(expression))

if __name__ == "__main__":
    main()