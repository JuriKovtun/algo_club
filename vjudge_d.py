
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input())
data = []
for i in range(n):
    e = int(input())
    data.append(e)

data.sort()

max_n = data[-1]

fib_series = [1, 2]

while fib_series[-1] <= max_n:
    f = fib_series[-1] + fib_series[-2]
    fib_series.append(f)

fib_length = len(fib_series)


def to_fib_list(nn):

    fi_index = ['0' for i in range(fib_length)]

    for i in range(fib_length - 1, -1, -1):
        e = fib_series[i]

        if e <= nn and fi_index[i + 1] == '0':
            fi_index[i] = '1'
            nn = nn - e

    return fi_index


for e in data:
    ind = to_fib_list(e)[::-1]
    ind = ''.join(ind)
    index = ind.find('1')
    ind = ind[index:]
    print(str(e) + ' = ' + ind + ' (fib)')












