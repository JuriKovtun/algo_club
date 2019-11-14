n, m = list(map(int, input().split()))

counter = 0
limit = int(1e3)
while n != m and counter < limit:

    if n < m:
        m = m - n
        n = 2 * n

    else:
        n, m = m, n

    counter += 1


if counter == limit:
    print(0)
else:
    print(1)
