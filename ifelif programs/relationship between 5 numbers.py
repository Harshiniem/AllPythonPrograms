a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a==b and b==c and c==d and d==e:
    print("All are equal")
elif a>b and a>c and a>d and a>e:
    print("a is max")
elif  b>c and b>d and b>e:
    print("b is max")
elif c>d and c>e:
    print("c is max")
elif d>e:
    print("d is max")
else:
    print("e is max")