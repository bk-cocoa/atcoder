from collections import deque

N, K = map(int, input().split())
A_L = list(map(int, input().split()))

ans = 0
que = deque()
for a in A_L:
    que.append(a)
    ans += len(que) - 1

    while True:
        if len(que) < 2:
            break
        if que[-1] - que[0] <= K:
            break
        que.popleft()
        ans -= 1
print(ans)
