def solution(numbers):
    answer = ''
    # Number List를 String type으로 변환
    numbers = list(map(str, numbers))

    # Lambda를 이용한 Sorting 기준 변경
    # 자연수 1000 이하의 수이기 때문에 문자열을 3개까지 이어붙여 비교할 수 있음
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    answer = str(int(''.join(numbers)))
    return answer
