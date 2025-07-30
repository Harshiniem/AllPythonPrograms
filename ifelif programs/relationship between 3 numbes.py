a = int(input())
b = int(input())
c = int(input())
if a == b and b == c:
    print("All are equal")
elif a>b and a>c:
    print("a is max")
elif b>c:
    print("b is max")
else:
    print("c is max")