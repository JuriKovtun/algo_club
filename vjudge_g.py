

# data = list(map(int, input().split()))

data = [1, 2, 3, 4]
cases = ['TRIANGLE', 'SEGMENT', 'IMPOSSIBLE']

data.sort()

sums = [
    data[0] + data[1],
    data[1] + data[2]
]

if data[3] < sums[1] or data[2] < sums[0]:
    print(cases[0])

elif data[2] == sums[1] or data[2] == sums[0]:
    print(cases[1])

else:
    print(cases[2])

