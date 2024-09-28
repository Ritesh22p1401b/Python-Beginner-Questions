x = int(input('enter the number:'))
p = 5
for i in range(x):
    for j in range(i+1):
        print(p,end='')
    p -= 1
    print()
