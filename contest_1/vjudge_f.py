# size = 5

size = int(input())

output = [['2' for i in range(size)] for j in range(size)]

for i in range(size):
    output[i][size - 1 - i] = '0'

for i in range(1, size):
    for j in range(size - i, size):
        output[i][j] = '1'

for e in output:
    print(''.join(e))
