a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    s = str(i)
    if (('3' in s) or ('6' in s) or ('9' in s)) or (i % 3 == 0):
        cnt += 1

print(cnt)
