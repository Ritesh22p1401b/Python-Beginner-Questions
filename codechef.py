t = int(input())
for j in range(t):
    l = input().split()
    l1 = input().split()
    l3 = []
    i = 0
    while i < len(l):
        w = 0
        while w < len(l1):
            if l[i] == l1[w]:
                l3.append(l1[w])
                w += 1
            else:
                w += 1
        i += 1
    print(l3[0])
