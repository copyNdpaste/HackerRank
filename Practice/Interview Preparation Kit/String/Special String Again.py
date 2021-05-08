#!/bin/python3

import os


def substr_count(n: int, s: str) -> int:
    count = n
    for i in range(0, n):
        even_before = i
        even_after = i + 1
        odd_before = i - 1
        odd_after = i + 1

        count = count_palindromes(
            count=count,
            even_before=even_before,
            even_after=even_after,
            odd_before=odd_before,
            odd_after=odd_after,
            n=n,
            s=s,
        )

    return count


def count_palindromes(
    count: int,
    even_before: int,
    even_after: int,
    odd_before: int,
    odd_after: int,
    n: int,
    s: str,
) -> int:
    even_std = s[even_before]
    odd_std = s[odd_before]
    while even_before >= 0 and even_after <= n - 1:
        if s[even_before] == s[even_after] == even_std:
            count += 1
            even_before -= 1
            even_after += 1
        else:
            break

    while odd_before >= 0 and odd_after <= n - 1:
        if odd_std == s[odd_before] and odd_std == s[odd_after]:
            count += 1
            odd_before -= 1
            odd_after += 1
        else:
            break

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = substr_count(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()
