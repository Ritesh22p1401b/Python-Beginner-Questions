x= int(input('Enter the upper value:'))
y= int(input('Enter the lower value:'))
z= 10
a= 0
for i in range(z,y+1):
    rem = 0
    temp = i
    sum = 0
    while sum != 1 and sum != 2 and sum != 3 and sum != 4 and sum != 5 and sum != 6 and sum != 7 and sum != 8 and sum != 9:
        sum = 0
        while temp > 0:
            rem = temp % 10
            sum = sum + rem
            temp = temp // 10
        temp = sum

    if sum == 1:
        print(i)
        a+=1
print('Number between {} and {} is-{}'.format(x,y,a))

