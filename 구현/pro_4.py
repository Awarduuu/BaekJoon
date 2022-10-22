x = input()

# 문자 저장할 리스트
lan = []

# 숫자 계산할 변수
num = 0

# 문자를 하나씩 확인하여
for i in x :
    # 문자가 알파벳이면
    if i.isalpha():
        # 리스트에 삽입
        lan.append(i)
    # 알파벳이 아니면
    else :
        # 숫자는 따로 더하기
        num += int(i)
        
# 알파벳을 오름차순으로 정렬
lan.sort()

# 숫자가 있다면, 더한값을 가장 뒤에 삽입
if num != 0 :
    lan.append(str(num))

# 리스트를 문자열로 반환하여 출력
print(''.join(lan))