n, m = list(map(int, input().split()))


connections = dict()
answer = 'IMPOSSIBLE'


def add_to_set(a, b):
    if a in connections:
        connections[a].add(b)
    else:
        connections[a] = set([b])

    if b in connections:
        connections[b].add(a)
    else:
        connections[b] = set([a])


for i in range(m):
    a, b = list(map(int, input().split()))
    add_to_set(a, b)

island_1 = connections.get(1)
island_N = connections.get(n)


for e in island_1:
    if island_N and e in island_N:
        answer = 'POSSIBLE'

print(answer)


















