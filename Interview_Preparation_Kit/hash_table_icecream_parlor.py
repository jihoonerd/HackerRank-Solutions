#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    cost_dict = {}
    for idx, c in enumerate(cost):
        if money - c in cost_dict:
            print(cost_dict[money - c] + 1, idx + 1)
            return None
        else:
            cost_dict[c] = idx


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
