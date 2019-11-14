def get_data():

    output = [[0, 0]]

    n = int(input())
    for i in range(n):
        a, b = input().split()
        a = int(a)
        b = int(b)
        output[0][0] += a
        output[0][1] += b
        output.append([a, b])

    return output


data = get_data()


def check_beauty():
    diff = abs(data[0][0] - data[0][1])
    counter = 0
    max_i = 0

    for i in range(1, len(data)):
        a = data[0][0] - data[i][0]
        b = data[0][1] - data[i][1]
        c = a + data[i][1]
        d = b + data[i][0]
        gain = abs(c - d)

        if gain > diff and gain > counter:
            counter = gain
            max_i = i

    return max_i


answer = check_beauty()
print(answer)




