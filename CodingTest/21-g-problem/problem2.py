grad = [[0, 'A+'], [1, 'A0'], [2, 'A-'], [3, 'B+'], [4, 'B0'], [5, 'B-'], [6, 'C+'],
        [7, 'C0'], [8, 'C-'], [9, 'D+'], [10, 'D0'], [11, 'D-'], [12, 'F']]

def findGradeW(grade):
    ret = -1
    for item in grad:
        if item[1] == grade:
            ret = item[0]
            break
    return ret


def gradeCheck(prev, post):
    ret = False
    
    if findGradeW(prev) > findGradeW(post):
        ret = True
        
    return ret 


def solution(grades):
    answer = []
    dic = {}
    new = {}
    
    for g in grades:
        ls = g.split(' ')
        try:
            if gradeCheck(dic[ls[0]], ls[1]):
                del dic[ls[0]]
                dic[ls[0]] = ls[1]
        except:
            dic[ls[0]] = ls[1]

    for item in dic.items():
        ret = findGradeW(item[1])
        tmp = [item[1], ret]
        new[item[0]] = tmp
    
    new = sorted(new.items(), key=lambda x:x[1])
    for item in new:
        tmp = item[0] + ' ' + item[1][0]
        answer.append(tmp)

    return answer