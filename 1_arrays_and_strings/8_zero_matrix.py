from typing import List


def zero_matrix(matrix: List[List[str]]) -> List[List[str]]:
    """
    When a 0 is found in matrix, writes all 0 in the related row and column
    """
    rows, cols = len(matrix), len(matrix[0])
    colToRowZeroMap = {}

    for row in range(rows):
        zeroRow = False
        for col in range(cols):
            if colToRowZeroMap.get(col):
                continue
            if matrix[row][col] == 0:
                zeroRow = True
                for rowToZero in range(rows):
                    matrix[rowToZero][col] = 0
                colToRowZeroMap[col] = True
        if zeroRow:
            matrix[row] = [0 for x in range(cols)]

    return matrix


assert zero_matrix([[1, 2, 3],  [4, 0, 6], [7, 6, 9]]) == [
    [1, 0, 3], [0, 0, 0], [7, 0, 9]]
assert zero_matrix([[0, 0, 3, 4], [1, 2, 3, 4], [5, 6, 7, 8]]) == [
    [0, 0, 0, 0], [0, 0, 3, 4], [0, 0, 7, 8]]
