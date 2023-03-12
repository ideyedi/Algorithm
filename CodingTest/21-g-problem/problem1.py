def checkLogin(id, pw, auth):
    ret = False
    if auth[id] == pw:
        ret = True
    return ret

def solution(infos, actions):
    answer = []
    user = ""
    order_tbl = []
    auth = {}
    
    # init auth infos
    if infos:
        for inf in infos:
            tmp = inf.split(" ")
            auth[tmp[0]] = tmp[1]
    
    # Actions
    for act in actions:
        ls = act.split(" ")
        
        if ls[0] == "LOGIN":
            ret = checkLogin(ls[1], ls[2], auth)
            if ret and user == "":
                user = ls[1]
                answer.append(True)
            else:
                answer.append(False)
        
        elif ls[0] == "ADD":
            if user == "":
                answer.append(False)
            else:
                order_tbl.append(ls[1])
                answer.append(True)                
        
        elif ls[0] == "ORDER":
            if not order_tbl:
                answer.append(False)
            else:
                order_tbl = []
                answer.append(True)

    return answer