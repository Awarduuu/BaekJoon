# set 자료형은 중복이 허용 되지 않고, 순서가 없는 특징을 가지고 있다.
# 1~10000까지 전체 집합
natural_n = set(range(1,10001))

# 생성자 있는 수 들어갈 집합
general_n = set()

# 생성자 있는 수 구하는 함수
def d(n) :
    for i in str(n) :
        n += int(i)
    return n

# 1~10000까지 생성자 있는 수 집합에 넣기
for i in range(1,10001) :
    general_n.add(d(i))

# 전체 - 생성자 있는 수 -> 정렬
self_n = sorted(natural_n - general_n)

# 브루트포스 알고리즘
for i in self_n :
    print(i)