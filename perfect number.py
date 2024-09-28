x = int(input('Enter The Number:'))
for i in range(x):
    if i*i == x:
        print('number is perfect')
        break
else:
    print('number is not perfect')
