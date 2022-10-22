def solution(n,m):
    answer = 0
    max = 1000000000
    d = [0] * (max + 1)

    if(max(d) <= 3) :
        for i in range(1, max+1) :
            for j in range(i, max+1, i) :
                d[j] += 1

    div_2 =[]
    div_3 =[]
    div_4 =[]

    for i in range(max+1) :
        if d[i] == 2 :
            div_2.append(d[i])
        elif d[i] == 3 :
            div_3.append(d[i])
        elif d[i] == 4 :
            div_4.append(d[i])

    if n == 2 :
        answer = div_2[m+1]
    elif n == 3 :
        answer = div_3[m+1]
    elif n == 4 :
        answer = div_4[m+1]
    return answer

