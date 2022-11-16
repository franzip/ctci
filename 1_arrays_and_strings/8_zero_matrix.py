from typing import List


def zero_matrix(matrix: List[List[str]]) -> List[List[str]]:
    """
    When a 0 is found in matrix, writes all 0 in the related row and column
    """
    rows, cols = len(matrix), len(matrix[0])
    col_to_row_zero = set()

    for row in range(rows):
        zero_row = False

        for col in range(cols):
            if col in col_to_row_zero:
                continue

            if matrix[row][col] == 0:
                zero_row = True
                col_to_row_zero.add(col)

                for row_to_zero in range(rows):
                    # zero the column
                    matrix[row_to_zero][col] = 0

        # zero the row
        if zero_row:
            matrix[row] = [0 for x in range(cols)]

    return matrix


assert zero_matrix([[1, 2, 3],  [4, 0, 6], [7, 6, 9]]) == [
    [1, 0, 3], [0, 0, 0], [7, 0, 9]]
assert zero_matrix([[0, 0, 3, 4], [1, 2, 3, 4], [5, 6, 7, 8]]) == [
    [0, 0, 0, 0], [0, 0, 3, 4], [0, 0, 7, 8]]
