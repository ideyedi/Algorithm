from collections import deque

def solution(subway, start, end):
    answer = 0
    sub = []
    dic = {}
    visit = []
    queue = deque()
    
    #maximum 1000
    for item in subway:
        tmp = list(map(int, item.split(' ')))
        sub.append(tmp)
    
    for item in sub:
        for idx in range(len(item)-1):
            try:
                dic[item[idx]].append(item[idx+1])
            except:
                dic[item[idx]] = [item[idx+1]]

    # print(dic)
    # bfs   
    queue.append(start)
    while queue:
        node = queue.pop()
        if node not in visit:
            visit.append(node)
            queue.extend(list(dic[node]))
            
    
    #print(visit)
    return answer
