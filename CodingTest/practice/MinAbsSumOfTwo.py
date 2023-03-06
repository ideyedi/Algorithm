#! python
def solution(A):
    """
    조합을 찾을 때 이미 사용된 인덱스의 값을 다시 사용하는 것이 가능한 것이 중요!
    :param A: N is an integer within the range [0..100,000];
    :return: Min abs sum of two, 두 수의 절대 값의 합의 최솟값
    """
    # 같은 수 두개을 더하는 경우에서 가장 작은 값을 구할 수는 없고, 0이 값으로 존재하는 경우도 없음
    # Combination 경우의 수만 생각하면 되는데
    # 두 수의 합의 절대값이 최소가 되기위한 조건
    min_val = 2000000000
    # 절대 값을 기준으로 정렬할 수 있는 Best Practice!!!
    A.sort(key=lambda x: abs(x))

    for i in range(len(A) - 1):
        min_val = min(min_val, abs(A[i] + A[i + 1]))

    return min_val


if __name__ == "__main__":
    print(f"ret: {solution([1, 4, -3])}")
    print(f"ret: {solution([1, 5, 2, -2])}")
