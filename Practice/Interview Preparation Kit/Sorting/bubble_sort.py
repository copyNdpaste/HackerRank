#!/bin/python3


def count_swaps(a):
    length = len(a)
    count = 0

    for _ in range(length):
        for j in range(length - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1

    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == "__main__":
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    count_swaps(a=a)
