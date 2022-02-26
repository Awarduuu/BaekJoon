# 입력
A, B = input().split()

# 정수 변환
A = int(A)
B = int(B)

# 사칙연산 함수 선언
def calculate(x,y) :
    print(x+y)
    print(x-y)
    print(x*y)
    print(int(x/y))
    print(x%y)

# 함수 적용
calculate(A,B)