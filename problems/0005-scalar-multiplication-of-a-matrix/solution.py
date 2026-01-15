def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	row, col = len(matrix), len(matrix[0])
    res = [[0 for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            res[i][j] = matrix[i][j] * scalar
    return res