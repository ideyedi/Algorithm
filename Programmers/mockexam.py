# 2021.07.15 eyedi
# Programmers problem solve Complete Search
# Mock-Exam

def solution(answers):
    human1 = [1, 2, 3, 4, 5]
    human2 = [2, 1, 2, 3, 2, 4, 2, 5]
    human3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {'1':0, '2':0, '3':0}
    answer = []

    # complete search
    for idx, item in enumerate(answers):
        if item == human1[idx%5]:
            count['1'] += 1

        if item == human2[idx%8]:
            count['2'] += 1

        if item == human3[idx%10]:
            count['3'] += 1

    # List Comprehension
    answer = [int(k) for k,v in count.items() if max(count.values()) == v]
    answer.sort()

    return answer

