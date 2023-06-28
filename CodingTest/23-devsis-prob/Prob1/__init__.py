from typing import List


def solution(score: int):
    answer = 0
    jelly_list: List[int] = [100, 50, 5, 1]

    for item in jelly_list:
        # 먹은 젤리 수
        answer += score // item
        # 남은 점수 값
        score = score % item

    return answer


if __name__ == "__main__":
    s = solution(156)
    print(f"answer: {s}")
