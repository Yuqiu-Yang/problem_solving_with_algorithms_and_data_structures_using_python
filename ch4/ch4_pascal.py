def dpPascal(n_row):
    triangle = []
    for r in range(n_row):
        temp_list = []
        for c in range(r+1):
            if (c == 0) or (c == r):
                temp_list.append(1)
            else:
                temp_list.append((triangle[r - 1][c - 1]) + \
                                    (triangle[r - 1][c]))
        triangle.append(temp_list)
    return triangle

print(dpPascal(5))


def recGetPascal(row_ind, col_ind):
    if col_ind > row_ind:
        raise ValueError("Column num should be less than or equal to Row num")
    if (col_ind == 0) or (col_ind == row_ind) or (row_ind == 0):
        return 1
    else:
        return recGetPascal(row_ind - 1, col_ind - 1) + recGetPascal(row_ind - 1, col_ind)


print(recGetPascal(0,0))
print(recGetPascal(4,2))
