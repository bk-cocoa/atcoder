# A05 - Three Cards
N, K = map(int, input().split())

ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        c = K - (a + b)
        if 1 <= c <= N:
            ans += 1
print(ans)
