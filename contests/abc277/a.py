from collections import defaultdict


# UnionFind
# uf = UnionFind(N)
#   N:ノード数（0~N-1)
# parents():各要素の親番号の番号を格納するリストを返す。要素が根(ルート)の場合は-(そのグループの要素数)を格納
# find(x):要素xが属するグループの根を返す
# union(x,y):要素xが属するグループと要素yが属するグループを併合する
# size(x):要素xが属するグループのサイズ（要素数）を返す
# same(x,y):要素xと要素yが同じグループに属するかどうかを返す
# members(x):要素xが属するグループに属する要素をリストで返す
# roots():全ての根の要素をリストで返す
# group_count():グループの数を返す
# all_group_members():dictで全てのグループの全ての要素を返す

class UnionFind():
    def __init__(self):
        self.parents = defaultdict(lambda: -1)

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
        return [i for i in range(len(self.parents)) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in self.parents:
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


# TODO:なにかやばいことになってたので修正予定
uf = UnionFind()
print(uf.parents)
uf.union(3, 4)
print(uf.parents)
uf.union(2, 3)
print(uf.parents.items())
print(uf.size(2))
print(uf.size(3))
print(uf.size(4))
uf.union(99, 143)
print(uf.all_group_members())
