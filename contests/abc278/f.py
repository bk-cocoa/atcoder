N = int(input())
word_L = []
for i in range(N):
    word_L.append(input())

# dp[状態][最後に使った単語] := 1/勝ち、0/負け
# 状態：1/使える、0/使えない
dp = [[0] * N for i in range(1 << N)]

for status in range(1 << N):
    for prev_word in range(N):
        last_char = word_L[prev_word][-1]
        for next_word in range(N):
            if last_char != word_L[next_word][0]:
                continue
            if (status >> next_word) & 1 == 0:
                continue

            next_status = status ^ (1 << next_word)
            if dp[next_status][next_word] == 0:
                dp[status][prev_word] = 1
                break
base = (1 << N) - 1
for i in range(N):
    if dp[base ^ (1 << i)][i] == 0:
        print('First')
        exit()
print('Second')
