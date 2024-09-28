x,y = map(str, input().split(' '))
x = int(x)
y = float(y)
if 0 < x <= 2000 and x+0.50 <=y:
    if x % 5 == 0:
        a = y-(x+0.50)
        w= format(a,'.2f')
        print(w)
else:
    print(y)


