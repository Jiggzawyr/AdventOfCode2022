with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    matrix = []
    for line in lines:
        row = []
        for l in line:
            row.append(int(l))
        matrix.append(row)
    M = len(matrix)
    N = len(matrix[0])
    best_scenic_score = 0
    for m, row in enumerate(matrix):
        for n, elem in enumerate(row):
            scenic_score = 1
            for cnt in range(4):
                i = m
                j = n
                multiplier = 0
                if cnt == 0: j += 1
                elif cnt == 1: i += 1
                elif cnt == 2: j -= 1
                else: i -= 1
                while i >= 0 and i < M and j >= 0 and j < N:
                    multiplier += 1
                    if matrix[i][j] >= matrix[m][n]:
                        break
                    if cnt == 0: j += 1
                    elif cnt == 1: i += 1
                    elif cnt == 2: j -= 1
                    else: i -= 1
                scenic_score *= multiplier
            if scenic_score > best_scenic_score: best_scenic_score = scenic_score
    print("best_scenic_score: ", best_scenic_score)