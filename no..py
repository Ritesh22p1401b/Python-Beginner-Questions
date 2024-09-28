x= 'internationalization'
z = len(x)
if z > 10:
    map = {}
    for i in range(z):
        if x[i] in map :
            map[x[i]]+1
        else:
           map[x[i]] = i
    a= len(map)
    print(a)

