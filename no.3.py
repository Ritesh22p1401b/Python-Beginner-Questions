(n,k) = 8 ,5
if 1 <= n <= 50 and k <= n:
    a = ['10','9','8','7','6','6','5','5']
    count= 0
    for i in a:
        for j in a[1:]:
            if a[j]>k:
                count+=1

print(count)







