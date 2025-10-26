a, o, c = input().split()
a = int(a)
c = int(c)

if o == "+":
    result = a + c
elif o == "-":
    result = a - c
elif o == "*":
    result = a * c
elif o == "/":  
    result = a / c
else:
    print("False")
    exit()

print(f"{a} {o} {c} = {result}")
