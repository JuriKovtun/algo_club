n, m = list(map(int, input().split()))


connections = {}
answer = {
    'true': 'POSSIBLE',
    'false': 'IMPOSSIBLE'
}


def add_to_set(a, b):
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = {b}

    if b in connections:
        connections[b].add(a)
    else:
        connections[b] = {a}


for i in range(m):
    a, b = list(map(int, input().split()))
    add_to_set(a, b)


for e in connections[1]:
    if e in connections[n]:
        print(answer['true'])
    else:
        print(answer['false'])


















