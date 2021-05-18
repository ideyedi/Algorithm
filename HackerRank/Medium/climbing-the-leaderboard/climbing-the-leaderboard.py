#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
"""
def climbingLeaderboard(scores, alice):
    result = []

    for a_score in alice:
        rank = 1 
        # Sorting socres array
        scores.sort(reverse = True)
        alice.sort()
        before_score = scores[0]

        for idx, score in enumerate(scores):
            if a_score < score:
                if before_score != score:
                    before_score = score;
                    rank = rank + 1 
                else :
                    if idx != 0:
                         rank = rank + 1 
                         result.append(rank)
                    break

                if (idx + 1) == int(len(scores)):
                    rank = rank + 1 
                    result.append(rank)

    return result

# Main function
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
"""

#!/bin/python3
# Can't solved this problem. 
# So, need to Analyze to source code which is uploaded at HackerRank
n = int(input().strip())
scores_raw = [int(scores_temp) for scores_temp in input().strip().split(' ')]
scores_list = list(set(scores_raw))
scores = list(reversed(sorted(scores_list)))
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]
## Start debug
print(alice)
#print(scores_raw)
# Deleted to duplicated number
#print(scores_list)
#print(sorted(scores_list))
#print(reversed(sorted(scores_list)))
print(list(reversed(sorted(scores_list))))
# End debug 

for x in alice:
#print(x)
    while len(scores) > 0 and scores[-1] <= x:
#print(scores)
        del scores[-1]
# if duplicated number deleted, scores length + 1 is to be rank
    print(len(scores) + 1)

