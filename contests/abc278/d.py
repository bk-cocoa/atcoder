from collections import defaultdict

N = int(input())
A_L = list(map(int, input().split()))
add_d = defaultdict(int)
for i, a in enumerate(A_L):
    add_d[i] = a

Q = int(input())
base = 0
for i in range(Q):
    q, *query = list(map(int, input().split()))

    if q == 1:
        add_d = defaultdict(int)
        base = query[0]

    if q == 2:
        add_d[query[0] - 1] += query[1]

    if q == 3:
        print(add_d[query[0] - 1] + base)
