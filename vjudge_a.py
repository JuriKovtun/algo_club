# Input example
# 8
# 30 27 31 25 32 29 25 30


n = int(input())
data = list(map(float, input().split()))

milk = 0
pie_count = 0

for i in range(n):

    if data[i] < 30:
        milk += 200
        pie_count += 1

packages = milk // 900 + (milk % 900 > 0)

print(packages, pie_count)
