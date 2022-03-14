import sys
N = int(sys.stdin.readline())

# list() 함수를 통해 리스트 형식으로 변환
# map() 함수를 통해 공백으로 구분해서 리스트에 넣기
A = list(map(int,sys.stdin.readline().split()))


# 리스트 최대, 최소 구하는 함수 : max, min
large = max(A)
small = min(A)

print(small, large)
