T = int(input())
N = int(input())

accum_L = [0] * (T + 10)
for i in range(N):
    L, R = map(int, input().split())
    accum_L[L] += 1
    accum_L[R] -= 1
ans_L = [0]

for accum in accum_L:
    ans_L.append(ans_L[-1] + accum)
print(*ans_L[1:T + 1])
