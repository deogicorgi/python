# datatype

"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전
"""

str1 = "Python"
str2 = "Anaconda"

myList = [str1, str2]

print(myList)

dict1 = {
    "name": "Machine Learning",
    "version": 2.0
}

print(dict1)
print(type(dict1))
print(type(myList))

tuple1 = (1, 2, 3, 4)
tuple2 = 1, 2, 3, 4
set1 = {1, 2, 3}

print(type(tuple1))
print(type(tuple2))
print(type(set1))

i = 78
i2 = 7

print(i / i2)
print(i // i2)
print(i % i2)

f = -5.1342341
print(abs(f))

print(pow(2, 3))

a = 3.
b = 6
c = .7

print(type(a))
print(type(b))
print(type(c))

print(int(a))
print(float(b))

x, y = divmod(100, 8)
print(x, y)

import math

print(math.pi)

