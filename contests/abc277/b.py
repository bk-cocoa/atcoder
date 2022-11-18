N = int(input())
L = []
for i in range(N):
    L.append(input())
# TODO:タプルじゃなくて良いですね
suit_s = ('H', 'D', 'C', 'S')
num_s = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
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
