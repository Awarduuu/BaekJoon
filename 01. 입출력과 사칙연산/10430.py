# 값 할당
A, B, C = input().split()
A = int(A) ; B = int(B); C = int(C)
# 함수 설정
def cal(x,y,z) :
    print((x+y)%z)
    print(((x%z)+(y%z))%z)
    print((x*y)%z)
    print(((x%z)*(y%z))%z)
# 함수 적용
cal(A,B,C)