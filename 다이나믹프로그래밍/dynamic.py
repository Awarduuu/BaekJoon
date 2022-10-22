# 피보나치 함수를 재귀함수로 표현
# 단, 단순 재귀 함수로 해결하면 지수 시간 복잡도를 가지게 되므로 매우 비효율적
def fibo(x):
    # A1 = 1, A2 = 1
    if x == 1 or x == 2 :
        return 1
    # An = A(n-1) + A(n-2)
    return fibo(x-1) + fibo(x-2)


