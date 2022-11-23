from collections import deque

N, K = map(int, input().split())
A_L = list(map(int, input().split()))

ans = 0
que = deque()
sum = 0
for a in A_L:

    que.append(a)
    sum += a
    ans += len(que) - 1
    while True:
        if sum <= K:
            break
        sum = sum - que.popleft()
        ans -= 1

print(ans + N)
