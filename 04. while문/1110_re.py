# 초기값 설정
# 루프 확인 값
N = 0
# 입력값
# ex) 26
num = int(input())
# 새로운 숫자
num_1 = num
while True :
    a = num_1 // 10 # 10의 자리수 ex) "2"
    b = num_1 % 10 # 1의 자리수 ex) "6"
    c = a + b # ex) "8"
    d = b * 10 # ex) "60"
    e = c % 10 # ex) "8"
    num_1 = d + e # ex) "68"
    # 루프 확인 값 1 증가
    N += 1
    # 새로운 숫자가 입력값과 같을 때 while loop 종료
    if num_1 == num :
        break

# 루프 확인값 출력
print(N)