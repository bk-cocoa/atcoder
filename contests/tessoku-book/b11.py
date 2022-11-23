def is_ok(arg):
    return A_L[arg] < X


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
A_L = list(map(int, input().split()))
A_L.sort()

Q = int(input())
for i in range(Q):
    X = int(input())
    ok = 0
    ng = N
    print(meguru_bisect(ng, ok) + 1)
