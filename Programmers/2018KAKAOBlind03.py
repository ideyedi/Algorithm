msg = input()
answer = []

new_id = 27
table_dict = dict()

# ASCII table init
for ascii_num in range(65, 91):
    table_dict[chr(ascii_num)] = ascii_num - 64

print(table_dict)

# Start, end index
idx_s, idx_e = 0, 0

while True:

    idx_e += 1
    
    if idx_e == len(msg):
        answer.append(table_dict[msg[idx_s:idx_e]])
        break
    # 더 큰 언어가 있는지 확인하는 과정
    # idx_e + 1 만큼의 스트링이 없을 경우 이전 길이의 인덱스를 답변에 추가
    # 그 후 idx 처음을 끝에 맞춘다.
    if msg[idx_s:idx_e+1] not in table_dict.keys():
        table_dict[msg[idx_s:idx_e+1]] = new_id
        new_id += 1
        answer.append(table_dict[msg[idx_s:idx_e]])
        idx_s = idx_e

print(answer)
