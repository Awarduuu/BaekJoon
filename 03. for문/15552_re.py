import sys

# 빠른 입력
# input() 대신 sys.stdin.readline()을 사용하여 입력받는다.
n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    print(a+b)