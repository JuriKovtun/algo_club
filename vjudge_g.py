# data = [1, 2, 3, 4]


data = list(map(int, input().split()))

cases = ['TRIANGLE', 'SEGMENT', 'IMPOSSIBLE']

data.sort()

a = data[0] + data[1]
b = data[1] + data[2]


if a > data[2] or b > data[3]:
    print(cases[0])

elif a == data[2] or b == data[3]:
    print(cases[1])

else:
    print(cases[2])

