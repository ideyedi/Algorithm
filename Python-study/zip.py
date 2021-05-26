# /bin/python3
# Written by eyedi
# Built-in function 'zip()' description
print(zip.__doc__)

A = ['A', 'B', 'C', 'B']
B = [10, 20, 30, 40]

print('=' * 100)
# Convert zip object to list
print(list(zip(A,B)))

A.append('E')
print(A)
# A,B의 리스트 요소 갯수차이가 날 경우 
# 요소가 적은 리스트 기준으로 zippig 된다.
print(list(zip(A,B)))

print("=" * 100)
# 만약 dictionary를 zip 한다면 
# dictionary의 index와 rank list만 zipping
# 이는 zip object를 dictionary로 convert하여도 마찬가지이다.
dic = {
    1:"Chelsea",
    2:"Liverpool",
    3:"ManU",
    4:"ManCity"
}
rank = [1, 2, 3, 4, 5, 6]

print(dic.values())
print(list(zip(dic, rank)))
print(dict(zip(dic, rank)))
