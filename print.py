# print 사용법

# 기본 출력
# 싱글, 더블 쿼티를 가장 많이 사용함
print('Python start!')
print("Python start!")
print('''Python start!''')
print("""Python start!""")

# 줄바꿈
print()

# separator 사용
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')  # PYTHON
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')  # P,Y,T,H,O,N
print('P', 'Y', 'T', 'H', 'O', 'N', sep='    ')  # P    Y    T    H    O    N

print('010', '1234', '1234', sep='-')  # 010-1234-1234
print('python', 'google.com', sep='@')  # python@google.com

# end 사용
print('Welcome to', end=' ')  # Welcome to IT news Website
print('IT news', end=' ')
print('Website')

# file 사용
import sys

print('Learn Python', file=sys.stdout)  # 인수 위치로 write

# format 사용 (d, s, f)
print('%s %s' % ('one', 'two'))  # one two
print('{} and {}'.format('one', 'two'))  # one and two
print('{} and {}'.format('one', 2))  # one and 2
print('{1} {0}'.format('one', 'two'))  # two one

# %s

print('%10s' % ('nice'))  # nice
print('{:>10}'.format('nice'))  # nice

print('%-10s' % ('nice'))  # nice
print('{:_<10}'.format('nice'))  # nice______

print('{:_>10}'.format('nice'))  # ______nice
print('{:_^10}'.format('nice'))  # ___nice___

print('%.5s' % ('python study'))  # pytho
print('%5s' % ('python study'))  # python study
print('{:10.5}'.format('python study'))  # pytho

# %d

print('%d %d' % (1, 2))  # 1 2
print('{} {}'.format(1, 2)) # 1 2

print('%4d' % (42))  #   42
