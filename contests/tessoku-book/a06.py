N, Q = map(int, input().split())
A_L = list(map(int, input().split()))

accum_L = [0]
for a in A_L:
    accum_L.append(accum_L[-1] + a)

for i in range(Q):
    L, R = map(int, input().split())

    print(accum_L[R] - accum_L[L - 1])
