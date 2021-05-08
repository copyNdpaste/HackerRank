#!/bin/python3

import os
from collections import Counter


def is_valid(s):
    s_counter = Counter(s)
    standard = set(s_counter.values())
    for std in standard:
        remove_count = 0
        for v in s_counter.values():
            if std != v:
                diff = abs(std - v)
                if diff > v:
                    remove_count += v
                else:
                    remove_count += diff
        if remove_count < 2:
            return "YES"
    return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = is_valid(s)

    fptr.write(result + "\n")

    fptr.close()
