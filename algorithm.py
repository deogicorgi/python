import sys
from collections import Counter

data = [int(sys.stdin.readline().strip()) for i in range(3)]

num = 1
for i in data:
    num *= i

strnum = str(num)

ll = [[k] * v for k, v in Counter(strnum).items()]

for i in range(0, 10):
    isPrint = False
    for v in ll:
        if str(i) in v:
            print(len(v))
            isPrint = True
            break
    if not isPrint:
        print(0)
