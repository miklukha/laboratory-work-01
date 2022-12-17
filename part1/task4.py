import argparse

def parse(capacity, weights, bars_number):
    if capacity and len(weights) != 0 and bars_number:
        weights = list(map(int, weights))

        weights = [0] + weights
        capacity = int(capacity) + 1
        bars_number = int(bars_number)

        w = [[0 for _ in range(bars_number)] for _ in range(capacity)]

        for i in range(1, bars_number):
            for j in range(1, capacity):
                w[j][i] = w[j][i - 1]
                if weights[i] <= j:
                    val = w[j - weights[i]][i - 1] + weights[i]
                    if w[j][i] < val:
                        w[j][i] = val
        return w[-1][-1]
    else:
        return "Please, enter all values"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-W", dest="capacity", nargs='?')
    parser.add_argument("-w", dest="weights", nargs='+', default=[])
    parser.add_argument("-n",  dest="bars_number", nargs='?')
    args = parser.parse_args()

    print(parse(args.capacity, args.weights, args.bars_number))

if __name__ == "__main__":
    main()