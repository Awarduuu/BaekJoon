# 입력
n_1,n_2,n_3 = map(int, input().split())

# 출력 할 값
sum = 0
# 세 수가 모두 같을 때
if n_1 == n_2 == n_3 :
    sum = 10000 + n_1 * 1000
    print(sum)
# 두 수만 같을 때
elif n_1 == n_2 or n_1 == n_3 :
    sum = 1000 + n_1 * 100
    print(sum)
elif n_2 == n_3 :
    sum = 1000 + n_2 * 100
    print(sum)
# 모두 다를 때
else :
    list = [n_1, n_2, n_3]
    sum = max(list) * 100
    print(sum)
