# 프로그래머스 '가장 큰 수' 문제

numbers = [3, 30, 34, 5, 9]

def function(numbers):
    # map 함수로 numbers의 인자들을 문자화 하고, 따로 리스트로 만들었다. 
    numbers_str = list(map(str, numbers))
    # 세자리수로 맞추어 정렬
    numbers_str.sort(key=lambda x:x*3, reverse=True) 
    # 형변환 후 answer 저장 
    answer = str(int(''.join(numbers_str)))  
    return answer
print(function(numbers))