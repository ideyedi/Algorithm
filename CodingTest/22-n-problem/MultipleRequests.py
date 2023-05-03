## read the string filename
from collections import Counter

filename = input()
multi_req = []

with open(filename, 'r') as f:
    for i in f.readlines():
        logs = i.split(" ")
        #print(logs[3][1:])
        multi_req.append(logs[3][1:])

    dup_req = Counter(multi_req)
    #print(dup_req)
    result = [l for l in dup_req if dup_req.get(l) > 1]

req_filename = "req_" + filename
with open(req_filename, 'w') as f:
    for item in result:
        f.write(item + '\n')

#with open(req_filename, 'r') as f:
#    for i in f.readlines():
#        print(i)