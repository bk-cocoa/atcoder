# B03 - Supermarket 1

N = int(input())
A_L = list(map(int, input().split()))

for a in range(N):
    for b in range(N):
        for c in range(N):
            if a == b or b == c or c == a:
                continue
            if A_L[a] + A_L[b] + A_L[c] == 1000:
                print('Yes')
                exit()
print('No')
