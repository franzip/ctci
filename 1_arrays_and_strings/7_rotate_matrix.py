from typing import List


def rotate_matrix(matrix: List[List[str]]) -> List[List[str]]:
    """
    In-place shift a matrix by 90°
    """
    length = len(matrix)
    even = length % 2 == 0
    iterations = length if even else length - 1
    last_col = iterations - 1 if even else iterations

    for i in range(iterations):
        if even and i == last_col:
            idx = length // 2 - 1
            matrix[idx][idx + 1], matrix[idx + 1][idx + 1], matrix[idx][idx], matrix[idx +
                                                                                     1][idx] = matrix[idx][idx], matrix[idx][idx + 1], matrix[idx + 1][idx], matrix[idx + 1][idx + 1]
        else:
            matrix[0][i], matrix[i][last_col], matrix[last_col][last_col -
                                                                i], matrix[last_col - i][0] = matrix[last_col - i][0], matrix[0][i], matrix[i][last_col], matrix[last_col][last_col - i]

    return matrix


assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
    [7, 4, 1], [8, 5, 2], [9, 6, 3]]
assert rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) == [
    [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
