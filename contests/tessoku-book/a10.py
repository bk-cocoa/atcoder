N = int(input())
A_L = list(map(int, input().split()))

accum_L = [0] * (N + 1)
accum_R = [0] * (N + 1)

for i, a in enumerate(A_L, 1):
    accum_L[i] = max(a, accum_L[i - 1])

for i, a in enumerate(A_L[::-1], 2):
    accum_R[-i] = max(a, accum_R[-i + 1])

D = int(input())
for i in range(D):
    L, R = map(int, input().split())
    max_L = accum_L[L - 1]
    max_R = accum_R[R]
    print(max(max_L, max_R))
