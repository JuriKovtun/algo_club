data = input()


data_half = len(data) // 2
data_l = data[0:data_half]
data_r = data[data_half:len(data)]


if len(data) % 2 > 0:
    counter = 1
    for i in range(data_half):
        if data_r[i + 1] == data_l[data_half - 1 - i]:
            counter += 1
else:
    counter = 0
    for i in range(data_half):
        if data_r[i] == data_l[data_half - 1 - i]:
            counter += 1


print(counter)
