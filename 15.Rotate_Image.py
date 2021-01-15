# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: list) -> list:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # l = len(matrix)
        # for i in range(l):
        #     for j in range(l):
        #         temp = matrix[i][l-1]
        #         if j != l:
        #             matrix[j][l-1] = matrix[i][j]
        #         else:
        #             matrix[j][l-1] = temp
        #     l -= 1
        
        matrix.reverse() # Reverse
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] # Transpose

        return matrix

sol = Solution()
print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))