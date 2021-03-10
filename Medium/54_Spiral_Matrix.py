class Solution(object):
    def spiralOrder(self, matrix):
        # A O(n) Solution A top 100% Solution
        # We define a map direction 1, 2, 3 and 4 | right, down, left and up
        d = 1
        i, j = 0, 0
        result_list = []
        # An empty Matrix
        if matrix == []:
            return []
        # A single column matrix
        if len(matrix[0]) == 1:
            for i in matrix:
                result_list.append(i[0])
            return result_list
        # A single row matrix
        if len(matrix) == 1:
            return matrix[0]
        # A ( m x n ) matrix
        while (True):
            # Test is the cell is visited or not
            if (matrix[i][j] != 500):
                result_list.append(matrix[i][j])
                # Tag the cell with 500
                matrix[i][j] = 500
            else:
                break
            # d == 1 Right direction
            if (d == 1):
                if (j < (len(matrix[1]) - 1)) and (matrix[i][j+1] != 500):
                    j+=1
                if not ((j < (len(matrix[1]) - 1)) and (matrix[i][j+1] != 500)):
                    d = 2
            # d == 2 Down direction
            elif (d == 2):
                if (i < (len(matrix) - 1)) and (matrix[i+1][j] != 500):
                    i+=1
                if not ((i < (len(matrix) - 1)) and (matrix[i+1][j] != 500)):
                    d = 3
            # d == 3 Left direction
            elif (d == 3):
                if (j > 0) and (matrix[i][j-1] != 500):
                    j-=1
                if not((j > 0) and (matrix[i][j-1] != 500)):
                    d = 4
            # d == 4 Up direction
            elif (d == 4):
                if (i > 0) and (matrix[i-1][j] != 500):
                    i-=1
                if not((i > 0) and (matrix[i-1][j] != 500)):
                    d = 1
        return result_list
