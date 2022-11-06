#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countInversions(arr):
    # Write your code here
    count = 0
    sorted_arr, count = merge_sort(arr, count)
    print(sorted_arr)
    return count


def merge_sort(array, count):

    if len(array) == 1:
        return array, count

    mid = len(array) // 2
    left_arr, count = merge_sort(array[:mid], count)
    right_arr, count = merge_sort(array[mid:], count)

    sorted_arr = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1
            count += len(left_arr) - i

    sorted_arr += left_arr[i:]
    sorted_arr += right_arr[j:]

    return sorted_arr, count


if __name__ == "__main__":
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr)
        print(result)
