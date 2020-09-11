import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    result = []
    start_score = alice[0]
    before_score = scores[0]
    rank = 1
    index = 0

    # find index, rank
    for idx, score in enumerate(scores):
        if (start_score < score):
            if (before_score != score):
                rank = rank + 1
                before_score = score
                index = idx

    print("index: " + str(index))
    print("rank : " + str(rank))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

