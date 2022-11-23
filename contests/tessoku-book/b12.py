N = int(input())


def is_ok(arg):
    return arg * arg * arg + arg <= N


def meguru_bisect(ng, ok):
    while abs(ok - ng) > 0.0001:
        mid = (ok + ng) / 2
        # mid = (ok + ng) // 2

        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ng = 10000
ok = 0
print(meguru_bisect(ng, ok))
