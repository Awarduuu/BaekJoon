def solution(s):
    answer = ''
    answer_1 = ''
    toss = ''
    s = s.lower()
    alp = 'abcdefghijklmnopqrstuvwxyz'
    count = [0] * len(alp)
    
    for i in s :
        index = alp.index(i)
        count[index] += 1
    

    for i in range(len(count)-1):
        if count[i] == max(count) :
            answer += alp[i]

    for i in answer :
        if i == 't' or i == 'o' or i == 's':
            answer = answer.replace(i, '')
            toss += i

    for i in 'tos' :
        if i in toss :
            if i == 't' or i == 'o':
                answer_1 += i.upper()
            else :
                answer_1 += i.upper() * 2
    
    answer = answer_1 + answer
    return answer


s = input()

print(solution(s))