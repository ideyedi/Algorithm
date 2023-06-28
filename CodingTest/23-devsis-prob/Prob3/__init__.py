from typing import List
from itertools import combinations


def solution(pouches):
    answer = 0

    for index in range(len(pouches)):
        nCr = list(combinations(pouches, index + 1))

        for case in nCr:
            print(f"Case: {case}")
            jelly_map = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

            # Make jelly Map
            for item in case:
                for jelly in item:
                    jelly_map[jelly] += 1

            map_max = max(jelly_map.values())
            others_sum = sum(jelly_map.values()) - map_max
            print(map_max, others_sum)
            if len(case) > answer and map_max > others_sum:
                answer = len(case)

    return answer


if __name__ == "__main__":
    #example
    """
    ["cab", "adaaa", "e"] return 3
    ["aabb", "baba"] return 0
    ["d", "a", "e", "d", "abdcc"] return 3
    ["a"] return 1
    """
    s = solution(['d', 'a', 'e', 'd', 'abdcc'])
