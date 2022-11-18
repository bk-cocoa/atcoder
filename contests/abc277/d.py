from collections import Counter
from collections import defaultdict


# 辞書型UnionFind
# 植林：UnionFind()
# add(x):自身を根とする要素xを追加する
# parents():各要素の親番号の番号を格納するリストを返す。要素が根(ルート)の場合は-(そのグループの要素数)を格納
# find(x):要素xが属するグループの根を返す
# union(x,y):要素xが属するグループと要素yが属するグループを併合する
# size(x):要素xが属するグループのサイズ（要素数）を返す
# same(x,y):要素xと要素yが同じグループに属するかどうかを返す
# members(x):要素xが属するグループに属する要素をリストで返す
# roots():全ての根の要素をリストで返す
# group_count():グループの数を返す
# all_group_members():dictで全てのグループの全ての要素を返す

class UnionFind:
    def __init__(self):
        self.parents = defaultdict(lambda: -1)

    def add(self, x):
        return self.parents[x]

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in self.parents if self.find(i) == root]

    def roots(self):
        return [i for i, x in self.parents.items() if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in self.parents:
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M = map(int, input().split())
A_L = list(map(int, input().split()))

A_L.sort()
A_sum = sum(A_L)
c = Counter(A_L)

uf = UnionFind()
for a in A_L:
    uf.add(a)

for i in range(1, N):
    if A_L[i] - A_L[i - 1] <= 1:
        uf.union(A_L[i], A_L[i - 1])

if A_L[-1] == M - 1 and A_L[0] == 0:
    uf.union(0, M - 1)

score = 0
for k, v in uf.all_group_members().items():
    score = max(score, sum([i * c[i] for i in v]))
ans = A_sum - score

print(ans)
