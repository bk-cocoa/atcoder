from collections import defaultdict

N = int(input())
A_L = list(map(int, input().split()))

add_cnt = 0

Q = int(input())
Q_L = []
add_d = defaultdict(int)

is_reset = False

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        start_num = query[1]
        add_d = defaultdict(int)
        is_reset = True
    if query[0] == 2:
        i = query[1] - 1
        x = query[2]
        add_d[i] += x

    if query[0] == 3:
        i = query[1] - 1
        if is_reset:
            print(start_num + add_d[i])
        else:
            print(A_L[i] + add_d[i])
