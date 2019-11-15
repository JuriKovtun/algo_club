# a = 'qwertyuiopasdfghjklzxcvbnm'
# b = 'veamhjsgqocnrbfxdtwkylupzi'
# c = 'TwccpQZAvb2017'

a = input()
b = input()
c = input()

layout_dict = dict()
answer = ''

for i, e in enumerate(a):
    layout_dict[e] = b[i]
    layout_dict[e.upper()] = b[i].upper()

for e in c:
    output = layout_dict.get(e)
    if output:
        answer += output
    else:
        answer += e

print(answer)




