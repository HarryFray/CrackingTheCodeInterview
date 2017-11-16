import unittest
''' check out answer on line looks way better than this'''
def zero_matrix(matrix):
    colwzero = []
    rowwzero = []
    '''figure out how to remove these counts simplify 4-loops'''
    countrow = -1
    countcol = 0
    '''finds locations of zeros stores in row zero and row col'''
    for row in matrix:
        countrow += 1
        for num in row:
            if num == 0:
                rowwzero.append(countrow)
                colwzero.append(countcol)
            countcol += 1
        countcol = 0

    ''' changes rows and cols to zeros based on found locations
    simplify here with another function'''
    for ii in rowwzero:
        for row in range(len(matrix)):
            matrix[ii][row] = 0
    for ii in range(len(matrix)):
        for col in colwzero:
            matrix[ii][col] = 0

    return matrix

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
