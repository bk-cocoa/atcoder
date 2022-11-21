H, W, N = map(int, input().split())

accum_L = [[0] * (W + 2) for i in range(H + 2)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    accum_L[A][B] += 1
    accum_L[A][D + 1] -= 1
    accum_L[C + 1][B] -= 1
    accum_L[C + 1][D + 1] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        accum_L[i][j] += accum_L[i][j - 1] + accum_L[i - 1][j] - accum_L[i - 1][j - 1]

for row in accum_L[1:-1]:
    print(*row[1:W + 1])
