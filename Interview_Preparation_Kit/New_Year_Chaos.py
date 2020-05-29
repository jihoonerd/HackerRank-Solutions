import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    total_move = 0
    for i in range(len(q) - 1, -1, -1):  # Iterate over the maximum index to 0
        # Should not use q.index(i) since it is computationally too heavy for every iteration

        # Left-side on the inequality indicates the number of bribes it tried,        
        # and right-side indicates how many times it got the bribes
        if (q[i] - (i + 1)) > 2:
            print("Too chaotic")
            return None

        # If it iterates simply from 0, it will face time limit.
        # Any bribery cannot go further 2 ahead than the position it should be.
        # Extreme cases)
        # e.g.) [3, 4, 5, 2, 1]
        #       q[4] - 2 = -1 <- Index should be searched from.
        # e.g.) [1, 2, 5, 3, 4]
        #       q[4] - 2 = 2 <- Index should be searched from.
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total_move += 1

    print(total_move)
    return None
