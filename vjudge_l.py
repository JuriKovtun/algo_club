multiplier = int(input())


def sum_digits(n):
    a = n % 10
    bb = n % 100
    b = bb // 10
    c = n // 100
    return a + b + c


counter = 0

for i in range(10, 100):

    s = sum_digits(i)
    new_i = i * multiplier
    new_s = sum_digits(new_i)

    if s == new_s:
        counter += 1

print(counter)


