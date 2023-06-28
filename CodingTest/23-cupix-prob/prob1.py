import math


def solution(n):
    k = 0
    l = len(bin(n)[2:])

    print(bin(n))
    for item in bin(n)[2:]:
        if item == '1':
            k += 1

    print(f"k = {k}, l = {l}")


    return answer


if __name__ == "__main__":
    s = solution(100)
    print(f"ret: {s}")
