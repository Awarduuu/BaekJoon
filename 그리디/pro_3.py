from collections import Counter


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in arr : # 공포도가 낮은 모험가부터 하나씩 확인하며
    count += 1 # 그룹에 포함시킨다음
    if count >= i : # 공포도보다 그룹에 포함된 모험가 수가 높으면
        result += 1 # 그룹짓기를 마무리하고, 총 그룹 수를 늘리기
        count = 0 # 다시 그룹을 지어야 하기 때문에 현재 그룹에 포함된 모험가 수 초기화
    
print(result) # 총 그룹의 수 출력

 
