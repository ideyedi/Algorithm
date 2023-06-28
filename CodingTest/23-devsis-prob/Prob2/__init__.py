from typing import List


def solution(capacity, routes):
    answer = True
    map_length: int = 1001
    count_map: List[int] = [0 for _ in range(map_length)]

    for route in routes:
        index = route[1]

        for _ in range(route[2] - route[1] + 1):
            count_map[index] += route[0]
            index += 1

            # 종료조건
            if count_map[index] > capacity:
                answer = False

    print(count_map[:60])

    return answer


if __name__ == "__main__":
    s = solution(20, [[5, 1, 15], [14, 3, 18], [3, 15, 21], [9, 14, 52]])
    print(s)
