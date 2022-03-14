num = []
x = []
N = 0

for i in range(10) :
    num.append(int(input()))
    x.append(num[i] % 42)

# 배열 중복 제거
# 중복 안되는 나머지 값 넣을 리스트 생성
n_x = []

for i in x :
    # 중복이 안되면 n_x에 append
    if i not in n_x :
        n_x.append(i)

print(len(n_x))

