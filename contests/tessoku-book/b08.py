N = int(input())

L = [[0] * 1501 for i in range(1501)]

for i in range(N):
    X, Y = map(int, input().split())
    L[X][Y] += 1
accum_L = [[0] * 1505 for i in range(1505)]

for i in range(1, 1501):
    for j in range(1, 1501):
        accum_L[i][j] = accum_L[i][j - 1] + L[i][j]

for j in range(1, 1501):
    for i in range(1, 1501):
        accum_L[i][j] = accum_L[i - 1][j] + accum_L[i][j]

for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    ans = accum_L[c][d] - accum_L[a - 1][d] - accum_L[c][b - 1] + accum_L[a - 1][b - 1]
    print(ans)
