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