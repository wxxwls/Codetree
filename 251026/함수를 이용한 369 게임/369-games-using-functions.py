a, b = map(int, input().split())
cnt=0
def tsn(n):
    global cnt
    if (n//10)==3:
        cnt+=1
    elif (n%10)==3:
        cnt+=1
    elif (n//10)==6:
        cnt+=1
    elif (n%10)==6:
        cnt+=1
    elif (n//10)==9:
        cnt+=1
    elif (n%10)==9:
        cnt+=1
    elif (n%3)==0:
        cnt+=1

for i in range(a,b+1):
    tsn(i)
print(cnt)