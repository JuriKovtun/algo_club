n = 4

# n = int(input())

if n == 2:
    print(0)

series = n - 2


def sum_of(n):
    return (n * (1 + n)) // 2


options = sum_of(series) * 2

print(options)


# 3 - 1
# 4 : 2 + 1
# 5 : 3 + 2 + 1
# 6 : 4 + 3 + 2 + 1
