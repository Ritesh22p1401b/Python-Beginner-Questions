n=int(input())
k=(n*2)-1
a=[[0 for i in range(k)] for j in range(k)]
value=n
low=0
high=k-1

for i in range(n):
    for j in range(low,high+1):
        a[i][j]=value
    for j in range(low+1,high+1):
        a[j][i]=value
    for j in range(low+1,high+1):
        a[high][j]=value
    for j in range(low+1,high):
        a[j][high]=value
    low=low+1
    high=high-1
    value-=1

for i in range(0,k):
    for j in range(0,k):
        print(a[i][j],end=" ")
    print()
