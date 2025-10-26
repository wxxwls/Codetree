a, b = map(int, input().split())
ssum=0
def is_prime(n):
    if n < 2:
        return False  
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


for i in range(a,b+1):
    if is_prime(i):
        ssum += i
print(ssum)
# Please write your code here.