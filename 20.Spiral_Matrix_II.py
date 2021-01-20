class Solution:
    def generateMatrix(self, n: int) -> list:
        k = 0 # current number
        x = 0 # x position 
        y = -1 # y position
        res = [[0 for _ in range(n)] for _ in range(n)] # empty n x n 

        # Set these to opposite of what you want it to be
        dx = -1 # direction of x
        dy = -1 # direction of y
        magx = n + 1 # magnitude of x
        magy = n # magnitude of y

        while(k < n ** 2):
            # move across horizontally 
            magx -= 1 # decrement
            dx *= -1 # flip direction
            for _ in range(magx):
                k += 1 # increment current value
                y += dx # move horizontally
                res[x][y] = k

            # move across vertically
            magy -= 1 # decrement
            dy *= -1 # flip direction
            for _ in range(magy):
                k += 1 # increment current value
                x += dy # move vertically
                res[x][y] = k 

        return res

sol = Solution()
print(sol.generateMatrix(3))
