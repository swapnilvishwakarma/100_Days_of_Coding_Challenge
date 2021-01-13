# Given an array of distinct integers candidates and a target integer target, return a list of all unique 
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in 
# any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique 
# if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 
# combinations for the given input.

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        dp = [ [] for _ in range(target+1)]

        for c in candidates:                   # O(N): for each candidate
            for i in range(c, target+1):       # O(M): for each possible value <= target
                if i == c:
                    dp[i].append([c])
                for comb in dp[i-c]:           # O(M) worst: for each combination
                    dp[i].append(comb + [c])

        return dp[-1]

sol = Solution()
print(sol.combinationSum([2,3,6,7], 10))
