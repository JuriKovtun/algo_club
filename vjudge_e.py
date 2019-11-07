# string = '1 25 2'
# string = '25 1 2'

string = input()

data = string.split()
quantity = int(data[2])
if len(data[1]) == 1:
    n = '0' + data[1]
    data[1] = n


price = int(data[0] + data[1])
total = price * quantity
hrn = total // 100
kop = total % 100


print(hrn, kop)
