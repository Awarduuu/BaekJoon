N = int(input())

# 총 경우의 수 = count
count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)