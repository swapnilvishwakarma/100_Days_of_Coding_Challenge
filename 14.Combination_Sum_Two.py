# Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
# combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        ans = []

        def dfs(idx, path, target):
            if idx > len(candidates):
                return

            if target == 0:
                ans.append(path)
                
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    return
                dfs(i+1, path+[candidates[i]], target-candidates[i])

        dfs(0, [], target)
        return ans

sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))