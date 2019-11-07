# n = int(input())
# l = list(map(int, input().split()))

# a = 0
#
# b = 0
#
# print(a, b)


data = [30, 27, 31, 25, 32, 29, 25, 30]


# n = int(input())
# l = input().split()


# l = list(map(int, input().split()))

# a, b = list(map(int, input().split()))


milk = 0
pie_count = 0

for i in range(len(data)):

    if data[i] < 30:
        milk += 200
        pie_count += 1

packages = milk // 900 + 1
print(packages, pie_count)





