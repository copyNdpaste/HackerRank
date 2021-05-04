#!/bin/python3

import os


def maximum_toys(prices, k):
    prices.sort()
    count = 0

    for price in prices:
        if k <= 0 or price > k:
            break
        k -= price
        count += 1

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximum_toys(prices, k)

    fptr.write(str(result) + "\n")

    fptr.close()
