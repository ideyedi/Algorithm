#! python3
import sys


def solution(cards, k):
    min_x = sys.maxsize
    card_map = set(cards)

    # 뽑을 수 있는 자연수보다 요구하는 수가 클 경우 불가능
    if k > len(cards):
        return -1

    for idx in range(len(cards)):
        x = 0
        tmp_set = set()
        index = idx

        while True:
            x += 1
            tmp_set.add(cards[index])
            index += 1

            if k == len(tmp_set):
                if min_x > x:
                    min_x = x
                break

            if index > len(cards) - 1:
                break

    return min_x


if __name__ == "__main__":
    print(f'test')