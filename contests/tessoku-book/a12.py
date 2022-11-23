N, K = map(int, input().split())
A_L = list(map(int, input().split()))


def is_ok(arg):
    score = 0
    for a in A_L:
        score += arg // a
    return score >= K


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ng = 0
ok = 10 ** 18
print(meguru_bisect(ng, ok))
