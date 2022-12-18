# You are given n bars of gold with weights: w1, w2, ..., wn and bag with capacity W.
# There is only one instance of each bar and for each bar you can either take it or not
# (hence you cannot take a fraction of a bar).
# Write a function that returns the maximum weight of gold that fits into a knapsack's capacity.
# The first parameter contains 'capacity' - integer describing the capacity of a knapsack.
# The next parameter contains 'weights' - list of weights of each gold bar.
# The last parameter contains 'bars_number' - integer describing the number of gold bars.
# Output : Maximum weight of gold that fits into a knapsack with capacity of W.

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