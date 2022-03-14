N = int(input())

for i in range(N) :
    # 값 초기화
    k =0 ; sum = 0
    # 새로운 값 입력
    quiz = input()

    # 알고리즘
    for j in quiz :
        if j == "O" :
            k += 1
            sum += k
        elif j == "X" :
            k = 0
            sum += k
    
    print(sum)
    