# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: list) -> list:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]

        return result

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))