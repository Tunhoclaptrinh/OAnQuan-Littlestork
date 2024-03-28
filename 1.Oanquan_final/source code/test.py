import math
x = int(input('Nhập vào số của bạn: '))
z = ""
dodai = len(str(x))

print('d', dodai)
for i in range(1,dodai + 1):
    print('i',i)
    y = int(x % (10**i))
    z += str(str(y)[0])

print(z)