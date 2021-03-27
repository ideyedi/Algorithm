#/bin/python3
# practice problem 4

an_a = int(input())
an_b = int(input())
an_c = int(input())

angle_total = an_a + an_b + an_c
if an_a == 60 and an_b == 60 and an_c == 60:
    print('Equilateral')
elif angle_total == 180:
    if an_a == an_b or an_b == an_c or an_a == an_c:
        print('lsosceles')
    else:
        print('Scalene')
else:
    print('Error')
