A, B = input().split()

# 방법 1
# 문자 뒤집는 함수 rev 선언
def rev(a : str) :
    arr_a = list(a)
    rev_a = ''
    for i in range(len(arr_a)-1,-1,-1):
        rev_a += arr_a[i]
    return rev_a

# A, B를 뒤집은 rev_A, rev_B 선언
rev_A = int(rev(A))
rev_B = int(rev(B))

# 방법 2
# list를 다루듯이 문자열을 뒤집는 방법
# rev_A = int(A[::-1])
# rev_B = int(B[::-1])

# 방법 1
# 크기 비교 후 출력
if rev_A > rev_B :
    print(rev_A)
else :
    print(rev_B)

# 방법 2
# max함수를 활용하여 큰 값 출력하는 방식
# print(max(rev_A,rev_B))