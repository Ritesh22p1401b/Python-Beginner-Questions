s = int(input())
e = int(input())
w = int(input())
d = 0
while s <= e:
    a = s-32
    b = a*5
    if b < 0:
        x = abs(b)
        c = x//9
        d = 0-c
    elif b > 0 or b == 0:
        d = b//9
    print(s, d)
    s = s+w




