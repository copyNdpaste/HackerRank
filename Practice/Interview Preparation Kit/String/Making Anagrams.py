#!/bin/python3

import os
from collections import Counter


def make_anagram(a: str, b: str) -> int:
    a_counter = Counter(a)
    b_counter = Counter(b)

    for c in a:
        if c in b_counter:
            if a_counter[c] >= b_counter[c]:
                a_counter[c] -= b_counter[c]
                b_counter[c] = 0
            else:
                b_counter[c] -= a_counter[c]
                a_counter[c] = 0

    for c in b:
        if c in a_counter:
            if b_counter[c] >= a_counter[c]:
                b_counter[c] -= a_counter[c]
                a_counter[c] = 0
            else:
                a_counter[c] -= b_counter[c]
                b_counter[c] = 0

    return sum(a_counter.values()) + sum(b_counter.values())


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = input()

    b = input()

    res = make_anagram(a, b)

    fptr.write(str(res) + "\n")

    fptr.close()
