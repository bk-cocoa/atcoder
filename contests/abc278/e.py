H, W, N, h, w = map(int, input().split())
grid_L = []
for i in range(H):
    grid_L.append(list(map(int, input().split())))

inf = 10 ** 18
row_min_L = [inf] * N
col_min_L = [inf] * N
row_max_L = [0] * N
col_max_L = [0] * N

for row in range(H):
    for col in range(W):
        num = grid_L[row][col] - 1

        row_min_L[num] = min(row_min_L[num], row)
        col_min_L[num] = min(col_min_L[num], col)
        row_max_L[num] = max(row_max_L[num], row)
        col_max_L[num] = max(col_max_L[num], col)

for mask_min_row in range(H - h + 1):
    ans_L = [0 for i in range(W - w + 1)]
    for mask_min_col in range(W - w + 1):
        mask_max_row = mask_min_row + h - 1
        mask_max_col = mask_min_col + w - 1
        for num in range(N):
            if row_min_L[num] == inf:
                continue
            if mask_min_row <= row_min_L[num] and mask_min_col <= col_min_L[num] and row_max_L[num] <= mask_max_row and \
                    col_max_L[num] <= mask_max_col:
                continue
            else:
                ans_L[mask_min_col] += 1
    print(*ans_L)
