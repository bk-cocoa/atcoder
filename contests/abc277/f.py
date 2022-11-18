class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


H, W = map(int, input().split())
grid_L = []
tentou_L = []
min_max_L = []
for i in range(H):
    grid_L.append(list(map(int, input().split())))

    bit = Bit(H * W + 10)
    tmp = grid_L[-1]
    bit_sum = 0
    tmp_L = []

    min_num = 10 ** 19
    max_num = -1
    for num in tmp:
        if num != 0:
            tmp_L.append(num)
            min_num = min(min_num, num)
            max_num = max(max_num, num)

    min_max_L.append([min_num, max_num])

    if len(tmp_L) == 0 or len(tmp_L) == 1:
        continue

    for i, num in enumerate(tmp_L):
        if num == 0:
            continue
        bit_sum += i - bit.sum(num - 1)
        bit.add(num, 1)

    tentou_L.append(bit_sum)

if len(set(tentou_L)) != 1:
    print('No')
    exit()
min_max_L.sort()
for i in range(1, len(min_max_L)):
    if min_max_L[i - 1][1] > min_max_L[i][0]:
        print('No')
        exit()
print('Yes')
