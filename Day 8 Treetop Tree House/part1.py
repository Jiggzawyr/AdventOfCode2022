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
    visible_count = 0
    for m, row in enumerate(matrix):
        for n, elem in enumerate(row):
            for cnt in range(4):
                i = m
                j = n
                visible = True
                if cnt == 0: j += 1
                elif cnt == 1: i += 1
                elif cnt == 2: j -= 1
                else: i -= 1
                while i >= 0 and i < M and j >= 0 and j < N:
                    if matrix[i][j] >= matrix[m][n]:
                        visible = False
                        break
                    if cnt == 0: j += 1
                    elif cnt == 1: i += 1
                    elif cnt == 2: j -= 1
                    else: i -= 1
                if visible: 
                    visible_count += 1
                    break
    print("visible_count: ", visible_count)