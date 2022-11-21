# A02 - Linear Search
N, X = map(int, input().split())
A_s = set(map(int, input().split()))
if X in A_s:
    print('Yes')
else:
    print('No')
