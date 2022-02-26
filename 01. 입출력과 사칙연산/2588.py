# 내 코드
# A = int(input()) ; B = int(input())
# B_1 = B % 100 ; 
# B_a = int(B / 100) ; B_b = int(B_1 / 10); B_c = B_1 % 10  

# print(A*B_c)
# print(A*B_b)
# print(A*B_a)
# print(A*B)

# map func 이용
# 입력
a,b = map(int, input().split())
#출력
print(b%10*a,b%100//10*a,b//100*a,b*a)