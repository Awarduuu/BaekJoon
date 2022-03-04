# # 입력
A, B = map(int, input().split())
# # if문
if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")

# 숏코딩
# print(['><'[A<B],'=='][A==B])