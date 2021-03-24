# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take to finish all the given tasks.

from collections import Counter

class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:

        # create list of process occurances 
        occurances = list(Counter(tasks).values())
        
        # base interval calculation = # of groups * size of each group
        intervals = (max(occurances)-1) * (n+1)
        
        # account for remaining intervals from processes with most occurances
        count_procc_with_max = occurances.count(max(occurances))
        
        # add these to your total interval count
        intervals += count_procc_with_max
        
        # return max of calculated intervals and length of initials task list
        print(max(intervals, len(tasks)))
        return max(intervals, len(tasks))
    
sol = Solution()
sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)
    
    
#         seen = {}
#         for i in tasks:
#             if i in seen:
#                 seen[i] += 1
#             else:
#                 seen[i] = 0
        
#         if n == 0:
#             return len(tasks)
        
#         print(seen)
        
#         CPU = 0
#         for i in seen:
#             if seen[i] == 0:
#                 CPU += 1
#             else:
#                 CPU += n*seen[i]
        
#         return CPU