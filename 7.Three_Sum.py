# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all 
# unique triplets in the array which gives the sum of zero.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: list) -> list:
        res = set()
        
        # Split into 3: negative, positive and zero lists
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
            
        # Create a separate list of negatives and positives for O(1) look-up
        N, P = set(n), set(p)

        # If atleast 1 zero is present, find both complements of a non-zero number. Eg. (-1, 0, 1)
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        # If atleast 3 zeros are present
        if len(z) >= 3:
            res.add((0, 0, 0))
        
        # For all pairs of -ve nos., check if the sum of complement is present
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

         # For all pairs of +ve nos., check if the sum of complement is present
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))
                    
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
