a, b = map(int, input().split())
s=1
for _ in range(b):
    s*=a
print(s)