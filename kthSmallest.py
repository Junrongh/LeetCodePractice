def kthSmallest(matrix, k):
    (m, n) = len(matrix), len(matrix[0])
    jud = [[0] * n for row in range(0, m)]
    i = 0
    j = 0
    complist = [(matrix[i][j], i, j)]
    jud[i][j] = 1
    count = 0
    print jud

    while count < k:
        out = min(complist)
        complist.remove(out)
        ans, i, j = out
        count = count + 1
        if out[1] < m - 1:
            if jud[i + 1][j] == 0:
                complist.append((matrix[i + 1][j], i + 1, j))
                jud[i + 1][j] = 1
        if out[2] < n - 1:
            if jud[i][j + 1] == 0:
                complist.append((matrix[i][j + 1], i, j + 1))
                jud[i][j + 1] = 1
    return ans