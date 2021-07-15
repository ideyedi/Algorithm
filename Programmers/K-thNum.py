#def solution(array, commands):
#    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    answer = []

    #print(array, commands)
    for com in commands:
        tmp_list = array[com[0]-1:com[1]]
        tmp_lsit = tmp_list.sort()
        #print(tmp_list)
        answer.append(tmp_list[com[2]-1])
    return answer

# .. Lambda로 훅 풀어버리는게 뒷통수 한대 맞은 느낌..

