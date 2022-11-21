from collections import deque

N, K = map(int, input().split())
A_L = list(map(int, input().split()))
que = deque(A_L)

for i in range(K):
    que.popleft()
    que.append(0)
print(*que)
