H, M = map(int, input().split())

while True:

    hh = str(H).zfill(2)
    mm = str(M).zfill(2)

    hh2 = hh[0] + mm[0]
    mm2 = hh[1] + mm[1]

    if 0 <= int(hh2) <= 23 and 0 <= int(mm2) <= 59:
        print(H, M)
        break

    M += 1
    if M == 60:
        M = 0
        H += 1
    if H == 24:
        H = 0
