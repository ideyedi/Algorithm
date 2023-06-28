
def solution(total_sp, skills):
    # 스킬 총 종류
    kinds = len(skills) + 1
    sp_map = {n+1: [] for n in range(kinds)}
    upper = set([])
    x_count = [0 for n in range(kinds)]

    for item in skills:
        upper.add(item[0])
        sp_map[item[0]].append(item[1])

    leaf = set(sp_map.keys()) - upper

    for item in leaf:
        x_count[item - 1] += 1

    # 상위 중 Leaf로만 되어있는 상위스킬을 찾아야함
    while True:
        length = len(upper)
        #print(upper, leaf)

        if length == 0:
            # 종료 조건
            break

        for idx in range(length):
            tmp = list(upper)
            ret = set(sp_map[tmp[idx]]) - leaf

            if len(ret) == 0:
                #x_count += len(sp_map[tmp[idx]])
                for sp in sp_map[tmp[idx]]:
                    x_count[tmp[idx] - 1] += x_count[sp - 1]
                #print('-'*10, x_count)

                upper.remove(tmp[idx])
                leaf.add(tmp[idx])

    axis = total_sp // sum(x_count)
    answer = [x * axis for x in x_count]
    return answer


if __name__ == "__main__":
    total_sp = 121
    skills = [[1,2], [1,3], [3,6], [3,4], [3,5]]

    s = solution(total_sp, skills)
    print(f"ret: {s}")
