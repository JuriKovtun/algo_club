# string = '5 2 3 1'

n, m, x, y = list(map(int, input().split()))

data = [['null' for i in range(m)] for i in range(n)]

counter = 0

for i in range(n):
    for j in range(m):

        if i % 2:
            direction = m - 1 - j
        else:
            direction = j

        data[i][direction] = counter
        counter += 1


print(data[x - 1][y - 1])
