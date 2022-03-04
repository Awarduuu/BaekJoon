H, M = map(int, input().split())
C = int(input())


# 방법 1
# ex) C = 80 이면 C_d = 1, C_q = 20 으로 선언
# 분을 60으로 나눈 시간
C_d = C // 60

# 분을 60으로 나눈 나머지
C_q = C % 60

# 첫번째 조건기준 (분) : 분이 60을 넘어갈때
if M + C_q >= 60 :
    # 두번째 조건기준 (시) : 시가 24를 넘어갈때
    if H + C_d + 1 < 24 :
        print(H + C_d + 1, M + C_q - 60)
    else :
        print(H + C_d + 1 - 24, M + C_q - 60)
else :
    if H + C_d < 24 :
        print(H + C_d, M + C_q)
    else :
        print(H + C_d - 24, M + C_q)

# 방법 2
# if H+((M+C)//60) < 24 :
#     print(H+((M+C)//60), (M+C)%60)
# else :
#     print((H+((M+C)//60)-24), (M+C)%60)

# # 오류 코드 -> 조건 기준 벤다이어그램 이해 필요
# # if H + C_d < 24 :
# #     if M + C_q >= 60 :
# #         print(H + C_d + 1, M + C_q - 60)
# #     else :
# #         print(H + C_d, M + C_q)
# # else :
# #     if M + C_q >= 60 :
# #         print(H + C_d + 1 - 24, M + C_q - 60)
# #     else :
# #         print(H + C_d - 24, M + C_q)