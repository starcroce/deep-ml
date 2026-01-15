def _transpose_matrix(matrix):
	row, col = len(matrix), len(matrix[0])
	mat = [[0 for _ in range(row)] for _ in range(col)]
	for i in range(row):
		for j in range(col):
			mat[j][i] = matrix[i][j]
	return mat

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "column":
		matrix = _transpose_matrix(matrix)
	for row in matrix:
		means.append(sum(row) / len(row))
	return means