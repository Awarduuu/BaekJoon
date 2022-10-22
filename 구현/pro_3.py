k = input()

# 유니코드 변환 후 시작점인 a의 변환 정수를 뺀 다음 1 더해주기 -> a~h => 1~8로 변환
col = int(ord(k[0])) - int(ord('a')) + 1
# 1~8 정수로 변환
row = int(k[1])

# 계산될 경우의 수
count = 0

# 이동할 모든 경우의 수
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]

# 모든 경우의 수에 대하여 브루트포스
for step in steps :
    # 이동될 다음 단계들
    next_row = row + step[0] 
    next_col = col + step[1]
    # 이동될 다음 단계들이 모두 체스판에 존재한다면 이 경우의 수를 선택
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :
        # 경우의 수에 1 더하기
        count += 1

print(count)