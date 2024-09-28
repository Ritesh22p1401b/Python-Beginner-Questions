while True:
    n = int(input())
    if n == 6:
        break
    if n < 6:
        a = int(input())
        b = int(input())
        if n == 1:
            c = a + b
            print(c)
        elif n == 2:
            c = a - b
            print(c)
        elif n == 3:
            c = a * b
            print(c)
        elif n == 4:
            c = a / b
            print(c)
        elif n == 5:
            c = a % b
            print(c)
    else:
        print('Invalid Operation')
