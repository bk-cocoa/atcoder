from collections import Counter


class Accumulate_2d:
    def __init__(self, num):
        self.acc_2d = [[0] * (W + 1)]
        for i in range(H):
            acc_1d = [0]
            for j in range(W):
                acc_1d += [acc_1d[-1] + (A[i][j] == num)]
            self.acc_2d.append(acc_1d)
            for j in range(W + 1):
                self.acc_2d[i + 1][j] += self.acc_2d[i][j]

    def query(self, sx, sy):
        tx, ty = sx + P, sy + Q
        ac2d = self.acc_2d
        res = ac2d[tx - 1][ty - 1] + ac2d[sx - 1][sy - 1]
        res -= ac2d[sx - 1][ty - 1] + ac2d[tx - 1][sy - 1]
        return res


def main():
    cnt = Counter(aij for ai in A for aij in ai)
    acc2d = {}
    for a in cnt:
        acc2d[a] = Accumulate_2d(a)

    res = len(cnt)

    for a, v in cnt.items():

        for i in range(H - P + 1):
            ans = []
            for j in range(W - Q + 1):
                res -= (v == acc2d[a].query(i + 1, j + 1))
            ans.append(res)
        print(*ans)
    return


if __name__ == '__main__':
    H, W, N, P, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    main()
