def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    row, col = len(a), len(a[0])
    res = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            res[j][i] = a[i][j]
    return res