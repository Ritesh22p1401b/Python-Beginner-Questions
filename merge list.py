arr1=[1,2,4]
arr2=[1,3,4]
x=len(arr1)
y=len(arr2)
arr3=[]
i=0
while i<x:
    a=arr1[i]
    b=arr2[i]
    j=i+i
    while j<=(i+i):
        arr3.insert(j,a)
        arr3.insert(j+1,b)
        j+=1
    i+=1

print(arr3)
