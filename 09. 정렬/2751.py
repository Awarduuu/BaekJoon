# 퀵정렬로 구현
import sys

N = int(input())
list = []
for _ in range(N):
    list.append(int(sys.stdin.readline()))

for i in sorted(list) :
    print(i)

# 이런거 쓰면 백준에선 시간초과네... 그래도 공부잘했다.
# def quick(list) :
#     if(len(list) <= 1) :
#         return list
#     pivot = list[0]
#     tail = list[1:]
#     pivot_left = [x for x in tail if x <= pivot]
#     pivot_right = [x for x in tail if x > pivot]

#     return quick(pivot_left) + [pivot] + quick(pivot_right)

# ans = quick(list)

# for i in ans:
#     print(i)