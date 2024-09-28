x= 1
y=1
z=2
n=3
l = list()
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if x+y+z!=n:
                l.append([i,j,k])

print(l)