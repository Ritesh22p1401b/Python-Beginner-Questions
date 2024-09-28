n= 17
w = len(str(bin(n))[2:])
for i in range(1, n + 1):
    print(str(i).rjust(w, ' '), oct(i)[2:].rjust(w, ' '), hex(i).upper()[2:].rjust(w, ' '), bin(i)[2:].rjust(w, ' '))














