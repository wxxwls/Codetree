n = int(input())
original_n = n  
ssum = 0

while n > 0:
    ssum += n % 10
    n //= 10

if original_n % 2 == 0 and ssum % 5 == 0:
    print("Yes")
else:
    print("No")
