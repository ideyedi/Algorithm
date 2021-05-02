#/bin/python3
# practice problem 

count = 7
i = 0
total = 0
min_num = 101

while i < count:
    num = int(input())
    # count total 
    if (num % 2) == 1:
        total += num

        # compare min
        if min_num > num:
            min_num = num
    
    # add count
    i += 1

if total != 0:
    print(total)
    print(min_num)
else:
    print(-1)
