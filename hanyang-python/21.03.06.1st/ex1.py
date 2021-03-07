#/bin/python3

num_a, num_b = input().split()
 
if num_a > num_b:
    print(">")
elif num_a < num_b:
    print("<")
else :
    print("==")
