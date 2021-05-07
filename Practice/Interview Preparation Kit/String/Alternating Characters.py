#!/bin/python3
import os


def alternating_characters(s: str) -> int:
    result = 0
    for i in range(len(s) - 1):
        current = s[i]
        after = s[i + 1]
        if current == after:
            result += 1

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternating_characters(s)

        fptr.write(str(result) + "\n")

    fptr.close()
