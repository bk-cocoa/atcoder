N = int(input())
A_L = list(map(int, input().split()))

accum_L = [0]
for a in A_L:
    accum_L.append(accum_L[-1] + a)

Q = int(input())
for i in range(Q):
    L, R = list(map(int, input().split()))
    total_cnt = R - (L - 1)
    win_cnt = accum_L[R] - accum_L[L - 1]
    lose_cnt = total_cnt - win_cnt

    if win_cnt > lose_cnt:
        print('win')
    elif win_cnt < lose_cnt:
        print('lose')
    else:
        print('draw')
