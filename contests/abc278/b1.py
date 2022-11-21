H, M = map(int, input().split())

while True:
    hh = str(H).zfill(2)
    mm = str(M).zfill(2)

    if 0 <= int(hh[0] + mm[0]) <= 23 and 0 <= int(hh[1] + mm[1]) <= 59:
        print(H, M)
        exit()

    M += 1
    if M == 60:
        M = 0
        H += 1
        H %= 24
