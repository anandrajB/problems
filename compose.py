import math
import os
import random
import re
import sys
from typing import Callable


def add(*args):
    result = 0
    for x in args:
        result += x
    return result


def square(a):
    return a * a


def splitter(a):
    return [a // 2, (a + 1) // 2]


def my_max(a):
    if type(a) is int:
        return a
    else:
        return max(a)


def my_min(a):
    if type(a) is int:
        return a
    else:
        return min(a)


def compose(*functionsList: Callable) -> Callable:
    pass


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    functionMapper = {
        "add": add,
        "square": square,
        "splitter": splitter,
        "my_max": my_max,
        "my_min": my_min,
    }

    functionsList_count = int(input().strip())

    functionsList = []

    for _ in range(functionsList_count):
        functionsList_item = input()
        functionsList.append(functionMapper[functionsList_item])

    composedFunctions = compose(*functionsList)

    argumentsList_count = int(input().strip())

    argumentsList = []

    for _ in range(argumentsList_count):
        argumentsList_item = int(input().strip())
        argumentsList.append(argumentsList_item)

    result = composedFunctions(*argumentsList)

    fptr.write(str(result) + "\n")

    fptr.close()
