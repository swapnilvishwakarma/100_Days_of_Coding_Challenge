# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.
import collections
import math

class Solution:
    def shortestSubarray(self, A: list, K: int) -> int:
        pre = [0]
        
        for num in A:
            pre.append(pre[-1]+num)
            
        deque = collections.deque()
        result = float(math.inf)
        
        for i,sum_ in enumerate(pre):
            while(deque and deque[-1][1] >=sum_):
                deque.pop()
            
            while deque and sum_ - deque[0][1] >= K:
                result = min(i-deque[0][0], result)
                deque.popleft()
                
            deque.append([i,sum_])

        print(result if result!= float(math.inf) else -1)    
        return result if result!= float(math.inf) else -1

sol = Solution()
sol.shortestSubarray(A = [2,-1,2], K = 3)