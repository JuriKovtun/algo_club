data = []
fib_series = [1, 2]

# input here
n = int(input())

for i in range(n):
    m = int(input())
    while m >= fib_series[-1]:
        fib_series.append(fib_series[-1] + fib_series[-2])
    data.append(m)


def convert(m_):
    output = []
    index = 0

    for i in range(len(fib_series) - 1, -1, -1):

        if fib_series[i] <= m_:
            # and not output[-1]
            output.append('1')
            m_ -= fib_series[i]

            if not index:
                index = i + 1

        else:
            output.append('0')

    output = output[-index:len(output)]
    cut_string = ''.join(output)

    return cut_string


for e in data:
    result = convert(e)
    answer = '' + str(e) + ' = ' + result + ' (fib)'

    print(answer)
