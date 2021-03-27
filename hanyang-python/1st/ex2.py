#/bin/python3
# practice problem 2

def determine_grade(point):
    if point <= 100 and point >= 90:
        return 'A'
    elif point < 90 and point >= 80:
        return 'B'
    elif point < 80 and point >= 70:
        return 'C'
    elif point < 70 and point >= 60:
        return 'D'
    else:
        return 'F'

def __init__():
    point = int(input())
    grade = determine_grade(point)
    print(grade)




__init__()
