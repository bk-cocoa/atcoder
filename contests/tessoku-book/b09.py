N = int(input())
accum_L = [[0] * 1501 for i in range(1501)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    accum_L[A][B] += 1
    accum_L[C][D] += 1
    accum_L[A][D] -= 1
    accum_L[C][B] -= 1

for row in range(1501):
    for col in range(1, 1501):
        accum_L[row][col] += accum_L[row][col - 1]
for row in range(1, 1501):
    for col in range(1501):
        accum_L[row][col] += accum_L[row - 1][col]

ans = 0
for row in accum_L:
    for col in row:
        if col > 0:
            ans += 1
print(ans)
