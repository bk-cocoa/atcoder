from collections import defaultdict
from collections import deque

N, M, K = map(int, input().split())
edge_d = defaultdict(list)
for i in range(M):
    u, v, a = map(int, input().split())
    if a == 1:
        edge_d[u].append(v)
        edge_d[v].append(u)
    else:
        edge_d[-u].append(-v)
        edge_d[-v].append(-u)
S_S = set(map(int, input().split()))

que = deque()
que.append(1)
inf = float('inf')
dist_d = defaultdict(lambda: inf)
dist_d[1] = 0

while que:
    now_pos = que.popleft()
    now_cost = dist_d[now_pos]
    if abs(now_pos) in S_S:
        for next_pos in edge_d[-now_pos]:
            if next_pos in dist_d:
                continue
            que.append(next_pos)
            dist_d[next_pos] = now_cost + 1

    for next_pos in edge_d[now_pos]:
        if next_pos in dist_d:
            continue
        que.append(next_pos)
        dist_d[next_pos] = now_cost + 1

ans_L = []

if dist_d[N] != inf:
    ans_L.append(dist_d[N])
if dist_d[-N] != inf:
    ans_L.append(dist_d[-N])

if len(ans_L) == 0:
    print(-1)
else:
    print(min(ans_L))
