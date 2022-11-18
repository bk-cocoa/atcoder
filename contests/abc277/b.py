N = int(input())
L = []
for i in range(N):
    L.append(input())
suit_s = 'HDCS'
num_s = 'A23456789TJQK'
for s in L:
    if not s[0] in suit_s:
        print('No')
        exit()

for s in L:
    if not s[1] in num_s:
        print('No')
        exit()

if len(set(L)) != len(L):
    print('No')
    exit()

print('Yes')
