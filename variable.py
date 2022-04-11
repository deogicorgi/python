# variable

n = 700

print(type(n))  # <class 'int'>

x = y = z = 700  # 동시선언
print(x, y, z)  # 700 700 700

# Object references
# 변수 값 할당 상태

# ex)
print(300)
# 1. 타입에 맞는 오브젝트 생성 300 -> int()
# 2. 값 생성 int(300)
# 3. 콘솔 출력 print

n = 700

m = n

# m -> 700 <- n
print(m, n)

# id(identity 확인)
m = 800
n = 600

print(id(m))
print(id(n))

# 값이 같을 경우 하나의 오브젝트로 판단
b = 800
print(id(b))
print(id(m))

# 다양한 변수 선언


