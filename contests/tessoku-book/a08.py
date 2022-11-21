H, W = map(int, input().split())
L = []
for i in range(H):
    L.append(list(map(int, input().split())))

accum_L = [[0] * (W + 1) for i in range(H + 1)]
for i in range(H):
    for j in range(W):
        accum_L[i + 1][j + 1] = accum_L[i + 1][j] + L[i][j]
for j in range(W):
    for i in range(H):
        accum_L[i + 1][j + 1] = accum_L[i][j + 1] + accum_L[i + 1][j + 1]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    ans = accum_L[C][D] - accum_L[A - 1][D] - accum_L[C][B - 1] + accum_L[A - 1][B - 1]
    print(ans)
