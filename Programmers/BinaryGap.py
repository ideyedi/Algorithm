#! python

def solution(N):
    bi_n = list(str(format(N, 'b')))
    longest_gap = 0
    curr = 0

    for item in bi_n:
        if item == '1':
            if curr == 0:
                pass
            else:
                longest_gap = max(longest_gap, curr)
                curr = 0
        else:
            curr += 1

    return longest_gap


if __name__ == "__main__":
    print(f"ret: {solution(1041)}")